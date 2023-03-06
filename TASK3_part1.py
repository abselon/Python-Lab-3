#part1
from binarytree import Node

root = Node(700)
root.left = Node(600)
root.right = Node(800)
root.left.right = Node(610)
root.right.left = Node(710)
root.right.right = Node(810)
root.left.left = Node(500)
root.left.left.left = Node(400)
root.left.left.right = Node(510)
root.left.left.left.left = Node(300)
root.left.left.left.right = Node(410)
root.left.left.left.left.left = Node(200)
root.left.left.left.left.right = Node(310)
root.left.left.left.left.left.left = Node(100)
root.left.left.left.left.left.right = Node(210)


print(root)
#
#      __1
#     /   \
#    2     3
#     \
#      4
#

