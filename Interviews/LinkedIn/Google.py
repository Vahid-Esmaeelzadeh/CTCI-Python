
class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def calc(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.val

    operator = root.val

    if operator == '+':
        return calc(root.left) + calc(root.right)
    elif operator == '-':
        return calc(root.left) - calc(root.right)
    elif operator == '*':
        return calc(root.left) * calc(root.right)
    elif operator == '/':
        return calc(root.left) / calc(root.right)
    else:
        return None


class treeNode:
    def __init__(self, val):
        self.val = val
        self.var_name = None
        self.left = None
        self.right = None


def calc(root, symbol_tab={}):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        if root.var_name is None:
            return root.val
        return symbol_tab[root.var_name]

    operator = root.val

    if operator == '+':
        return calc(root.left, symbol_tab) + calc(root.right, symbol_tab)
    elif operator == '-':
        return calc(root.left, symbol_tab) - calc(root.right, symbol_tab)
    elif operator == '*':
        return calc(root.left, symbol_tab) * calc(root.right, symbol_tab)
    elif operator == '/':
        return calc(root.left, symbol_tab) / calc(root.right, symbol_tab)
    elif operator == "let":
        # root.var_name = x
        left_val = calc(root.left, symbol_tab)
        symbol_tab[root.var_name] = left_val
        right_val = calc(root.right, symbol_tab)
        return right_val
    else:
        return None





































































