import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_no_value_to_html_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="b", value="test")
            node.value = None
            node.to_html()

    def test_no_tag_to_html(self):
        node = LeafNode(value="test text")
        html = node.to_html()
        expected = "test text"
        self.assertEqual(html, expected)

    def test_to_html(self):
        node = LeafNode(tag="p", value="test parapgraph")
        html = node.to_html()
        expected = "<p>test parapgraph</p>"
        self.assertEqual(html, expected)

    def test_to_html_with_props(self):
        node = LeafNode(
            tag="button", value="test", props={"class": "btn", "type": "submit"}
        )
        html = node.to_html()
        expected = '<button class="btn" type="submit">test</button>'
        self.assertEqual(html, expected)

    def test_to_html_with_emty_value(self):
        node = LeafNode(tag="div", value="")
        html = node.to_html()
        expected = "<div></div>"
        self.assertEqual(html, expected)

    def test_to_html_with_emty_value_if_void(self):
        node = LeafNode(tag="img", value="", props={"src": "/test.png", "alt": "test"})
        html = node.to_html()
        expected = '<img src="/test.png" alt="test">'
        self.assertEqual(html, expected)


if __name__ == "__main__":
    unittest.main()
