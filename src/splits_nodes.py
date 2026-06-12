from textnode import *
from extract_markdown import *

def split_nodes_delimeter(old_nodes: list[TextNode], delimeter: str, text_type: TextType) ->  list[TextNode]:
    return_list = []

    for i in old_nodes:
        if i.text_type != TextType.TEXT:
            return_list.append(i)
        else:
            i_text = i.text.split(delimeter)
            if len(i_text) % 2 == 0:
                raise Exception("Invalid markdown syntax")
            for j in range(len(i_text)):
                if i_text[j] == "":
                    continue
                if j % 2 == 0:
                    return_list.append(TextNode(text=i_text[j], text_type=TextType.TEXT))
                else:
                    return_list.append(TextNode(i_text[j], text_type))
    return return_list


def _split_nodes_markup(old_nodes, extract_func, text_type):
    return_list = []

    for i in old_nodes:
        if i.text_type != TextType.TEXT:
            return_list.append(i)
        else:
            nodes = extract_func(i.text)
            if len(nodes) == 0:
                return_list.append(i)
            else:
                original_text = i.text

                for node in nodes:
                    alt = node[0]
                    url = node[1]
                    target_markdown = f"![{alt}]({url})" if text_type == TextType.IMAGE else f"[{alt}]({url})"

                    sections = original_text.split(target_markdown, 1)

                    if sections[0] != "":
                        return_list.append(TextNode(sections[0], TextType.TEXT))
                    return_list.append(TextNode(alt, text_type, url))

                    original_text = sections[1]

                if original_text != "":
                    return_list.append(TextNode(original_text, TextType.TEXT))

    return return_list
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    return _split_nodes_markup(old_nodes, extract_markdown_images, TextType.IMAGE)

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    return _split_nodes_markup(old_nodes, extract_markdown_links, TextType.LINK)