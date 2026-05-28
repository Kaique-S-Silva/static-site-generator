from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self) -> str:
        return f"TextNode(text='{self.text}', text_type={self.text_type}, url='{self.url}')"
    

def text_node_to_html_node(textnode: TextNode) -> LeafNode:
    match textnode.text_type:
        case TextType.TEXT:
            return LeafNode(None, textnode.text) 
        case TextType.BOLD:
            return LeafNode(tag="b", value=textnode.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=textnode.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=textnode.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=textnode.text, props={"href": textnode.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": textnode.url, "alt": textnode.text})
        case _:
            raise Exception("Text type invalid")








    
