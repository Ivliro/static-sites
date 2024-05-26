import re

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
    

print(block_to_block_type('###### Heading'))
print(block_to_block_type('```\ncode\n```'))
print(block_to_block_type('>This is\n>a quote.'))
print(block_to_block_type('* list item 1\n- list item 2'))
print(block_to_block_type('1. list item 1\n2. list item 2'))
print(block_to_block_type('just a paragraph'))