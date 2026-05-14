import json
from pathlib import Path

from babel.support import Translations
from jinja2 import Environment, FileSystemLoader, select_autoescape

from data import mobility_datasets


def load_gbfs_info():
    with open("../gbfs/gbfs.json") as f:
        data = json.load(f)

    final_data = []
    for k, v in data.items():
        si = v["system_info"]
        name = si["name"]
        if not isinstance(name, str):
            # I don't want to write this properly
            if "Getaround" in json.dumps(name):
                name = "Getaround"
            else:
                raise RuntimeError()
        final_data.append(
            {
                "key": k,
                "name": name,
                "url": v["url"],
                "license_id": si.get("license_id", None),
                "license_url": si.get("license_url", None),
                "operator": si.get("operator", None),
                "raw": json.dumps(si, indent=2, ensure_ascii=False),
            }
        )
    return final_data


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

    gbfs_info = load_gbfs_info()

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
                    "gbfs_info": gbfs_info,
                    "lang": lang,
                }
            )
            out_dir = out_directory / lang
            out_dir.mkdir(exist_ok=True)
            out_file = out_dir / f"{out_name}.html"
            out_file.write_text(html)


if __name__ == "__main__":
    main()
