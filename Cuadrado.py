#Cuadrado
import turtle
t=turtle.Pen()
def micuadrado (size):
    for x in range(1,5):
        t.forward(size)
        t.left(90)
a=int(input("Ingrese la longitud:")) 
micuadrado(a)
