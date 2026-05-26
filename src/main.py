import textnode

def main():
    node1 = textnode.TextNode("Hello, World!", textnode.Bender.AIR_BENDER)
    node2 = textnode.TextNode("Hello, World!", textnode.Bender.AIR_BENDER)
    print(node1.__repr__())
    print(node2.__repr__())
    print(node1 == node2)


if __name__ == "__main__":    
    main()