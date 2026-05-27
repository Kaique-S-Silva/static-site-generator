class HTMLnode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method must be implemented by subclasses")
    
    def props_to_html(self):
        if not self.props:
            return ''
        return ' '+' '.join(f'{key}="{value}"' for key, value in self.props.items()) if self.props else ''
    
    def __repr__(self) -> str:
        return f"HTMLnode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"

class LeafNode(HTMLnode):
    def __init__(self, tag: str, value: str, children: list = None, props: dict = None):
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        if self.tag is None:
            return f"{self.value}"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"LeafNode(tag='{self.tag}', value='{self.value}', props={self.props})"
    
class ParentNode(HTMLnode):
    def __init__(self, tag: str = None, children: list = None, props: dict = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag not found")
        if not self.children:
            raise ValueError("Has no children")
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"