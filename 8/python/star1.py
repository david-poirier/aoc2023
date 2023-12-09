class Node:
    def __init__(self, data: str):
        self.data = data
        self.name = data[0:3]
        self.left = data[7:10]
        self.right = data[12:15]


def main():
    nodes = {}

    with open("../input.txt") as f:
        instructions = list(f.readline().strip())

        # empty
        f.readline()

        for line in f:
            line = line.strip()
            node = Node(line)
            nodes[node.name] = node

    steps = 0
    current_instruction = 0
    current_node = "AAA"

    while current_node != "ZZZ":
        if instructions[current_instruction] == "L":
            current_node = nodes[current_node].left
        else:
            current_node = nodes[current_node].right

        current_instruction += 1
        if current_instruction >= len(instructions):
            current_instruction = 0

        steps += 1

    print(steps)


main()
