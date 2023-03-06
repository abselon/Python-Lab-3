from graphviz import Digraph

# Define the tree
tree = Digraph()

tree.node("700")
tree.node("600")
tree.node("800")
tree.node("500")
tree.node("510")
tree.node("610")
tree.node("710")
tree.node("810")
tree.node("400")
tree.node("410")
tree.node("300")
tree.node("310")
tree.node("200")
tree.node("210")
tree.node("100")

tree.edge("700", "600")
tree.edge("700", "800")
tree.edge("600", "500")
tree.edge("600", "610")
tree.edge("800", "710")
tree.edge("800", "810")
tree.edge("500", "400")
tree.edge("500", "510")
tree.edge("400", "300")
tree.edge("400", "410")
tree.edge("300", "200")
tree.edge("300", "310")
tree.edge("200", "100")
tree.edge("200", "210")

# Render and save the tree
tree.render("tree_graphviz.gv", view=True)
