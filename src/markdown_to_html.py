from .htmlnode import ParentNode, LeafNode
from .block_markdown import markdown_to_blocks, block_to_block_type, BlockTypes
from .inline_markdown import text_to_text_nodes
from .textnode import text_node_to_html_node 

def parse_heading_block(block):
  parsed_headings = list()

  for heading in block.split("\n"):
    header_arr = heading.split(" ")
    parsed_header_text = text_to_text_nodes(" ".join(header_arr[1:]))
    content = list(map(text_node_to_html_node, parsed_header_text))
    parsed_headings.append(ParentNode(f"h{len(header_arr[0])}", children=content))

  return parsed_headings

def parse_quote_block(block):
  quote_text = "".join(map(lambda s: s.strip("> "), block.split("\n")))
  return [LeafNode("blockquote", value=quote_text)]

def parse_code_block(block):
  children = [LeafNode("pre", value=block.strip("```"))]
  return [ParentNode("code", children=children)]

def parse_paragraph_block(block):
  text_nodes = text_to_text_nodes(block)
  inline_elements = list(map(text_node_to_html_node, text_nodes))

  return [ParentNode("p", children=inline_elements)]

def parse_unordered_list_block(block):
  create_list_item = lambda item: LeafNode("li", value=item.strip("*- "))
  list_items = list(map(create_list_item, block.split("\n")))

  return [ParentNode("ul", children=list_items)]

def parse_ordered_list_block(block):
  list_items = list()

  for block in sorted(block.split("\n")):
    _, text = block.split(". ", 1)
    list_items.append(LeafNode("li", value=text))

  return [ParentNode("ol", children=list_items)]

block_type_parser_map = dict()

block_type_parser_map[BlockTypes.HEADING] = parse_heading_block
block_type_parser_map[BlockTypes.CODE] = parse_code_block
block_type_parser_map[BlockTypes.ORDERED_LIST] = parse_ordered_list_block
block_type_parser_map[BlockTypes.UNORDERED_LIST] = parse_unordered_list_block
block_type_parser_map[BlockTypes.QUOTE] = parse_quote_block
block_type_parser_map[BlockTypes.PARAGRAPH] = parse_paragraph_block

def markdown_to_html(markdown):
  # convert markdown into blocks
  blocks = markdown_to_blocks(markdown)
  block_types = list(map(block_to_block_type, blocks))
  blocks_with_types = list(zip(block_types, blocks))

  root_children = list()

  for type, block in blocks_with_types:
    parser = block_type_parser_map[type]
    root_children.extend(parser(block))

  return ParentNode(tag="div", children=root_children)
