from turtle import Turtle, Screen

# Define the colors
node_color = "white"
line_color = "black"

# Set up the turtle screen
screen = Screen()
screen.setup(800, 800)
screen.title("Binary Tree Visualization")

# Create the turtle object
t = Turtle()
t.hideturtle()
t.speed(0)

# Define the function to draw a node
def draw_node(node, x, y, level):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.fillcolor(node_color)
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.setpos(x, y - 15)
    t.pendown()
    t.write(node, align="center", font=("Arial", 12, "normal"))
    if level > 0:
        t.penup()
        t.setpos(x, y - 25)
        t.pendown()
        t.pencolor(line_color)
        t.setheading(270)
        t.forward(50)
        t.penup()
        t.setpos(x, y - 50)
        t.pendown()
        t.forward(50)
        t.penup()
        t.setpos(x, y - 25)
        t.pendown()
        t.setheading(90)
        t.forward(50)
        t.penup()
        t.setpos(x - 50, y - 50)
        t.pendown()
        t.forward(100)
    return x, y - 50

# Define the recursive function to draw the tree
def draw_tree(node, x, y, level=0):
    if node is None:
        return x, y
    x_left, y_left = draw_tree(node.left, x - 100, y - 50, level + 1)
    x_right, y_right = draw_tree(node.right, x + 100, y - 50, level + 1)
    x_node, y_node = draw_node(node.val, x, y, level)
    return x_node, y_node

# Define the binary tree
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

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

# Draw the binary tree
draw_tree(root, 0, 400)

# Exit on click
screen.exitonclick()
