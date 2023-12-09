class Node:
    def __init__(self, data: str):
        self.data = data
        self.name = data[0:3]
        self.left = data[7:10]
        self.right = data[12:15]

        self.shortcut = []


def main():
    nodes = {}

    with open("../input.txt") as f:
        instructions = f.readline().strip()

        # empty
        f.readline()

        for line in f:
            line = line.strip()
            node = Node(line)
            nodes[node.name] = node

    for node in nodes.keys():
        start_node = node
        shortcut = []
        zed = 0 if node.endswith("Z") else None

        i = 0
        for instruction in instructions:
            if instruction == "L":
                node = nodes[node].left
            else:
                node = nodes[node].right

            shortcut.append(node)
            if node.endswith("Z"):
                zed = i
            i += 1

        nodes[start_node].shortcut = shortcut[-1], zed

    steps = 0
    current_nodes = list(filter(lambda node: node.endswith("A"), nodes.keys()))

    while True:
        next_nodes = []
        zeds = list()
        for n in current_nodes:
            node = nodes[n]
            shortcut, zed = node.shortcut
            next_nodes.append(shortcut)
            if zed:
                zeds.append(zed)

        if len(zeds) > 5:
            print(current_nodes, zeds)
            steps += list(zeds)[0] + 1
            break

        current_nodes = next_nodes

        steps += len(instructions)

    print(steps)


main()
