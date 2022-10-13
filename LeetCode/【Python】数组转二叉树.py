arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def print_all(node):
    if node is not None:
        print(node.data)
        print_all(node.left)
        print_all(node.right)

node_list = []
for i in range(len(arr)):
    node = Node(arr[i], None, None)
    node_list.append(node)

if len(node_list) > 0:
    for i in range(int(len(arr)/2)-1):
        if node_list[2*i + 1].left is None:
            node_list[i].left = node_list[2*i+1]
        if node_list[2*i + 2].right is None:
            node_list[i].right = node_list[2*i +2]
    last_idx = int(len(arr)/2) - 1
    node_list[last_idx].left = node_list[last_idx * 2 +1]
    if len(arr) % 2 == 1:
        node_list[last_idx].right = node_list[last_idx * 2 + 2]

if node_list is not None:
    print_all(node_list[0])
# if __name__ == '__main__':
#     if node_list is not None:
#         print_all(node_list[0])
