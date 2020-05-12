class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


one = TreeNode(1)
two = TreeNode(2)
four = TreeNode(4)
three = TreeNode(3)
five = TreeNode(5)
six = TreeNode(6)
seven = TreeNode(7)
eight = TreeNode(8)
nine = TreeNode(9)
ten = TreeNode(10)

one.right = two
two.left = three
three.right = four
four.right = five

import collections
parent = {}
depth = [-1 for i in range(101)]
print(depth)
visited = {}

depth[one.val] = 0
q = collections.deque()
q.append(one)
depth[one.val] = 0
parent[one.val] = -100
while q:
    curr = q.popleft()
    if visited.get(curr,1):
        if curr.left != None:
            q.append(curr.left)
            parent[curr.left.val] = curr.val
            depth[curr.left.val] = depth[curr.val]+1
        if curr.right != None:
            q.append(curr.right)
            parent[curr.right.val] = curr.val
            depth[curr.right.val] = depth[curr.val] + 1

        visited[curr] = 0
x = 1
y =3
if parent[x] != parent[y] and depth[x] == depth[y]:
    print(True)
print(False)

