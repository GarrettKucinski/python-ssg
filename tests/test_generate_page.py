
import unittest

from src.generate_page import extract_page_title

class TestGeneratePage(unittest.TestCase):
  def test_extract_page_title(self):
    markdown = """
    # This is the page title

    > a block quote
    > that has more than one line in it
    > an goes on a little further

    ## a level two header

    a few paragraphs about not much at all, just some text to fill out the
    document so that I can test that my function works properly

    ```
    a code block
    ```
"""

    test_title = "This is the page title"
    title = extract_page_title(markdown)

    self.assertEqual(test_title.lstrip("# "), title)
    self.assertRaises(ValueError, extract_page_title)
