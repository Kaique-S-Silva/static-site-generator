import unittest

from htmlnode import HTMLnode, LeafNode, ParentNode

class TestHTMLnode(unittest.TestCase):
    def test_init(self):
        node = HTMLnode(tag='div', value='Hello', children=[], props={'class': 'my-class'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello')
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {'class': 'my-class'})

    def test_to_html_not_implemented(self):
        node = HTMLnode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_props_to_html(self):
        node = HTMLnode(props={'class': 'my-class', 'id': 'my-id'})
        self.assertEqual(node.props_to_html(), ' class="my-class" id="my-id"')

    def test_repr(self):
        node = HTMLnode(tag='div', value='Hello', children=[], props={'class': 'my-class'})
        expected_repr = "HTMLnode(tag='div', value='Hello', children=[], props={'class': 'my-class'})"
        self.assertEqual(repr(node), expected_repr) 

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode(tag='p', value="Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_to_html(self):
        node = LeafNode(tag='a', value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>') 

    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_repr(self):
        node = LeafNode(tag='p', value='Hello, World!')
        expected_repr = "LeafNode(tag='p', value='Hello, World!', props=None)"
        self.assertEqual(repr(node), expected_repr)        

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
if __name__ == '__main__':
    unittest.main()