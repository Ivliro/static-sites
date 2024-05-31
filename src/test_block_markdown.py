import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, \
                            markdown_to_htmlnode

class TestBlockMarkdown(unittest.TestCase):
    def test_m2b_1(self):
        text = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        self.assertListEqual(markdown_to_blocks(text),
                             [
                                 'This is **bolded** paragraph', 
                                 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
                                 '* This is a list\n* with items'
                             ])

    def test_m2b_2(self):
            text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item"""
            self.assertListEqual(markdown_to_blocks(text),
                                [
                                    '# This is a heading', 
                                    'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                                    '* This is a list item\n* This is another list item'
                                ])

    def test_block_to_block_types(self):
         block = '# heading'
         self.assertEqual(block_to_block_type(block),'heading')
         block = '```\ncode\n```'
         self.assertEqual(block_to_block_type(block),'code')
         block = '>This is\n>a quote.'
         self.assertEqual(block_to_block_type(block),'quote')
         block = '* list item 1\n- list item 2'
         self.assertEqual(block_to_block_type(block),'unordered_list')
         block = '1. list item 1\n2. list item 2'
         self.assertEqual(block_to_block_type(block),'ordered_list')
         block = 'paragraph'
         self.assertEqual(block_to_block_type(block),'paragraph')

    def test_paragraphs(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
        node = markdown_to_htmlnode(markdown).to_html()
        self.assertEqual(node,
                         '<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>')
        
    def test_lists(self):
        markdown = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
        node = markdown_to_htmlnode(markdown).to_html()
        self.assertEqual(node,
                         '<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>')

    def test_headings(self):
        markdown = """
# this is an h1

this is paragraph text

## this is an h2
"""
        node = markdown_to_htmlnode(markdown).to_html()
        self.assertEqual(node,
                         '<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>') 

    def test_blockquote(self):
        markdown = """
> This is a
> blockquote block

this is paragraph text

"""
        node = markdown_to_htmlnode(markdown).to_html()
        self.assertEqual(node,
                         '<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>')


if __name__ == "__main__":
    unittest.main()