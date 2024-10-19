import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    strings = markdown.split("\n\n")

    stripped_strings = []
    for string in strings:
        stripped = string.strip()
        if string != "\n" and len(stripped) > 0:
            stripped_strings.append(stripped)

    return stripped_strings


def is_heading_block(block):
    # Headings start with 1-6 # characters, followed by a space and then the heading text
    matches = re.findall(r"^(#{1,6} ).+", block)
    return len(matches) > 0


def is_code_block(block):
    # Code blocks must start with 3 backticks and end with 3 backticks
    matches = re.findall(r"^(`{3}).+(`{3})$", block, flags=re.MULTILINE | re.DOTALL)
    return len(matches) > 0


def is_quote_block(block):
    # Every line in a quote block must start with a > character
    lines = block.split("\n")
    are_lines_quoted = list(map(lambda line: line.startswith("> "), lines))
    all_lines_quoted = all(are_lines_quoted)
    return all_lines_quoted


def is_unordered_list_block(block):
    # Every line in an unordered list block must start with dashes (-), asterisks (*), or plus signs (+), followed by a space
    lines = block.split("\n")
    are_lines_listed = list(
        map(
            lambda line: line.startswith("* ")
            or line.startswith("- ")
            or line.startswith("+ "),
            lines,
        )
    )
    all_lines_listed = all(are_lines_listed)
    return all_lines_listed


def is_ordered_list_block(block):
    # Every line in an ordered list block must start with a number followed by a . character and a space
    lines = block.split("\n")
    are_lines_listed = []
    line_pattern = r"^(\d+. ).+"
    # The numbers don’t have to be in numerical order, but the list should start with the number one
    first_line_pattern = r"^(1. ).+"
    for index in range(0, len(lines)):
        line = lines[index]
        if index == 0:
            matches = re.findall(first_line_pattern, line)
        else:
            matches = re.findall(line_pattern, line)
        are_lines_listed.append(len(matches) > 0)
    all_lines_listed = all(are_lines_listed)
    return all_lines_listed


def block_to_block_type(block):
    if is_heading_block(block):
        return BlockType.HEADING
    elif is_code_block(block):
        return BlockType.CODE
    elif is_quote_block(block):
        return BlockType.QUOTE
    elif is_unordered_list_block(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list_block(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
