import re
from htmlnode import ParentNode,LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_blocks(document):
    blocks = []
    doc_lines = document.split('\n')
    block = ""
    for line in doc_lines:
        if line == "":
            if block == "":
                continue
            blocks.append(block.strip())
            block = ""
            continue
        block += line + '\n'
        if line == doc_lines[-1]:
            blocks.append(block.strip())
    return blocks

def block_to_block_type(block):
    if re.match(r'^#{1,6}\s.*',block):
        return 'heading'
    elif re.match(r'(?m)```\s*.*\s*```',block):
        return 'code'
    elif re.match(r'(?m)^>.*$',block):
        return 'quote'
    elif re.match(r'(?m)^[*-]\s.*',block):
        return 'unordered_list'
    elif re.match(r'(?m)^[0-9]\.\s.*',block):
        for i,sent in enumerate(block.split('\n')):
            if int(sent[0]) == i+1:
                continue
            else:
                return 'paragraph'
        return 'ordered_list'
    else:
        return 'paragraph'
    
def markdown_to_htmlnode(markdown):
    # split markdown document into blocks
    html_document = ParentNode('div',[])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        # determine the type of the block
        block_type = block_to_block_type(block)
        if block_type == 'quote':
            html_document.children.append(quote_to_html(block))
        if block_type == 'unordered_list':
            html_document.children.append(ul_to_html(block))
        if block_type == 'ordered_list':
            html_document.children.append(ol_to_html(block))
        if block_type == 'code':
            html_document.children.append(code_to_html(block))
        if block_type == 'heading':
            html_document.children.append(heading_to_html(block))
        if block_type == 'paragraph':
            html_document.children.append(paragragh_to_html(block))
    return html_document

# tuto funkciu som si pozrel z riesenia
def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children

def quote_to_html(block):
    quote = ""
    for line in block.split('\n'):
        quote += line[2:] + ' '
    children = text_to_children(quote.strip())
    return ParentNode('blockquote',children)

def ul_to_html(block):
    items = []
    for line in block.split('\n'):
        children = text_to_children(line[2:])
        items.append(ParentNode('li',children))
    return ParentNode('ul',items)

def ol_to_html(block):
    items = []
    for line in block.split('\n'):
        children = text_to_children(line[3:])
        items.append(ParentNode('li',children))  
    return ParentNode('ol',items)

def code_to_html(block):
    # ak nezacina alebo nekonci s ukazovatelom na code-block
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError('invalid code block')
    text = block[4:-3]
    children = text_to_children(text)
    return ParentNode('pre',[ParentNode('code',children)])

def heading_to_html(block):
    text = re.search(r'\s.*',block)
    children = text_to_children(text.group().strip())
    if block.startswith('# '):
        return ParentNode('h1',children)
    elif block.startswith('## '):
        return ParentNode('h2',children)
    elif block.startswith('### '):
        return ParentNode('h3',children)
    elif block.startswith('#### '):
        return ParentNode('h4',children)
    elif block.startswith('##### '):
        return ParentNode('h5',children)
    elif block.startswith('###### '):
        return ParentNode('h6',children)

def paragragh_to_html(block):
    paragraph = ""
    for line in block.split('\n'):
        paragraph += line + ' '
    children = text_to_children(paragraph.strip())
    return ParentNode('p',children)


markdown = """
> This is a
> blockquote block
> with *italic words*

this is paragraph text

- This is a list
- with items
- and *more* items

# this is an h1

this is paragraph text

## this is an h2

1. This is an `ordered` list
2. with items
3. and more items

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here
"""
#print(markdown_to_htmlnode(markdown).to_html())