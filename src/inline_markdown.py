from textnode import TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if text_type not in ['text','bold','italic','code','link','image']:
        raise ValueError(f'text_type unknown: {text_type}')
    new_nodes = []
    #result = []
    for node in old_nodes:
        if node.text_type != 'text':
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception(f'invalid markdown syntax, unmatched delimiter: {delimiter}')
        for i, string in enumerate(split_text):
            if string == "":
                continue
            if i % 2 == 1:
                new_nodes.append(TextNode(string,text_type))
                continue
            new_nodes.append(TextNode(string,node.text_type))
        #result.extend(new_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern,text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern,text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        extracted_images = extract_markdown_images(node.text)
        for i, image in enumerate(extracted_images):
            #split_text1 = node.text.split(f'![{image[0]}]({image[1]})',2)
            split_text = re.split(r'[!)]',node.text)
            #print(split_text)
            if split_text[i*2] != "":
                new_nodes.append(TextNode(split_text[i*2],'text'))
            new_nodes.append(TextNode(image[0],'image',image[1]))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        extracted_links = extract_markdown_links(node.text)
        for i, link in enumerate(extracted_links):
            split_text = re.split(r'[\[)]',node.text)
            new_nodes.append(TextNode(split_text[i*2],'text'))
            new_nodes.append(TextNode(link[0],'link',link[1]))
            if i == len(extracted_links)-1 and len(split_text) % 2 == 1:
                new_nodes.append(TextNode(split_text[(i+1)*2],'text'))
    return new_nodes
