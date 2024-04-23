import unittest

from src.textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")

        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")

        self.assertNotEqual(node, node2)

    def test_string_rep(self):
      string = "TextNode(Don't panic!, italic, https://thanksforallthefish.com)"
      node = TextNode("Don't panic!", "italic", "https://thanksforallthefish.com")

      self.assertEqual(node.__repr__(), string)


if __name__ == "__main__":
    unittest.main()
