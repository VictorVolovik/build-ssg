from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)

        parts = node.text.split(sep=delimiter)
        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown syntax")

        new_nodes = []
        for index in range(0, len(parts)):
            if len(parts[index]) > 0:
                if index % 2 != 0:
                    new_nodes.append(TextNode(parts[index], text_type))
                else:
                    new_nodes.append(TextNode(parts[index], TextType.TEXT))
        nodes.extend(new_nodes)

    return nodes
