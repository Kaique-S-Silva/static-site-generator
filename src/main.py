from textnode import *

def main():
    node1 = TextNode("Hello, World!", TextNode)
    node2 = TextNode("Hello, World!", TextNode)
    print(node1.__repr__())
    print(node2.__repr__())
    print(node1 == node2)

    text_node_to_html_node(node1)



if __name__ == "__main__":    
    main()