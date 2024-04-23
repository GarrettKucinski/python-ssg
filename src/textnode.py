from enum import Enum
from .htmlnode import LeafNode

class TextTypes(Enum):
  TEXT = "text" 
  BOLD = "bold" 
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"

class TextNode():
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other):
    return self.text == other.text and self.text_type == other.text_type and self.url == other.url

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
  if text_node.text_type == TextTypes.TEXT:
    return LeafNode(None, value=text_node.text)
  elif text_node.text_type == TextTypes.BOLD:
    return LeafNode("b", value=text_node.text)
  elif text_node.text_type == TextTypes.CODE:
    return LeafNode("code", value=text_node.text)
  elif text_node.text_type == TextTypes.ITALIC:
    return LeafNode("i", value=text_node.text)
  elif text_node.text_type == TextTypes.LINK:
    return LeafNode("a", value=text_node.text, props={ "href": text_node.url })
  elif text_node.text_type == TextTypes.IMAGE:
    return LeafNode("img", value="", props={ "src": text_node.url, "alt": text_node.text })

  raise ValueError("Invalid text node type")
