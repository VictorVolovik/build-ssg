import os
import re


from md_to_html import markdown_to_html_node
from file_helpers import create_folder

TITLE_PATTERN = r"^(#{1} ).+"

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
   dir = os.listdir(dir_path_content)
   for path in dir:
        path_src = os.path.join(dir_path_content, path)
        path_dst = os.path.join(dest_dir_path, path).replace('.md', ".html")
        if os.path.isfile(path_src):
            generate_page(path_src, template_path, path_dst)
        else:
            create_folder(path_dst)
            generate_pages_recursive(path_src, template_path, path_dst)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    html = generate_page_html(from_path, template_path)
    write_page_to_file(html, dest_path)


def write_page_to_file(html, dest_path):
    dirs = os.path.dirname(dest_path)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    with open(dest_path, "w") as file:
        file.write(html)


def generate_page_html(from_path, template_path):
    with open(from_path, encoding="utf-8") as file:
        markdown = file.read()

    with open(template_path, encoding="utf-8") as file:
        template = file.read()

    title = extract_title(markdown)
    html_content = markdown_to_html_node(markdown).to_html()
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    return html


def extract_title(markdown):
    lines = markdown.split("\n")
    first_line = lines[0]
    matches = re.findall(TITLE_PATTERN, first_line)

    if len(matches) == 0:
        raise Exception("No title found")

    heading_signs = matches[0]
    title = first_line.lstrip(heading_signs)
    return title
