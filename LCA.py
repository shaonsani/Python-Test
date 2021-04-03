class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


def find_ancestor(node):
    parents = dict()
    while node.parent:
        parents[node.parent.value] = True
        node = node.parent
    return parents


def lca(n1, n2):
    n1_ancestors = find_ancestor(n1)
    n2_ancestors = find_ancestor(n2)
    for key, value in n1_ancestors.items():
        if key in n2_ancestors:
            return key

    # IN case we are passing a node who is not in the tree
    if not n1_ancestors:
        return n2.value
    if not n2_ancestors:
        return n1.value


root = Node(1, None)
child1 = Node(2, root)
child2 = Node(3, root)
child3 = Node(4, child2)
child4 = Node(5, child2)

print(lca(child3, child4))

""" 
Time Complexity O(n) ;where h is depth of the tree
Space complexity O(n)
"""
