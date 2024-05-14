import unittest
from inline_markdown import split_nodes_delimiter,extract_markdown_links, \
                        extract_markdown_images
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

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertListEqual(extract_markdown_links(text),
                             [("link", "https://www.example.com"), 
                              ("another", "https://www.example.com/another")])

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertListEqual(extract_markdown_images(text),
                             [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                               ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])
        



if __name__ == "__main__":
    unittest.main()