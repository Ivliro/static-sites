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
