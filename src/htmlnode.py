class HtmlNode():
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError()

  def props_to_html(self):
    return "".join(list(map(lambda t: f" {t[0]}=\"{t[1]}\"", self.props.items())))

  def __repr__(self):
    return f"HtmlNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HtmlNode):
  def __init__(self, tag=None, value=None, props={}):
    super().__init__(tag=tag, value=value, props=props)

  def to_html(self):
    if self.tag:
      return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    else:
      return self.value

  def __repr__(self):
    return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"


class ParentNode(HtmlNode):
  def __init__(self, tag=None, children=None, props=None):
    super().__init__(tag=tag, children=children, props=props)

  def to_html(self):
    if not self.tag:
      raise ValueError("Parent elements must have a tag")
    if not self.children:
      raise ValueError("Parent elements must contain children")

    def parse_child_nodes(children):
      if not len(children):
        return ""

      return children[0].to_html() + parse_child_nodes(children[1:])

    return f"<{self.tag}>{parse_child_nodes(self.children)}</{self.tag}>"

  def __repr__(self):
    return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
