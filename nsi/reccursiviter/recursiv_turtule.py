import turtle

def spirale(n,largeur,angle):
    if n==0:
        return None 
    else:
        turtle.forward(largeur)
        turtle.right(angle)
        spirale(n-1,largeur-10,angle)

turtle.done()
print(spirale(20,200,95))