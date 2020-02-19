order = []
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def pre_order(self):
        temp = []
        while self.left != None:
            order.append(self.data)
            temp.append(self)
            self = self.left
        order.append(self.data)
        temp.append(self)
        while len(temp):
            i = temp.pop()
            if i.right != None:
                i = i.right
                i.pre_order()
            else:
                continue


root = Node('D')
root_l = Node('B')
root_r = Node('E')
root.left = root_l
root.right = root_r
leaf_root_l = Node('A')
leaf_root_l_r = Node('C')
leaf_root_r = Node('F')
root_l.left = leaf_root_l
root_l.right = leaf_root_l_r
root_r.right = leaf_root_r
test = Node('K')
test2 = Node('S')
leaf_root_l_r.left = test
leaf_root_l_r.right = test2
post_seq = root.pre_order()
print(order)
