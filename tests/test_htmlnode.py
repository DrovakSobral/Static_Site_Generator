import pytest
from src.htmlnode import HTMLNode, LeafNode, ParentNode


def test_props_to_html_none():
    node = HTMLNode()
    assert node.props_to_html() == ""


def test_props_to_html_empty():
    node = HTMLNode(props={})
    assert node.props_to_html() == ""


def test_props_to_html_multiple_pairs():
    node = HTMLNode(props={"href": "https://www.google.com"})
    assert node.props_to_html() == ' href="https://www.google.com"'


def test_props_to_html_multiple_pairs():
    node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    assert node.props_to_html() == ' href="https://www.google.com" target="_blank"'


def test_leafnode_to_html_no_value():
    node = LeafNode("p", None)
    with pytest.raises(ValueError, match="Invalid HTML: no value"):
        node.to_html()


def test_leafnode_to_html_no_tag():
    node = LeafNode(None, "Lorem ipsum")
    assert node.to_html() == "Lorem ipsum"


def test_leafnode_to_html_p():
    node = LeafNode("p", "Lorem ipsum")
    assert node.to_html() == "<p>Lorem ipsum</p>"


def test_leafnode_to_html_link():
    node = LeafNode("a", "Lorem ipsum", {"href": "https://www.boot.dev"})
    assert node.to_html() == '<a href="https://www.boot.dev">Lorem ipsum</a>'


def test_leafnode_to_html_img():
    node = LeafNode("img", "", {"src": "url/of/img.jpg", "alt": "description of img"})
    assert node.to_html() == '<img src="url/of/img.jpg" alt="description of img">'


def test_parentnode_to_html_tag_none():
    node = ParentNode(None, None, None)
    with pytest.raises(ValueError, match="Invalid HTML: no tag"):
        node.to_html()


def test_parentnode_to_html_tag_empty_string():
    node = ParentNode("", None, None)
    with pytest.raises(ValueError, match="Invalid HTML: no tag"):
        node.to_html()


def test_parentnode_to_html_children_none():
    node = ParentNode("div", None, None)
    with pytest.raises(ValueError, match="Invalid HTML: no children"):
        node.to_html()


def test_parentnode_to_html_children_empty_list():
    node = ParentNode("div", [], None)
    with pytest.raises(ValueError, match="Invalid HTML: no children"):
        node.to_html()


def test_parentnode_to_html_children_one():
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    assert parent_node.to_html() == "<div><span>child</span></div>"


def test_parentnode_to_html_children_multiple():
    child_node_1 = LeafNode("span", "child_1")
    child_node_2 = LeafNode("b", "child_2")
    parent_node = ParentNode("div", [child_node_1, child_node_2])
    assert parent_node.to_html() == "<div><span>child_1</span><b>child_2</b></div>"


def test_parentnode_to_html_grandchildren():
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    assert parent_node.to_html() == "<div><span><b>grandchild</b></span></div>"
