import pytest
from src.textnode import TextNode, TextType


def test_eq_textnode():
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    assert node == node2


def test_not_eq_textnode():
    node = TextNode("This is a bold text node", TextType.BOLD)
    node2 = TextNode("This is an italic text node", TextType.ITALIC)
    assert node != node2
