import re

from block_processor import (
    markdown_to_blocks,
    block_to_block_type,
    HEADING_PATTERN,
    OREDERED_LIST_LINE_PATTERN,
    BlockType,
)
from inline_processor import text_to_textnodes
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = list(map(block_to_html_node, blocks))
    root_node = ParentNode(tag="div", children=html_nodes)
    return root_node


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    html_node = create_block_node(block_type, block)
    return html_node


def create_block_node(block_type: BlockType, block):
    match block_type:
        case BlockType.HEADING:
            return create_heading(block)
        case BlockType.CODE:
            return create_code(block)
        case BlockType.QUOTE:
            return create_quote(block)
        case BlockType.UNORDERED_LIST:
            return create_unordered_list(block)
        case BlockType.ORDERED_LIST:
            return create_ordered_list(block)
        case BlockType.PARAGRAPH:
            return create_paragraph(block)
        case _:
            raise Exception("Unknown block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return list(map(lambda text_node: text_node_to_html_node(text_node), text_nodes))


def create_heading(block):
    matches = re.findall(HEADING_PATTERN, block)
    heading_signs = matches[0]
    heading_level = heading_signs.count("#")
    cleared = block.lstrip(heading_signs)
    children = text_to_children(cleared)
    return ParentNode(tag=f"h{heading_level}", children=children)


def create_code(block):
    cleared = block.strip("```")
    children = text_to_children(cleared)
    code = ParentNode(tag="code", children=children)
    return ParentNode(tag="pre", children=[code])


def create_quote(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        if line == ">":
            children.append(LeafNode(tag="br", value=""))
            continue
        cleared_line = line.lstrip("> ")
        line_children = text_to_children(cleared_line)
        children.append(ParentNode(tag="p", children=line_children))
    return ParentNode(tag="blockquote", children=children)


def create_unordered_list(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        cleared_line = line.lstrip("* ").lstrip("- ").lstrip("+ ")
        line_children = text_to_children(cleared_line)
        children.append(ParentNode(tag="li", children=line_children))
    return ParentNode(tag="ul", children=children)


def create_ordered_list(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        matches = re.findall(OREDERED_LIST_LINE_PATTERN, line)
        line_numbering = matches[0]
        cleared = line.lstrip(line_numbering)
        line_children = text_to_children(cleared)
        children.append(ParentNode(tag="li", children=line_children))
    return ParentNode(tag="ol", children=children)


def create_paragraph(block):
    children = text_to_children(block)
    return ParentNode(tag="p", children=children)
