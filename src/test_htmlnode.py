import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="input",
            props={"id": "fullName", "name": "fullName", "type": "text"},
        )
        props = node.props_to_html()
        expected = 'id="fullName" name="fullName" type="text"'
        self.assertEqual(props, expected)

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


if __name__ == "__main__":
    unittest.main()
