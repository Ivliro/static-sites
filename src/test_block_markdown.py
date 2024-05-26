import unittest
from block_markdown import markdown_to_blocks, block_to_block_type

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



if __name__ == "__main__":
    unittest.main()