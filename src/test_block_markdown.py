import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockTypes

class TestBMarkdownNode(unittest.TestCase):

  def test_markdown_to_blocks(self):
    text = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
    test_output = [
      "This is **bolded** paragraph",
      "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
      "* This is a list\n* with items"
    ]

    blocks = markdown_to_blocks(text)

    self.assertEqual(blocks, test_output)

  def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


  def test_block_to_block_type(self):
    quote = """
> hello there
> this is a quote
> how are you
"""

    unordered = """
* item one
* item one
* item one
* item one
"""

    ordered = """
1. first
2. second
3. third
4. fourth
"""
    ordered_wrong_order = """
1. first
5. fifth
2. second
3. third
4. fourth
"""

    heading_one = "# heading 1"
    heading_three = "### heading 3"

    code = """
```
this is some code I wrote today
```
"""
    paragraph = "This is just some ordinary text."

    self.assertEqual(BlockTypes.QUOTE, block_to_block_type(quote))
    self.assertEqual(BlockTypes.UNORDERED_LIST, block_to_block_type(unordered))
    self.assertEqual(BlockTypes.ORDERED_LIST, block_to_block_type(ordered))
    self.assertEqual(BlockTypes.HEADING, block_to_block_type(heading_one))
    self.assertEqual(BlockTypes.HEADING, block_to_block_type(heading_three))
    self.assertEqual(BlockTypes.CODE, block_to_block_type(code))
    self.assertEqual(BlockTypes.PARAGRAPH, block_to_block_type(paragraph))
    self.assertNotEqual(BlockTypes.ORDERED_LIST, ordered_wrong_order)
