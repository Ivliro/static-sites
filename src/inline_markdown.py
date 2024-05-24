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
        if node.text_type != 'text':
            new_nodes.append(node)
            continue
        nejaky_text = node.text
        extracted_images = extract_markdown_images(node.text)
        if len(extracted_images) == 0:
            new_nodes.append(node)
            continue
        for i, image in enumerate(extracted_images):
            #split_text1 = node.text.split(f'![{image[0]}]({image[1]})',2)
            #### MOJE RIESENIE NEDORIESENE ####
            # split_text = re.split(r'[!)]',node.text)
            # #print(i)
            # print(f'split text: {split_text}')
            # if split_text[i*2] != "":
            #     new_nodes.append(TextNode(split_text[i*2],'text'))
            # new_nodes.append(TextNode(image[0],'image',image[1]))
            # if split_text[(i+1)*2] == "":
            #     continue
            # if split_text[(i+1)*2] != new_nodes[-2].text:
            #     pass
            #     new_nodes.append(TextNode(split_text[(i+1)*2],'text'))
        #print(new_nodes)
            sections = nejaky_text.split(f'![{image[0]}]({image[1]})',1)
            if len(sections) != 2:
                raise ValueError('Invalid markdow, image section not closed')
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],'text'))
            new_nodes.append(TextNode(image[0],'image',image[1]))
            nejaky_text = sections[1]
        if nejaky_text != "":
            new_nodes.append(TextNode(nejaky_text,'text'))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            new_nodes.append(node)
            continue
        if node.text_type != 'text':
            new_nodes.append(node)
            continue
        extracted_links = extract_markdown_links(node.text)
        #print(extracted_links)
        if len(extracted_links) == 0:
            new_nodes.append(node)
            continue
        for i, link in enumerate(extracted_links):
            split_text = re.split(r'[\[\)]',node.text)
            #print(['inside split_nodes_link'] + split_text)
            new_nodes.append(TextNode(split_text[i*2],'text'))
            new_nodes.append(TextNode(link[0],'link',link[1]))
            if i == len(extracted_links)-1 and len(split_text) % 2 == 1:
                if split_text[(i+1)*2] == "":
                    continue
                new_nodes.append(TextNode(split_text[(i+1)*2],'text'))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, 'text')]
    nodes = split_nodes_delimiter(nodes,'**','bold')
    nodes = split_nodes_delimiter(nodes,"*",'italic')
    nodes = split_nodes_delimiter(nodes,'`','code')
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

node = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
new_nodes = text_to_textnodes(node)
#print(new_nodes)

node = TextNode(
           "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            'text',
)
print(split_nodes_link([node]))