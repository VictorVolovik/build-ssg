from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node should have a tag")

        # FIXME: mb it's ok to have empty children list
        if self.children is None or len(self.children) == 0:
            raise ValueError("Parent node should have children")

        html = ""
        for childNode in self.children:
            html += childNode.to_html()

        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
