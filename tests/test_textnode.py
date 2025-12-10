import pytest
from src.textnode import TextNode, TextType, textnode_to_htmlnode
from src.htmlnode import LeafNode


def test_eq_textnode():
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    assert node == node2


def test_not_eq_textnode():
    node = TextNode("This is a bold text node", TextType.BOLD)
    node2 = TextNode("This is an italic text node", TextType.ITALIC)
    assert node != node2


def test_textnode_to_htmlnode_invalid_text_type():
    node = TextNode("", None, "")
    with pytest.raises(ValueError, match="Invalid text type: None"):
        node2 = textnode_to_htmlnode(node)


def test_textnode_to_htmlnode_bold():
    node = TextNode("lorem ipsum", TextType.BOLD)
    node2 = textnode_to_htmlnode(node) 
    assert node2.tag == "b"
    assert node2.value == "lorem ipsum"


def test_textnode_to_htmlnode_link():
    node = TextNode("lorem ipsum", TextType.LINK, "https://www.boot.dev")
    node2 = textnode_to_htmlnode(node)
    assert node2.tag == "a"
    assert node2.value == "lorem ipsum"
    assert node2.props == {"href": "https://www.boot.dev"}