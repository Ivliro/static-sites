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