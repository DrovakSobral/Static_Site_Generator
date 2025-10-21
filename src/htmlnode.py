class HTMLNode():
    def __init__(self, tag:str = None, value:str = None, children:list["HTMLNode"] = None, props:dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("This method is only implemented in it's subclasses")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f" {prop}=\"{self.props[prop]}\""
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag:str, value:str, props:dict[str, str] = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise TypeError("This leaf node has no value!")
        elif self.tag is None:
            return self.value
        elif self.tag and self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {list(self.props.keys())[0]}=\"{list(self.props.values())[0]}\">{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:list[LeafNode], props:dict[str, str] = None):
        if not tag:
            raise TypeError("The parent node is missing a tag")
        if not children:
            raise TypeError("The parent node is missing children")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
