import re
from enum import Enum

class BlockTypes(Enum):
  CODE = "code"
  PARAGRAPH = "paragraph"
  HEADING = "heading"
  QUOTE = "quote"
  UNORDERED_LIST = "unordered_list"
  ORDERED_LIST = "ordered_list"

def markdown_to_blocks(text):
  blocks = filter(lambda s: s != "", text.split("\n\n"))
  cleaned_blocks = filter(lambda s: s != "", map(lambda s: s.strip(), blocks))

  return list(cleaned_blocks)

def block_to_block_type(block):
  cleaned_block = block.strip()

  lines = cleaned_block.split("\n")

  if cleaned_block.strip().startswith("```") \
    and cleaned_block.strip().endswith("```"):
      return BlockTypes.CODE

  if (
    cleaned_block.startswith("# ")
    or cleaned_block.startswith("## ")
    or cleaned_block.startswith("### ")
    or cleaned_block.startswith("#### ")
    or cleaned_block.startswith("##### ")
    or cleaned_block.startswith("###### ")
  ):
    return BlockTypes.HEADING

  if cleaned_block.startswith(("* ", "- ")):
    for line in lines:
      if not line.startswith(("* ", "- ")):
       continue 

    return BlockTypes.UNORDERED_LIST

  if cleaned_block.startswith("1. "):
    for i, line in enumerate(lines[1:]):
      if not line.startswith(f"{i+2}. "):
       continue 

    return BlockTypes.ORDERED_LIST

  if cleaned_block.startswith(">"):
    for line in lines:
      if not line.startswith(">"):
       continue 

    return BlockTypes.QUOTE

  return BlockTypes.PARAGRAPH
