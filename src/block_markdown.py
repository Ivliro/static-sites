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
