import unittest

from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        test_string = " href=\"https://scriptarcade.dev\" name=\"ScriptArcade\""
        node = HtmlNode(props={"href": "https://scriptarcade.dev", "name": "ScriptArcade"})

        self.assertEqual(node.props_to_html(), test_string)


if __name__ == "__main__":
    unittest.main()
