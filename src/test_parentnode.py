import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_no_tag_to_html_error(self):
        with self.assertRaises(ValueError):
            node = ParentNode(
                tag="div",
                children=[
                    LeafNode(tag="p", value="test 1"),
                    LeafNode(tag="p", value="test 2"),
                ],
            )
            node.tag = None
            node.to_html()

    def test_no_children_to_html_error(self):
        with self.assertRaises(ValueError):
            node = ParentNode(
                tag="div",
                children=[
                    LeafNode(tag="p", value="test 1"),
                    LeafNode(tag="p", value="test 2"),
                ],
            )
            node.children = None
            node.to_html()

    def test_empty_children_to_html_error(self):
        with self.assertRaises(ValueError):
            node = ParentNode(
                tag="div",
                children=[],
            )
            node.to_html()

    def test_basic_children_to_html(self):
        node = ParentNode(
            tag="div",
            children=[
                LeafNode(tag="p", value="test1"),
                LeafNode(tag="p", value="test2"),
            ],
            props={"class": "text"},
        )
        html = node.to_html()
        expected = '<div class="text"><p>test1</p><p>test2</p></div>'
        self.assertEqual(html, expected)

    def test_nested_children_to_html(self):
        node = ParentNode(
            tag="main",
            children=[
                ParentNode(
                    tag="div",
                    children=[
                        LeafNode(tag="p", value="test1"),
                        LeafNode(tag="p", value="test2"),
                    ],
                    props={"class": "text"},
                ),
                ParentNode(
                    tag="ul",
                    children=[
                        LeafNode(tag="li", value="item"),
                    ],
                ),
            ],
        )
        html = node.to_html()
        expected = '<main><div class="text"><p>test1</p><p>test2</p></div><ul><li>item</li></ul></main>'
        self.assertEqual(html, expected)


if __name__ == "__main__":
    unittest.main()
