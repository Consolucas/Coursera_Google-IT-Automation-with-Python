import math

def triangle(base, height):
    return base*height/2

def rectangle(base, height):
    return base*height

def circle(radius):
    return math.pi*(radius**2)

# usamos esse script para usarmos como importação no terminal, e fazermos contas direto do interprete


def donut(outside_radius, inside_radius):
    return circle(outside_radius), circle(inside_radius)