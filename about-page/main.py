from pathlib import Path
from data import mobility_datasets
from babel.support import Translations
from jinja2 import Environment, select_autoescape, FileSystemLoader

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(),
    extensions=["jinja2.ext.i18n"],
)

out_directory = Path(__file__).parent / "public"

for lang in ["de", "en"]:
    translations = Translations.load("translations", [lang, "en"])
    env.install_gettext_translations(translations)


    def localize(input: dict[str, str]) -> str:
        return input[lang]


    env.filters["localize"] = localize

    template = env.get_template("main.html")
    html = template.render({
        "mobility_datasets": mobility_datasets,
        "lang": lang,
    })
    out_dir = out_directory / lang
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / "index.html"
    out_file.write_text(html)
