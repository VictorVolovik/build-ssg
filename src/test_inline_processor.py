import unittest

from textnode import TextNode, TextType
from inline_processor import split_nodes_delimiter


class TestLeafNode(unittest.TestCase):
    def test_split_nodes_delimiter_for_bold_text(self):
        node = TextNode("This is some **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        excepted = [
            TextNode("This is some ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, excepted)

    def test_split_nodes_delimiter_for_italic_text(self):
        node = TextNode("This is some *italic* text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        excepted = [
            TextNode("This is some ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, excepted)

    def test_split_nodes_delimiter_for_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        excepted = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, excepted)

    def test_split_nodes_delimiter_at_start(self):
        node = TextNode("`code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        excepted = [
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, excepted)

    def test_split_nodes_delimiter_at_end(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        excepted = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
        ]
        self.assertEqual(new_nodes, excepted)

    def test_split_nodes_delimiter_empty(self):
        node = TextNode("This is text with an empty block `` of code", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        excepted = [
            TextNode("This is text with an empty block ", TextType.TEXT),
            TextNode(" of code", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, excepted)

    def test_split_nodes_delimiter_incorrect_no_matching_delimiter(self):
        with self.assertRaises(Exception):
            node = TextNode("This is some **bold* text", TextType.TEXT)
            split_nodes_delimiter([node], "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()
