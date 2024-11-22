import numpy as np
import matplotlib.pyplot as plt
from random import seed, choice

def Transformacion(P, p1, p2, q1, q2, a=1):
    """
    Computa la transformación rígida del plano que lleva los puntos q1 y q2 a p1 y p2 respectivamente, y se la aplica al punto P.
    Si a=1, la transformación preserva la orientación, mientras que con a=-1, la invierte.
    """
    v1=p2-p1
    v2=q2-q1
    l1=np.linalg.norm(v1)
    l2=np.linalg.norm(v2)
    A=np.arctan2(np.cross(v2,v1)[2],np.matmul(v1,v2))
    cos=np.cos(A)
    sin=np.sin(A)

    return np.matmul([[cos, -a*sin, 0],[sin, a*cos,0], [0,0,1]],P-q1)*l1/l2+p1


def Koch(I, G, n):
    """
    Dados un iniciador I, un generador G (expresados como arrays de vectores tridimensionales) y un número de pasos n,
    computa la posición de las esquinas de los polígonos que tienden a la curva de Koch límite definida por I y G. Devuelve una lista de
    n+1 arrays, siendo cada uno las posiciones de las esquinas del estadio i-ésimo de la construcción.
    """
    
    K=[I] #Se añade el iniciador a K
    N=len(G)-1
    inicioG=G[0]
    finalG=G[N]

    Gtrunc=G[0:N] #Se elimina el punto final de G, ya que el punto final de una copia del generador acaba en el mismo punto que el inicial de la siguiente

    for paso in range(n):
        K.append([])
      
        for j in range(len(K[paso])-1):
            inicio=K[paso][j]
            fin=K[paso][j+1]
            for a in Gtrunc:
                K[paso+1].append(Transformacion(a, inicio, fin, inicioG, finalG)) #Para cada segmento del paso anterior, se ve donde acaba cada esquina del generador (truncado) tras moverlo
    
        K[paso+1].append(I[-1]) #Se añade el último punto, que por el truncamiento no se ha añadido antes: resulta ser el punto final del iniciador

    return K

def KochAlterno(I,G,n,A=[1,-1]):
    """
    Dados un iniciador I, un generador G (expresados como arrays de vectores tridimensionales), un número de pasos n,
    y un vector de alternancia (toma valor 1 o -1 según si se quiere preservar o invertir la orientación del generador)
    computa la posición de las esquinas de los polígonos que tienden a la curva de Koch límite definida por I, G y A. La regla
    de alternancia es igual en cada paso, y viene determinada por A (si se agota A, vuelve a empezar). Devuelve una lista de
    n+1 arrays, siendo cada uno las posiciones de las esquinas del estadio i-ésimo de la construcción.
    """
    K=[I]
    N=len(G)-1
    inicioG=G[0]
    finalG=G[N]

    Gtrunc=G[0:N]

    periodo=len(A) #Luego se hace un módulo con respecto a este periodo para que si se acaba A, se vuelva a leer desde el principio
    
    for paso in range(n):
        K.append([])
        
        for j in range(len(K[paso])-1):
            inicio=K[paso][j]
            fin=K[paso][j+1]
            for a in Gtrunc:
                K[paso+1].append(Transformacion(a, inicio, fin, inicioG, finalG, a=A[j%periodo]))
    
        K[paso+1].append(I[-1])

    return K

def KochAlternoComplejo(I,G,n,A=[[1,-1]*10]):
    """
    Dados un iniciador I, un generador G (expresados como arrays de vectores tridimensionales), un número de pasos n,
    y un array de vectores de alternancia (toma valor 1 o -1 según si se quiere preservar o invertir la orientación del generador)
    computa la posición de las esquinas de los polígonos que tienden a la curva de Koch límite definida por I, G y A. La regla de
    alternancia puede cambiarse en cada paso, y viene determinada por A[i] (si se agota A[i], vuelve a empezar). El A por defecto
    no admite valores de n mayores que 10. Devuelve una lista de n+1 arrays, siendo cada uno las posiciones de las esquinas del
    estadio i-ésimo de la construcción.
    """
    
    #SI n>10, NO SE PUEDE UTILIZAR EL VALOR DE A POR DEFECTO
    K=[I]
    N=len(G)-1
    inicioG=G[0]
    finalG=G[N]

    Gtrunc=G[0:N]
    
    for paso in range(n):
        periodo=len(A[paso])
        K.append([])
        
        for j in range(len(K[paso])-1):
            inicio=K[paso][j]
            fin=K[paso][j+1]
            for a in Gtrunc:
                K[paso+1].append(Transformacion(a, inicio, fin, inicioG, finalG, a=A[paso][j%periodo]))
    
        K[paso+1].append(I[-1])

    return K


def Dibujo(I,G,n,A=None):
    """
    Enseña por pantalla el estadio n-ésimo de la construcción de una curva de Koch con
    iniciador I y generador G.
    """

    if A==None:
        K=Koch(I,G,n)[n]
    else:
        K=KochAlternoComplejo(I,G,n,A)[n]

    for i in range(len(K)-1):
        plt.plot([K[i][0], K[i+1][0]], [K[i][1], K[i+1][1]], 'k-', linewidth=0.5)

    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    
    plt.show()


def CopoDeNieve(n, dibujar=False):
    """
    Devuelve el n-ésimo estadio del copo de nieve
    """
    A=np.sqrt(3)
    L=6
    I=np.array([[-L/2,A*L/4,0],[L/2,A*L/4,0],[0,-A*L/4,0],[-L/2,A*L/4,0]])
    G=np.array([ [-3,0,0], [-1,0,0],[0,A,0], [1,0,0], [3,0,0]])
    A=None

    if dibujar==True:
        Dibujo(I,G,n)

    return([I,G,n,A])

def Sierpinski(n, dibujar=False):
    """
    Devuelve el n-ésimo estadio del triángulo de Sierpinski
    """
    A=np.sqrt(3)
    L=6
    I=np.array([[-3,0,0],[3,0,0]])
    G=np.array([[-3,0,0],[-1.5,1.5*A,0],[1.5,1.5*A,0],[3,0,0]])

    N=len(G)-1

    A=[[]]

    for i in range(n):
        for j in range(3**i):
            A[i].append((-1)**(j+i))
        A.append([])

    if dibujar==True:
        Dibujo(I,G,n,A)

    return([I,G,n,A])


def Aleatorio(n, semilla=4041, dibujar=False):
    """
    Devuelve el n-ésimo estadio de un fractal de Koch aleatorio.
    El segundo parámetro es una semilla: cambiarla cambiará el fractal aleatorio obtenido.
    """
    A=np.sqrt(3)

    I=np.array([[-3,0,0], [3,0,0]])
    G=np.array([ [-3,0,0], [-1,0,0],[0,A,0], [1,0,0], [3,0,0]])

    A=[[]]
    El=[1,-1]

    seed(semilla)
    for i in range(n):
        for j in range(4**i):
            A[i].append(choice(El))
        A.append([])

    if dibujar==True:
        Dibujo(I,G,n,A)

    return([I,G,n,A])