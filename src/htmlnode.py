class HTMLnode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method must be implemented by subclasses")
    
    def props_to_html(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items()) if self.props else ''
    
    def __repr__(self) -> str:
        return f"HTMLnode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"