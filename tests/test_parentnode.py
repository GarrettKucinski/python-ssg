import unittest
from src.htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        test_string = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), test_string)

    def test_nested_parents(self):
        test_string = "<p><div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        node = ParentNode(
            "p",
            [
                ParentNode("div", [
                  LeafNode("b", "Bold text"),
                  LeafNode(None, "Normal text"),
                  LeafNode("i", "italic text"),
                  LeafNode(None, "Normal text"),
                ]),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), test_string)

    def test_multiple_nested_parents(self):
        test_string = "<section><div><b>Bold text</b>Normal text<section><div><p>I'm super nested<a href=\"https://scriptarcade.dev\">anchor with props</a></p></div><nav>I'm a nav item</nav><p>I'm a nested sibling</p></section><i>italic text</i>Normal text</div><b>Bold text</b>Normal text<i>italic text</i>Normal text</section>"

        node = ParentNode(
            "section",
            [
                ParentNode("div", [
                  LeafNode("b", "Bold text"),
                  LeafNode(None, "Normal text"),
                  ParentNode("section", [
                    ParentNode("div", [
                        ParentNode("p", [
                            LeafNode(None, "I'm super nested"),
                            LeafNode("a", "anchor with props", { "href": "https://scriptarcade.dev" }),
                        ]),
                    ]),
                    LeafNode('nav', "I'm a nav item"),
                    LeafNode("p", "I'm a nested sibling")
                  ]),
                  LeafNode("i", "italic text"),
                  LeafNode(None, "Normal text"),
                ]),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), test_string)

if __name__ == "__main__":
    unittest.main()
