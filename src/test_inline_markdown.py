import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode

class TestInlineMarkdown(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", 'text')
        new_nodes = split_nodes_delimiter([node], "`", 'code')
        #node2 = TextNode("This is a text node", "bold")
        self.assertEqual(new_nodes, 
                         [
                        TextNode("This is text with a ", 'text'),
                        TextNode("code block", 'code'),
                        TextNode(" word", 'text'),
        ])

    def test_split_italic(self):
        node = TextNode("This is text with a *italic* word", 'text')
        new_nodes = split_nodes_delimiter([node], "*", 'italic')
        self.assertListEqual(new_nodes,
                             [
                                TextNode("This is text with a ", 'text'),
                                TextNode("italic", 'italic'),
                                TextNode(" word", 'text'), 
                             ]
        )

    def test_split_bold(self):
        node = TextNode("This is text with a **bolded** word", 'text')
        new_nodes = split_nodes_delimiter([node], "**", 'bold')
        self.assertListEqual(new_nodes,
                             [
                                TextNode("This is text with a ", 'text'),
                                TextNode("bolded", 'bold'),
                                TextNode(" word", 'text'), 
                             ]
        )

    def test_split_bold_double(self):
        node = TextNode("This is text with a **bolded** word and **another**", 'text')
        new_nodes = split_nodes_delimiter([node], "**", 'bold')
        self.assertListEqual(new_nodes,
                             [
                                TextNode("This is text with a ", 'text'),
                                TextNode("bolded", 'bold'),
                                TextNode(" word and ", 'text'),
                                TextNode("another",'bold'),
                             ]
        )

if __name__ == "__main__":
    unittest.main()