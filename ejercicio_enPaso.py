from cmu_graphics import *

def onMouseMove(x, y):
    

    app.fondo = 'negro'

Rótulo('*No a escala', 340, 370, relleno='blanco', tamaño=16)

sol = Estrella(200, 200, 35, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))

tierra = Grupo(
    Círculo(200, 200, 150, relleno=None, borde='grisOscuro'),
    Círculo(200, 50, 10, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior'))
    )

mercurio= Grupo(

    Circulo (200, 200, 70, relleno=None, borde="grisOscuro"), 
    Circulo (200, 130, 10, relleno="grisOscuro"))

venus = Grupo(

    Circulo(200, 200, 100, relleno=None, borde="grisOscuro"), 
    Circulo (200, 100, 10, relleno="naranjaMarrón"))



estrella= Estrella(320,40,5,5,relleno='blanco')
estrella1= Estrella(200,40,5,5,relleno='blanco')
estrella2= Estrella(320,160,5,5,relleno='blanco')
fugaz = Linea(320,40,350,20, relleno='blanco')
fugaz1 = Linea(200,40,230,20, relleno='blanco')
fugaz2 = Linea(320,160,350,140, relleno='blanco')

estrella1.dx= - 10
estrella2.dx=-10
estrella.dx= - 10
estrella.dy=+10
estrella1.dy=+10
estrella2.dy=+10
fugaz.dx=-10
fugaz1.dx=-10
fugaz2.dx=-10
fugaz.dx=10
fugaz1.dx=10
fugaz2.dx=10

tierra.dirección = 'sentido-horario'
mercurio.dirección = 'sentido-horario'
venus.dirección = 'sentido-horario'

def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
        mercurio.dirección = 'sentido-horario'
        venus.dirección = 'sentido-horario'
    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'
        mercurio.dirección = 'sentido-horario'
        venus.dirección = 'sentido-horario'

def enPaso():
    fugaz.x2 = estrella.centroX+20
    fugaz1.x2 = estrella1.centroX+20
    fugaz2.x2 = estrella2.centroX+20
    fugaz.x2 = estrella.centroX
    fugaz1.x1 = estrella1.centroX
    fugaz2.x1=estrella2.centroX
    fugaz.y1=estrella.centroY
    fugaz1.y1=estrella1.centroY
    fugaz2.y1=estrella2.centroY
    fugaz.y2=estrella.centroY-20
    fugaz1.y2=estrella1.centroY-20 
    fugaz2.y2=estrella2.centroY-20

    estrella.centroX+=estrella.dx
    estrella1.centroX+=estrella1.dx
    estrella2.centroX+=estrella1.dx 
    fugaz.centroX+=estrella.dx
    fugaz1.centroX+=estrella1.dx
    fugaz2.centroX+=estrella1.dx
    estrella.centroY+=estrella.dy
    estrella1.centroY+=estrella1.dy 
    estrella2.centroY+=estrella1.dy
    fugaz.centroY+=estrella.dy
    fugaz1.centroY+=estrella1.dy
    fugaz2.centroY+=estrella1.dy

    sol.puntos += 1
    if (tierra.dirección == 'sentido-horario'):
        tierra.rotarÁngulo += 3
        mercurio.rotarÁngulo-=7
        venus.rotarÁngulo += 5

    else:
        tierra.rotarÁngulo -= 3
        mercurio.rotarÁngulo-=7
        venus.rotarÁngulo -= 5
    

cmu_graphics.run()