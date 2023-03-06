from treelib import Node, Tree

# Create the tree
tree = Tree()
tree.create_node("700", "700")  # root node
tree.create_node("600", "600", parent="700")
tree.create_node("800", "800", parent="700")
tree.create_node("500", "500", parent="600")
tree.create_node("510", "510", parent="500")
tree.create_node("610", "610", parent="600")
tree.create_node("400", "400", parent="500")
tree.create_node("410", "410", parent="400")
tree.create_node("300", "300", parent="400")
tree.create_node("310", "310", parent="300")
tree.create_node("200", "200", parent="300")
tree.create_node("210", "210", parent="200")
tree.create_node("100", "100", parent="200")
tree.create_node("810", "810", parent="800")
tree.create_node("710", "710", parent="800")

# Show the tree
tree.show()
