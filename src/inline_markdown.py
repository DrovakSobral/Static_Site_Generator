from textnode import TextNode, TextType
import re


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        sub_nodes = old_node.text.split(delimiter)
        if len(sub_nodes) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sub_nodes)):
            if sub_nodes[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sub_nodes[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(sub_nodes[i], text_type))
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text: str) -> list[tuple]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        raw_images = extract_markdown_images(old_node.text)
        if raw_images == []:
            new_nodes.append(old_node)
            continue
        else:
            old_text = old_node.text
            for raw_image in raw_images:
                img_alt_txt = raw_image[0]
                img_link = raw_image[1]
                split_text = old_text.split(f"![{img_alt_txt}]({img_link})", 1)
                if split_text[0] != "":
                    new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                new_nodes.append(TextNode(img_alt_txt, TextType.IMAGE, img_link))
                old_text = split_text[1]
            if old_text != "":
                new_nodes.append(TextNode(old_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        raw_links = extract_markdown_links(old_node.text)
        if raw_links == []:
            new_nodes.append(old_node)
            continue
        else:
            old_text = old_node.text
            for raw_link in raw_links:
                link_txt = raw_link[0]
                link_url = raw_link[1]
                split_text = old_text.split(f"[{link_txt}]({link_url})", 1)
                if split_text[0] != "":
                    new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                new_nodes.append(TextNode(link_txt, TextType.LINK, link_url))
                old_text = split_text[1]
            if old_text != "":
                new_nodes.append(TextNode(old_text, TextType.TEXT))
    return new_nodes


def text_to_textnode(raw_markdown: str) -> list[TextNode]:
    nodes = [TextNode(raw_markdown, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
