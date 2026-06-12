import unittest
from inline_markdown import *

class TestSplitNodesDelimeter(unittest.TestCase):
    def test_bold_delimeter(self):
        node = TextNode("This is a text with a **bold** word", TextType.TEXT)
        new_node = split_nodes_delimiter([node],"**", TextType.BOLD)
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_node, expected)

    def test_italic_delimeter(self):
        node = TextNode("This is a text with a *italic* word", TextType.TEXT)
        new_node = split_nodes_delimiter([node],"*", TextType.ITALIC)
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_node, expected)

    def test_error_message(self):
        node = TextNode("This is a text with a *error", TextType.TEXT)
        
        with self.assertRaises(Exception) as cm:
            split_nodes_delimiter([node], "*", TextType.BOLD)

        self.assertEqual(str(cm.exception), "Invalid markdown syntax")

    def test_code_block(self):
        node = TextNode("This is a `code` block", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" block", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_delimeters(self):
        node = TextNode("Este *bold* e este *bold*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(len(new_nodes), 4)

class TestSplitNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da) and another [second link](https://www.boot.dev/dashboard)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://www.boot.dev/dashboard"
                ),
            ],  
            new_nodes,
        )

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_empty_text(self):
        img_matches = extract_markdown_images("")
        link_matches = extract_markdown_links("")
        self.assertListEqual([], img_matches)
        self.assertListEqual([], link_matches)
        
    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), This is second text with an ![image](https://i.imgur.com/zjjcJKZ.png), This is third text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),("image", "https://i.imgur.com/zjjcJKZ.png"),("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://www.google.com/), This is second text with an [link](https://www.google.com/), This is third text with an [link](https://www.google.com/)"
            )
        self.assertListEqual([("link", "https://www.google.com/"),("link", "https://www.google.com/"),("link", "https://www.google.com/")], matches)

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_next_node(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(text_to_textnodes(text), expected)