import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue

        parts = node.text.split(sep=delimiter)
        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown syntax")

        for index in range(0, len(parts)):
            if len(parts[index]) > 0:
                if index % 2 != 0:
                    nodes.append(TextNode(parts[index], text_type))
                else:
                    nodes.append(TextNode(parts[index], TextType.TEXT))

    return nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT and len(node.text) > 0:
            nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if len(images) == 0:
            if len(node.text) > 0:
                nodes.append(node)
            continue

        image = images[0]
        image_alt, image_src = image
        parts = text.split(f"![{image_alt}]({image_src})", 1)
        nodes.extend(split_nodes_image([TextNode(parts[0], TextType.TEXT)]))
        nodes.append(TextNode(image_alt, TextType.IMAGE, image_src))
        nodes.extend(split_nodes_image([TextNode(parts[1], TextType.TEXT)]))

    return nodes


def split_nodes_link(old_nodes):
    nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT and len(node.text) > 0:
            nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if len(links) == 0:
            if len(node.text) > 0:
                nodes.append(node)
            continue

        link = links[0]
        link_text, link_url = link
        parts = text.split(f"[{link_text}]({link_url})", 1)
        nodes.extend(split_nodes_link([TextNode(parts[0], TextType.TEXT)]))
        nodes.append(TextNode(link_text, TextType.LINK, link_url))
        nodes.extend(split_nodes_link([TextNode(parts[1], TextType.TEXT)]))

    return nodes


def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.TEXT)

    bold_processed = split_nodes_delimiter([initial_node], "**", TextType.BOLD)
    italic_processed = split_nodes_delimiter(bold_processed, "*", TextType.ITALIC)
    code_processed = split_nodes_delimiter(italic_processed, "`", TextType.CODE)
    links_processed = split_nodes_link(code_processed)
    images_processed = split_nodes_image(links_processed)

    return images_processed
