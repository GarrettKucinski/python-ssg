import unittest

from src.htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        test_string = "<p id=\"maple\">Shakin like a leaf on a tree</p>"
        node = LeafNode(tag="p", value="Shakin like a leaf on a tree", props={"id": "maple"})

        self.assertEqual(node.to_html(), test_string)


if __name__ == "__main__":
    unittest.main()
