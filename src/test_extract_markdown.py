import unittest
from extract_markdown import *


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_empty_text(self):
        matches = extract_markdown_images("")
        self.assertListEqual([], matches)
    
    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), This is second text with an ![image](https://i.imgur.com/zjjcJKZ.png), This is third text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),("image", "https://i.imgur.com/zjjcJKZ.png"),("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_empty_text(self):
        matches = extract_markdown_links("")
        self.assertListEqual([], matches)

    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://www.google.com/), This is second text with an [link](https://www.google.com/), This is third text with an [link](https://www.google.com/)"
            )
        self.assertListEqual([("link", "https://www.google.com/"),("link", "https://www.google.com/"),("link", "https://www.google.com/")], matches)