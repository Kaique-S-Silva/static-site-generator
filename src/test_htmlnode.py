import unittest

from htmlnode import HTMLnode

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
        self.assertEqual(node.props_to_html(), 'class="my-class" id="my-id"')

    def test_repr(self):
        node = HTMLnode(tag='div', value='Hello', children=[], props={'class': 'my-class'})
        expected_repr = "HTMLnode(tag='div', value='Hello', children=[], props={'class': 'my-class'})"
        self.assertEqual(repr(node), expected_repr) 

    
if __name__ == '__main__':
    unittest.main()