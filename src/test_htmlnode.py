import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        #node2 = HTMLNode("This is a text node", "bold")
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" target="_blank"')
        #print(node)

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(),'<p>This is a paragraph of text.</p>')

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),
                         '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
        
if __name__ == "__main__":
    unittest.main()