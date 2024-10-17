class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""

        return " " + " ".join(
            list(
                map(
                    prop_to_html,
                    self.props.items(),
                )
            )
        )

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"


def prop_to_html(prop):
    attribute, value = prop

    if len(value) == 0:
        return f"{attribute}"
    else:
        return f'{attribute}="{value}"'
