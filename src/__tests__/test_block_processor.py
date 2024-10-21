import unittest
import sys

sys.path.append("./src")

from block_processor import markdown_to_blocks, block_to_block_type, BlockType


class TestHTMLNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        blocks = markdown_to_blocks(md)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]
        self.assertEqual(blocks, expected)

    def test_block_to_block_type_heading(self):
        block = "# Example first level heading"
        block_type = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_subheading(self):
        block = "### Example third level heading"
        block_type = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_code(self):
        block = "```npm start```"
        block_type = block_to_block_type(block)
        expected = BlockType.CODE
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_multiple_lines_code(self):
        block = """```
npm install
npm start
```"""
        block_type = block_to_block_type(block)
        expected = BlockType.CODE
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_quote(self):
        block = "> This a quote"
        block_type = block_to_block_type(block)
        expected = BlockType.QUOTE
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_multiple_lines_quote(self):
        block = """> This a quote
> which has
> several lines of text"""
        block_type = block_to_block_type(block)
        expected = BlockType.QUOTE
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_unordered_list(self):
        block = """- item
* which has
+ several lines of text"""
        block_type = block_to_block_type(block)
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_ordered_list(self):
        block = """1. item
2. which has
3. several lines of text"""
        block_type = block_to_block_type(block)
        expected = BlockType.ORDERED_LIST
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_ordered_list_auto_ordering(self):
        block = """1. item
1. which has
1. several lines of text"""
        block_type = block_to_block_type(block)
        expected = BlockType.ORDERED_LIST
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_ordered_list_incorrect_start(self):
        block = """2. item
4. which has
6. several lines of text"""
        block_type = block_to_block_type(block)
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_paragraph(self):
        block = "Just a regular paragraph"
        block_type = block_to_block_type(block)
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_type, expected)


if __name__ == "__main__":
    unittest.main()
