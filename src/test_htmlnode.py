import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

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

    def test_to_html_parent_no_tag(self):
        node = ParentNode(None, [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children(self):
        node = ParentNode('div', [LeafNode('span', 'child')])
        self.assertEqual(node.to_html(),
                         '<div><span>child</span></div>')

    def test_to_html_with_grandchildren(self):
        node = ParentNode('div',
                          [ParentNode('span',[LeafNode('b','grandchildren')])])
        self.assertEqual(node.to_html(),
                         '<div><span><b>grandchildren</b></span></div>')

    def test_to_html_many_childs_priklad(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),
                         '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    #toto bolo tiez v rieseni/priklade
    def test_headings(self):
        node = ParentNode('h2',
                          [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                        ],
        )
        self.assertEqual(node.to_html(),
                         '<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>')


if __name__ == "__main__":
    unittest.main()