import unittest

from generate_pages import extract_title, generate_page_html


class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        md = """# test title
"""
        title = extract_title(md)
        expected = "test title"
        self.assertEqual(title, expected)

    def test_extract_title_failed(self):
        with self.assertRaises(Exception):
            md = """there is no title
"""
            extract_title(md)

    def test_generate_page_html(self):
        html = generate_page_html("src/test.md", "template.html")
        expected = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Test page</title>
    <link href="/index.css" rel="stylesheet" />
  </head>

  <body>
    <article><div><h1>Test page</h1><p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Incidunt, vel. Saepe temporibus accusamus architecto aspernatur? Possimus ratione corporis, consequatur doloremque quia maxime quidem nostrum suscipit? Nihil porro minima culpa odit?</p></div></article>
  </body>
</html>
"""
        self.assertEqual(html, expected)


if __name__ == "__main__":
    unittest.main()
