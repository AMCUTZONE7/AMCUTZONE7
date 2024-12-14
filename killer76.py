# fractal_tree.py
import turtle

def draw_tree(t, branch_length, angle, factor):
    """
    Draws a fractal tree using recursion.
    
    Parameters:
    t: The turtle object.
    branch_length: Length of the current branch.
    angle: Angle of branching.
    factor: Factor to reduce branch length after each recursion.
    """
    if branch_length > 5:
        # Draw the main branch
        t.forward(branch_length)
        
        # Draw right subtree
        t.right(angle)
        draw_tree(t, branch_length - factor, angle, factor)
        
        # Return to the original position and orientation
        t.left(2 * angle)
        draw_tree(t, branch_length - factor, angle, factor)
        
        # Reset orientation
        t.right(angle)
        t.backward(branch_length)

def main():
    # Create the turtle screen and set up
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Fractal Tree")
    screen.bgcolor("black")
    
    # Create a turtle object
    t = turtle.Turtle()
    t.color("lime")
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.up()
    t.goto(0, -250)
    t.down()
    
    # Customize the tree
    branch_length = int(screen.numinput("Tree Settings", "Initial branch length (50-200):", 100, 50, 200))
    angle = int(screen.numinput("Tree Settings", "Branching angle (10-45):", 30, 10, 45))
    factor = int(screen.numinput("Tree Settings", "Branch length reduction factor (5-20):", 15, 5, 20))
    
    # Draw the tree
    draw_tree(t, branch_length, angle, factor)
    
    # Wait for the user to close the window
    screen.mainloop()

if __name__ == "__main__":
    main()
