import unittest
import sys

sys.path.append("./src")

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        result = node.__repr__()
        expected = "TextNode(This is a text node, bold text, None)"
        self.assertEqual(result, expected)

    def test_default_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        url = node.url
        self.assertIsNone(url)

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_no_url_link(self):
        with self.assertRaises(ValueError):
            TextNode("example", TextType.LINK)

    def test_no_url_image(self):
        with self.assertRaises(ValueError):
            TextNode("example", TextType.IMAGE)

    def test_text_node_to_html_node_has_incorrect_node_type(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node("test")

    def test_text_node_to_html_node_has_ukknown_node_type(self):
        with self.assertRaises(Exception):
            node = TextNode("This is regular text", "some text")
            text_node_to_html_node(node)

    def test_regular_text_node_to_html_node(self):
        node = TextNode("This is regular text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        result = html_node.__repr__()
        expected = "HTMLNode(tag: None, value: This is regular text, children: None, props: None)"
        self.assertEqual(result, expected)

    def test_regular_text_node_to_html(self):
        node = TextNode("This is regular text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        html = html_node.to_html()
        expected = "This is regular text"
        self.assertEqual(html, expected)

    def test_bold_text_node_to_html_node(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        result = html_node.__repr__()
        expected = (
            "HTMLNode(tag: b, value: This is bold text, children: None, props: None)"
        )
        self.assertEqual(result, expected)

    def test_bold_text_node_to_html(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        html = html_node.to_html()
        expected = "<b>This is bold text</b>"
        self.assertEqual(html, expected)

    def test_italic_text_node_to_html_node(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        result = html_node.__repr__()
        expected = (
            "HTMLNode(tag: i, value: This is italic text, children: None, props: None)"
        )
        self.assertEqual(result, expected)

    def test_italic_text_node_to_html(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        html = html_node.to_html()
        expected = "<i>This is italic text</i>"
        self.assertEqual(html, expected)

    def test_code_text_node_to_html_node(self):
        node = TextNode("npm start", TextType.CODE)
        html_node = text_node_to_html_node(node)
        result = html_node.__repr__()
        expected = "HTMLNode(tag: code, value: npm start, children: None, props: None)"
        self.assertEqual(result, expected)

    def test_code_text_node_to_html(self):
        node = TextNode("npm start", TextType.CODE)
        html_node = text_node_to_html_node(node)
        html = html_node.to_html()
        expected = "<code>npm start</code>"
        self.assertEqual(html, expected)

    def test_link_text_node_to_html_node(self):
        node = TextNode("example", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        result = html_node.__repr__()
        expected = "HTMLNode(tag: a, value: example, children: None, props: {'href': 'https://example.com'})"
        self.assertEqual(result, expected)

    def test_link_text_node_to_html(self):
        node = TextNode("example", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        html = html_node.to_html()
        expected = '<a href="https://example.com">example</a>'
        self.assertEqual(html, expected)

    def test_image_text_node_to_html_node(self):
        node = TextNode("test", TextType.IMAGE, "/test.png")
        html_node = text_node_to_html_node(node)
        result = html_node.__repr__()
        expected = (
            "HTMLNode(tag: img, value: "
            ", children: None, props: {'src': '/test.png', 'alt': 'test'})"
        )
        self.assertEqual(result, expected)

    def test_image_text_node_to_html(self):
        node = TextNode("test", TextType.IMAGE, "/test.png")
        html_node = text_node_to_html_node(node)
        html = html_node.to_html()
        expected = '<img src="/test.png" alt="test">'
        self.assertEqual(html, expected)


if __name__ == "__main__":
    unittest.main()
