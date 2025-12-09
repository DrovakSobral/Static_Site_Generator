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

    def props_to_html(self) -> str:
        try:
            result = ""
            for prop in self.props:
                result += f' {prop}="{self.props[prop]}"'
            return result
        except TypeError:
            return ""

    def __repr__(self):
        return f"HTMLNode(TAG = {self.tag}, VALUE = {self.value}, CHILDREN = {self.children}, PROPS = {self.props})"


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        value: str,
        props: dict[str, str] = None,
    ) -> LeafNode:
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("The LeafNode has no value!")
        if self.tag is None:
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"