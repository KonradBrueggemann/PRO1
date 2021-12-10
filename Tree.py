class Tree:
    def __init__(self, label, ID, children=None):
        self.label = label
        self.ID = ID
        self.children = children

    def get_label(self):
        return self.label

    def get_id(self):
        return self.ID

    def get_children(self):
        return self.children

    def is_root(self):
        return self.label == "S"

    def is_leaf(self):
        return self.children is None or self.children == []

    def degree(self):
        amount = []
        if self.children is None:
            return 0
        else:
            for child in self.children:
                amount.append(Tree.degree(child))
        return len(amount)

    def pre_order(self, by_label=False, only_leaves=False):
        order = []
        leaves = []
        if self.children is not None:
            if not by_label:
                order.append(self.ID)
                if self.is_leaf():
                    leaves.append(self.ID)

            else:
                order.append(self.label)
                if self.is_leaf():
                    leaves.append(self.label)
            for child in self.children:
                if not by_label:
                    order.extend(Tree.pre_order(child))
                    if only_leaves:
                        leaves.extend(Tree.pre_order(child, only_leaves=True))
                else:
                    order.extend(Tree.pre_order(child, by_label=True))
                    if only_leaves:
                        leaves.extend(Tree.pre_order(child, by_label=True, only_leaves=True))
        else:
            if not by_label:
                order.append(self.ID)
                if self.is_leaf():
                    leaves.append(self.ID)
            else:
                order.append(self.label)
                if self.is_leaf():
                    leaves.append(self.label)
        if only_leaves:
            return leaves
        else:
            return order

    def __str__(self):
        result = self.label
        if self.children is None:
            return f"({result})"
        else:
            for child in self.children:
                result += f"{Tree.__str__(child)}"
        return f"({result})"