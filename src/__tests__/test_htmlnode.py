import unittest
import sys

sys.path.append("./src")

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            tag="ul",
            children=[HTMLNode("li", "test")],
            props={"class": "list"},
        )
        result = node.__repr__()
        expected = "HTMLNode(tag: ul, value: None, children: [HTMLNode(tag: li, value: test, children: None, props: None)], props: {'class': 'list'})"
        self.assertEqual(result, expected)

    def test_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html(self):
        node = HTMLNode(
            tag="input",
            props={"id": "fullName", "name": "fullName", "type": "text"},
        )
        html_props = node.props_to_html()
        expected = ' id="fullName" name="fullName" type="text"'
        self.assertEqual(html_props, expected)

    def test_props_to_html_defaults(self):
        node = HTMLNode(tag="p", value="test")
        html_props = node.props_to_html()
        expected = ""
        self.assertEqual(html_props, expected)

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="test", props={})
        html_props = node.props_to_html()
        expected = ""
        self.assertEqual(html_props, expected)

    def test_props_to_html_no_prop_value(self):
        node = HTMLNode(
            tag="button", value="test", props={"class": "test", "disabled": ""}
        )
        html_props = node.props_to_html()
        expected = ' class="test" disabled'
        self.assertEqual(html_props, expected)


if __name__ == "__main__":
    unittest.main()
