import unittest
from inline_markdown import split_nodes_delimiter,extract_markdown_links, \
                        extract_markdown_images,split_nodes_image, \
                        split_nodes_link, text_to_textnodes
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
        
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            'text',
        )
        self.assertListEqual(split_nodes_image([node]),
                             [TextNode("This is text with an ", 'text', None), 
                              TextNode('image', 'image', "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), 
                              TextNode(" and another ", 'text', None), 
                              TextNode("second image", 'image', "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
                              ])
        
    def test_split_single_image(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            'text',
        )
        self.assertListEqual(split_nodes_image([node]),
                             [TextNode("image", 'image', "https://www.example.com/image.png"),])
        
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            'text',
        )
        self.assertListEqual(split_nodes_link([node]),
                             [TextNode("This is text with a ", 'text', None), 
                              TextNode('link', 'link', "https://boot.dev"), 
                              TextNode(" and ", 'text', None), 
                              TextNode("another link", 'link', "https://blog.boot.dev"),
                              TextNode(" with text that follows", 'text'),
                            ])

    def test_text_to_textnode(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(nodes,
                [
                    TextNode("This is ", 'text'),
                    TextNode("text", 'bold'),
                    TextNode(" with an ", 'text'),
                    TextNode("italic", 'italic'),
                    TextNode(" word and a ", 'text'),
                    TextNode("code block", 'code'),
                    TextNode(" and an ", 'text'),
                    TextNode("image", 'image', "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and a ", 'text'),
                    TextNode("link", 'link', "https://boot.dev"),
                ])


if __name__ == "__main__":
    unittest.main()