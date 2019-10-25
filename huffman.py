import bisect

class TreeNode:
    def __init__(self, name, prob, lchild=None, rchild=None):
        self.name = name
        self.prob = prob
        self.lchild = lchild
        self.rchild = rchild

    def __repr__(self):
        return f'Tree Name:{self.name} Prob:{self.prob}'

def encode(counts_dict):
    tree_nodes = [TreeNode(name, count, None, None) for name, count in counts_dict.items()]
    return assign_codes(huffman_partition(tree_nodes))

def huffman_partition(tree_nodes):
    sorted_xs = sorted(tree_nodes, reverse=True, key=lambda x: x.prob)
    def helper(xs):
        rchild = xs.pop(-1)
        lchild = xs.pop(-1)
        #Insert into a sorted list.
        bisect.insort(xs, TreeNode(None, rchild.prob + lchild.prob, lchild, rchild))
        if len(xs) == 1:
            return xs[0]
        return huffman_partition(xs)
    return helper(sorted_xs)


def assign_codes(tree):
    def assign_codes_helper(tree, code_lists, code=""):
        if tree.lchild is None and tree.rchild is None:
            code_dict[tree.name] = code
            return
        assign_codes_helper(tree.lchild, code_lists, code+'0')
        assign_codes_helper(tree.rchild, code_lists, code+'1')
    code_dict = []
    assign_codes_helper(tree, code_dict)
    return code_dict