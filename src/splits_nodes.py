from textnode import *

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