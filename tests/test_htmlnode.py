import pytest
from src.htmlnode import HTMLNode, LeafNode


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


def test_leafnode_to_html_no_value():
    node = LeafNode(None, None)
    with pytest.raises(ValueError):
        node.to_html()


def test_leafnode_to_html_no_tag():
    node = LeafNode(None, "Lorem ipsum")
    assert node.to_html() == "Lorem ipsum"


def test_leafnode_to_html_p():
    node = LeafNode("p", "Lorem ipsum")
    assert node.to_html() == "<p>Lorem ipsum</p>"


def test_leafnode_to_html_link():
    node = LeafNode("a", "Lorem ipsum", {"href":"https://www.boot.dev"})
    assert node.to_html() == '<a href="https://www.boot.dev">Lorem ipsum</a>'


def test_leafnode_to_html_img():
    node = LeafNode("img", "", {"src":"url/of/img.jpg", "alt":"description of img"})
    assert node.to_html() == '<img src="url/of/img.jpg" alt="description of img">'