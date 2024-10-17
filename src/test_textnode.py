import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
