from block_markdown import markdown_to_htmlnode
import os
from pathlib import Path

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:]
    raise ValueError('no h1 header found. all pages need h1 header')


def generate_page(from_path, template_path, to_path):
    print(f'Generating page from {from_path} to {to_path} using {template_path}')
    file = open(from_path,'r')
    from_content = file.read()
    file.close()
    file = open(template_path,'r')
    template_content = file.read()
    file.close()
    from_html = markdown_to_htmlnode(from_content).to_html()
    title = extract_title(from_content)
    template_content = template_content.replace('{{ Title }}',title)
    template_content = template_content.replace('{{ Content }}',from_html)

    dest_dir_path = os.path.dirname(to_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path,exist_ok=True)
    file = open(to_path,'w')
    file.write(template_content)
    #file.close()
    
def generate_pages_recursive(content,template_path,dest_path):
    for filename in os.listdir(content):
        from_path = os.path.join(content,filename)
        to_path = os.path.join(dest_path,filename)
        if os.path.isfile(from_path):
            to_path = Path(to_path).with_suffix('.html')
            generate_page(from_path,template_path,to_path)
        else:
            generate_pages_recursive(from_path,template_path,to_path)