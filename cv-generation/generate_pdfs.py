import os
import json
import logging
from urllib.parse import quote
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from data_structures import CV

def get_all_available_jsons(json_dir: str = "./output") -> list[str]:
    return [
        os.path.join(json_dir, f)
        for f in os.listdir(json_dir)
        if f.endswith(".json")
    ]

def avatar_url(seed: str) -> str:
    """ Simple function to generate an avatar URL based on a seed string. """
    return f"https://api.dicebear.com/9.x/toon-head/svg?seed={quote(seed)}"


def render_cv_html(cv: CV) -> str:
    env = Environment(loader=FileSystemLoader("templates"))
    cv_data = cv.model_dump()
    cv_data["avatar_url"] = avatar_url(f"{cv.avatar_seed}")
    template = env.get_template("cv.html")
    return template.render(**cv_data)


def html_to_pdf(html: str, output_path: str):
    HTML(string=html, base_url=".").write_pdf(output_path)


def generate_pdfs_from_available_jsons():
    logging.info("Generating PDF CVs from available JSONs...")
    json_files = get_all_available_jsons()
    for i, json_file in enumerate(json_files):
        try:
            logging.info(f"Processing {json_file} ({i+1}/{len(json_files)})")
            with open(json_file, "r") as f:
                cv_data = CV(**json.load(f))            
            filename = os.path.basename(json_file)
            pdf_path = os.path.join("output", f"{filename[:-5]}.pdf")
            html_to_pdf(render_cv_html(cv_data), pdf_path)
            logging.info(f"Saved PDF CV to {pdf_path}")
        except Exception as e:
            logging.error(f"Failed to generate PDF from {json_file}: {e}")