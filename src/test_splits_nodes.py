import unittest
from splits_nodes import *

class TestSplitNodesDelimeter(unittest.TestCase):
    def test_bold_delimeter(self):
        node = TextNode("This is a text with a **bold** word", TextType.TEXT)
        new_node = split_nodes_delimeter([node],"**", TextType.BOLD)
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_node, expected)

    def test_italic_delimeter(self):
        node = TextNode("This is a text with a *italic* word", TextType.TEXT)
        new_node = split_nodes_delimeter([node],"*", TextType.ITALIC)
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_node, expected)

    def test_error_message(self):
        node = TextNode("This is a text with a *error", TextType.TEXT)
        
        with self.assertRaises(Exception) as cm:
            split_nodes_delimeter([node], "*", TextType.BOLD)

        self.assertEqual(str(cm.exception), "Invalid markdown syntax")

    def test_code_block(self):
        node = TextNode("This is a `code` block", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" block", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_delimeters(self):
        node = TextNode("Este *bold* e este *bold*", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "*", TextType.BOLD)
        self.assertEqual(len(new_nodes), 4)