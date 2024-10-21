from prepare_static_files import prepare_static_files
from generate_pages import generate_page


def main():
    prepare_static_files()
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
