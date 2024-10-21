import unittest
import sys

sys.path.append("./src")

from md_to_html import markdown_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.
"""
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        expected = "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p></div>"
        self.assertEqual(html, expected)

    def test_markdown_to_blocks_with_code(self):
        md = """```
npm install
npm start
```"""
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        expected = """<div><pre><code>
npm install
npm start
</code></pre></div>"""
        self.assertEqual(html, expected)

    def test_markdown_to_blocks_with_code_and_quote(self):
        md = """
```
npm install
npm start
```

> let's get dangerous 
"""
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        expected = """<div><pre><code>
npm install
npm start
</code></pre><blockquote><p>let's get dangerous</p></blockquote></div>"""
        self.assertEqual(html, expected)

    def test_markdown_to_blocks_with_code_and_multiline_quote(self):
        md = """
```
npm install
npm start
```

> The way to get started is to quit talking and begin doing.
> - Walt Disney
"""
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        expected = """<div><pre><code>
npm install
npm start
</code></pre><blockquote><p>The way to get started is to quit talking and begin doing.</p><p>- Walt Disney</p></blockquote></div>"""
        self.assertEqual(html, expected)

    def test_markdown_to_blocks_with_unordered_list(self):
        md = """
- item
* item
+ item
"""
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        expected = "<div><ul><li>item</li><li>item</li><li>item</li></ul></div>"
        self.assertEqual(html, expected)

    def test_markdown_to_blocks_with_ordered_list(self):
        md = """
1. item
1. item
1. item
"""
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        expected = "<div><ol><li>item</li><li>item</li><li>item</li></ol></div>"
        self.assertEqual(html, expected)


if __name__ == "__main__":
    unittest.main()
