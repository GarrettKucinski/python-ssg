from htmlnode import ParentNode, LeafNode
from block_markdown import markdown_to_blocks, block_to_block_type, BlockTypes
from inline_markdown import text_to_text_nodes
from textnode import text_node_to_html_node, TextTypes

def markdown_to_html(markdown):

  root_children = list()

  # convert markdown into blocks
  blocks = markdown_to_blocks(markdown)
  block_types = list(map(block_to_block_type, blocks))
  blocks_with_types = list(zip(block_types, blocks))

  for type, block in blocks_with_types:
    if type == BlockTypes.HEADING:
      headings = block.split("\n")
      for heading in headings:
        header_arr = heading.split(" ")
        root_children.append(LeafNode(f"h{len(header_arr[0])}", value=" ".join(header_arr[1:])))

    if type == BlockTypes.QUOTE:
      root_children.append(LeafNode("blockquote", value="".join(map(lambda s: s.strip("> "), block.split("\n")))))

    if type == BlockTypes.CODE:
      root_children.append(ParentNode("code", children=[LeafNode("pre", value=block.strip("```"))]))

    if type == BlockTypes.PARAGRAPH:
      inline_elements = list(map(text_node_to_html_node, text_to_text_nodes(block)))
      root_children.append(ParentNode("p", children=inline_elements))

    if type == BlockTypes.UNORDERED_LIST:
      list_items = list(map(lambda item: LeafNode("li", value=item.strip("* ")), block.split("\n")))

      root_children.append(ParentNode("ul", children=list_items))

    if type == BlockTypes.ORDERED_LIST:
      list_items = list()

      for block in sorted(block.split("\n")):
        _, text = block.split(" ")
        list_items.append(LeafNode("li", value=text))

      root_children.append(ParentNode("ol", children=list_items))

  return ParentNode(tag="div", children=root_children)
