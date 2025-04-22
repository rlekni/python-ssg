import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("href", "test.com", None, props)
        result = f"{node}"
        expected = f'HTMLNode(href, test.com, False,  href="https://www.google.com" target="_blank")'
        self.assertEqual(result, expected)

    def test_no_props(self):
        node = HTMLNode("href", "test.com", None, None)
        result = f"{node}"
        expected = f"HTMLNode(href, test.com, False, )"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
