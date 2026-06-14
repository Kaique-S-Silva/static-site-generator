def markdown_to_blocks(markdown):
    block = markdown.split("\n\n")
    cleaned = []

    for i in block:
        lines = i.strip().split("\n")
        cleaning = "\n".join([line.strip() for line in lines])
        if cleaning:
            cleaned.append(cleaning)
    return cleaned