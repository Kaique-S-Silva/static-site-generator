from enum import Enum

class TextType(Enum):
    AIR_BENDER = 1
    WATER_BENDER = 2
    EARTH_BENDER = 3
    FIRE_BENDER = 4

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