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