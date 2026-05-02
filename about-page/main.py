from pathlib import Path
from data import mobility_datasets
from babel.support import Translations
from jinja2 import Environment, select_autoescape, FileSystemLoader


def main():
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(),
        extensions=["jinja2.ext.i18n"],
        lstrip_blocks=True,
        trim_blocks=True,
    )
    env.policies["ext.i18n.trimmed"] = True

    out_directory = Path(__file__).parent / "public"

    pages = {"index": "main"}

    for lang in ["de", "en"]:
        translations = Translations.load("translations", [lang, "en"])
        env.install_gettext_translations(translations)

        def localize(input: dict[str, str]) -> str:
            return input[lang]

        env.filters["localize"] = localize

        for out_name, template_name in pages.items():
            template = env.get_template(f"{template_name}.html")
            html = template.render(
                {
                    "mobility_datasets": mobility_datasets,
                    "lang": lang,
                }
            )
            out_dir = out_directory / lang
            out_dir.mkdir(exist_ok=True)
            out_file = out_dir / f"{out_name}.html"
            out_file.write_text(html)


if __name__ == '__main__':
    main()
