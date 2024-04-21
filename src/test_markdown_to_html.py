import unittest

from markdown_to_html import markdown_to_html

class TestMarkdownToHtml(unittest.TestCase):

  def test_markdown_to_html(self):
    test_string = "<div><h1>Hello</h1><h2>Level Two</h2><h4>Level Four</h4><p>This is some markdown text with <i>italic</i> in it\nLet's throw in some <b>bold</b> as well</p><p>Then an unorderd list for good measure</p><ul><li>item one</li><li>item two</li><li>item three</li><li>item four</li></ul></div>"

    html = markdown_to_html("""
# Hello
## Level Two
#### Level Four

This is some markdown text with *italic* in it
Let's throw in some **bold** as well

Then an unorderd list for good measure

* item one
* item two
* item three
* item four
    """)

    self.assertEqual(test_string, html.to_html())
