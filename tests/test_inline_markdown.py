import unittest

from src.textnode import TextNode, TextTypes
from src.inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    text_to_text_nodes
)

class TestInlineMarkdownNode(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"

        output = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]


        self.assertEqual(extract_markdown_images(text), output)

    def test_extract_markdown_links(self):
      text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
      output = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]


      self.assertEqual(extract_markdown_links(text), output)

    def test_split_node_delimiter(self):
        def get_test_nodes(type):
            return [
                TextNode("Node with delimiter ", TextTypes.TEXT),
                TextNode("some node that is not a text node", type),
                TextNode(" and some stuff after", TextTypes.TEXT),
            ] 

        nodes = split_nodes_delimiter([
            TextNode("Node with delimiter `some node that is not a text node` and some stuff after", TextTypes.TEXT)
        ], "`", TextTypes.CODE)
        nodes2 = split_nodes_delimiter([
            TextNode("Node with delimiter **some node that is not a text node** and some stuff after", TextTypes.TEXT)
        ], "**", TextTypes.BOLD)
        nodes3 = split_nodes_delimiter([
            TextNode("Node with delimiter *some node that is not a text node* and some stuff after", TextTypes.TEXT),
            TextNode("Another normal node", TextTypes.CODE),
        ], "*", TextTypes.ITALIC)

        self.assertEqual(get_test_nodes(TextTypes.CODE), nodes)
        self.assertEqual(get_test_nodes(TextTypes.BOLD), nodes2)
        self.assertEqual(get_test_nodes(TextTypes.ITALIC) + [TextNode("Another normal node", TextTypes.CODE)], nodes3)

    def test_split_images(self):
        output = [
            TextNode("This is text with an ", TextTypes.TEXT),
            TextNode("image", TextTypes.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", TextTypes.TEXT),
            TextNode(
                "second image", TextTypes.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]

        node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", TextTypes.TEXT)

        new_nodes = split_nodes_image([node])

        self.assertEqual(output, new_nodes)

    def test_text_to_text_nodes(self):
        new_nodes = text_to_text_nodes("This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)")

        output = [
            TextNode("This is ", TextTypes.TEXT),
            TextNode("text", TextTypes.BOLD),
            TextNode(" with an ", TextTypes.TEXT),
            TextNode("italic", TextTypes.ITALIC),
            TextNode(" word and a ", TextTypes.TEXT),
            TextNode("code block", TextTypes.CODE),
            TextNode(" and an ", TextTypes.TEXT),
            TextNode("image", TextTypes.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", TextTypes.TEXT),
            TextNode("link", TextTypes.LINK, "https://boot.dev"),
        ]


        self.assertEqual(new_nodes , output)

if __name__ == "__main__":
    unittest.main()
