class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('to_html method not implemented')
    
    def props_to_html(self):
        result = ""
        if self.props == None:
            return result
        for id,string in self.props.items():
            result += f' {id}="{string}"'
        return result

    def __repr__(self):
        return f'tag:{self.tag}\nvalue:{self.value}\nchildren:\
              {self.children}\nprops:{self.props}'

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError('all leaf nodes require a value')
        elif self.tag is None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('there should be a TAG but there is none')
        if self.children is None:
            raise ValueError('there are no children! ParentNode has to have a child')
        result_children = ""
        for child in self.children:
            if child == None:
                continue
            result_children += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{result_children}</{self.tag}>'

    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'