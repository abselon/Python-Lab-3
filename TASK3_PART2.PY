from anytree import Node, RenderTree

root = Node(700)
node_600 = Node(600, parent=root)
node_500 = Node(500, parent=node_600)
node_400 = Node(400, parent=node_500)
node_300 = Node(300, parent=node_400)
node_200 = Node(200, parent=node_300)
node_310 = Node(310, parent=node_300)
node_410 = Node(410, parent=node_400)
node_510 = Node(510, parent=node_500)
node_610 = Node(610, parent=node_600)
node_800 = Node(800, parent=root)
node_710 = Node(710, parent=node_800)
node_810 = Node(810, parent=node_800)

for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}") 
