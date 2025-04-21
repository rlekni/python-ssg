import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("content", TextType.BOLD)
        node2 = TextNode("content", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_url_is_defaulted_to_none(self):
        node = TextNode("content", TextType.LINK)
        self.assertEqual(node.url, None)

    def test_repr(self):
        node = TextNode("content", TextType.NORMAL)
        result = f"{node}"
        expected = "TextNode(content, normal, None)"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
