from htmlnode import LeafNode

class TextNode:
    def __init__(self, text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,another):
        if self.text == another.text and self.text_type == another.text_type \
            and self.url == another.url:
            return True
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
    def text_node_to_html_node(text_node):
        if text_node.text_type == 'text':
            LeafNode(None,text_node.text)
        elif text_node.text.type == 'bold':
            LeafNode('b',text_node.text)
        elif text_node.text.type == 'italic':
            LeafNode('i',text_node.text)
        elif text_node.text.type == 'code':
            LeafNode('code',text_node.text)
        elif text_node.text.type == 'link':
            LeafNode('a',text_node.text,{'href':text_node.url})
        elif text_node.text.type == 'image':
            LeafNode('img',None,{'src':text_node.url,'alt':text_node.text})        
        else:
            raise ValueError(f'wront text type: {text_node.text_type}')