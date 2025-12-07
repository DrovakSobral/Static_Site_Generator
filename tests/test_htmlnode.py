import pytest
from src.htmlnode import HTMLNode


def test_props_to_html_none():
    node = HTMLNode()
    assert node.props_to_html() == ""


def test_props_to_html_empty():
    node = HTMLNode(props={})
    assert node.props_to_html() == ""


def test_props_to_html_multiple_pairs():
    node = HTMLNode(props={"href" : "https://www.google.com"})
    assert node.props_to_html() == ' href="https://www.google.com"'


def test_props_to_html_multiple_pairs():
    node = HTMLNode(props={"href" : "https://www.google.com", "target": "_blank"})
    assert node.props_to_html() == ' href="https://www.google.com" target="_blank"'
