from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node should have a value")

        if not self.tag:
            return self.value

        html = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return html
