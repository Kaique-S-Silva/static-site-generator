import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.AIR_BENDER)
        node2 = TextNode("This is a text node", TextType.AIR_BENDER)
        self.assertEqual(node1, node2)
    
    def test_neq(self):
        node1 = TextNode("This is a text node", TextType.AIR_BENDER)
        node2 = TextNode("This is a different text node", TextType.AIR_BENDER)
        self.assertNotEqual(node1, node2)
    
    def test_neq_different_type(self):
        node1 = TextNode("This is a text node", TextType.AIR_BENDER)
        node2 = TextNode("This is a text node", TextType.FIRE_BENDER)
        self.assertNotEqual(node1, node2)

    def test_urlIsNone(self):
        node1 = TextNode("This is a text node", TextType.AIR_BENDER)
        self.assertIsNone(node1.url)
        
if __name__ == '__main__':
    unittest.main()