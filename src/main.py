from prepare_static_files import prepare_static_files
from generate_pages import generate_pages_recursive


def main():
    prepare_static_files()
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
