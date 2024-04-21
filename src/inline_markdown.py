import re
from textnode import TextNode, TextTypes

def extract_markdown_images(text):
  return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
  return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = list()

  for node in old_nodes:
    text = node.text.split(delimiter)

    if node.text_type != TextTypes.TEXT:
      new_nodes.append(node)
      continue
 
    if len(text) % 2 == 0:
      raise ValueError("Invalid markdown, formatted section not closed")

    for i, text in enumerate(text):
      if text == "":
        continue

      if i % 2 != 0:
        new_nodes.append(TextNode(text, text_type))
      elif i % 2 == 0:
        new_nodes.append(TextNode(text, TextTypes.TEXT))

  return new_nodes

def split_nodes_image(old_nodes):
  new_nodes = []

  for node in old_nodes:
    if node.text_type != TextTypes.TEXT:
      new_nodes.append(node)
      continue

    original_text = node.text
    images = extract_markdown_images(original_text)

    if len(images) == 0:
      new_nodes.append(node)
      continue

    for i in images:
      name, url = i
      image = f"![{name}]({url})"
      p = original_text.split(image, 1)

      if len(p) != 2:
        raise ValueError("Improperly closed markdown")

      original_text = p[1]

      if p[0] != "":
        new_nodes.append(TextNode(p[0], TextTypes.TEXT))

      new_nodes.append(TextNode(name, url=url, text_type=TextTypes.IMAGE))
    
    if original_text != "":
      new_nodes.append(TextNode(original_text, TextTypes.TEXT))

  return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = []

  for node in old_nodes:
    if node.text_type != TextTypes.TEXT:
      new_nodes.append(node)
      continue

    original_text = node.text
    links = extract_markdown_links(original_text)

    if len(links) == 0:
      new_nodes.append(node)
      continue 

    for l in links:
      name, url = l
      link= f"[{name}]({url})"
      p = original_text.split(link, 1)

      if len(p) != 2:
        raise ValueError("Improperly closed markdown")

      original_text = p[1]

      if p[0] != "":
        new_nodes.append(TextNode(p[0], TextTypes.TEXT))

      new_nodes.append(TextNode(name, url=url, text_type=TextTypes.LINK))

    if original_text != "":
      new_nodes.append(TextNode(original_text, TextTypes.TEXT))

  return new_nodes

def text_to_text_nodes(text):
  nodes = [TextNode(text, text_type=TextTypes.TEXT)]

  nodes = split_nodes_delimiter(nodes, "`", TextTypes.CODE)
  nodes = split_nodes_delimiter(nodes, "**", TextTypes.BOLD)
  nodes = split_nodes_delimiter(nodes, "*", TextTypes.ITALIC)
  nodes = split_nodes_image(nodes)
  nodes = split_nodes_link(nodes)

  return nodes
