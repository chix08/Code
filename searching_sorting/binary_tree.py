order = []
inorderseq = []
st = []
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
    #Another way for preOrder
    def preorderIterative(root):

        if (root == None):
            return

        st = []

        # start from root node (set current node to root node)
        curr = root

        # run till stack is not empty or current is
        # not NULL
        while (len(st) or curr != None):

            # Print left children while exist
            # and keep appending right into the
            # stack.
            while (curr != None):

                print(curr.data)

                if (curr.right != None):
                    st.append(curr.right)

                curr = curr.left

                # We reach when curr is NULL, so We
            # take out a right child from stack
            if (len(st) > 0):
                curr = st[-1]
                st.pop()

    def inorder(self):
        while self.left != None:
            st.append(self)
            self = self.left
        inorderseq.append(self.data)
        while st:
            n = st.pop()
            inorderseq.append(n.data)
            n = n.right
            n.inorder()




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
# post_seq = root.pre_order()
# print(post_seq)
root.inorder()
print (inorderseq)