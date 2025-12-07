class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list[HTMLNode] = None,
        props: dict[str, str] = None,
    ) -> HTMLNode:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        try:
            result = ""
            for key in self.props:
                result += f' {key}="{self.props[key]}"'
            return result
        except TypeError:
            return ""

    def __repr__(self):
        return f"HTMLNode(TAG = {self.tag}, VALUE = {self.value}, CHILDREN = {self.children}, PROPS = {self.props})"
