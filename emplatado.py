from horno import *
from manim import *

config.background_color = YELLOW_A
config.default_stroke_color=BLACK

def MiFractal():
    """
    Aquí dentro es donde tienes que introducir tu iniciador (I), generador (G), y número de pasos (n).
    Si quieres añadir también una alternancia (soportada por KochAlternoComplejo), añádela en A.
    """
    I=np.array([[-3,0,0],[3,0,0]])
    G=np.array([ [-3,0,0], [-1,0,0],[0,np.sqrt(3),0], [1,0,0], [3,0,0]])
    n=4
    A=None

    #¿Quieres un fractal ya preparado? ¡Prueba con estos! Aumenta el número para ver más detalles
    #[I,G,n,A]=CopoDeNieve(5)
    #[I,G,n,A]=Sierpinski(5)
    [I,G,n,A]=Aleatorio(5, semilla=111)


    return([I,G,n,A])

def Receta(self,I,G,n, A=None, Dim=True, Titulo=None):
    """
    Este código se encarga de dibujar tu fractal y animarlo. Si sabes lo que estás haciendo, puedes modificarlo para cambiar las animaciones a tu gusto.
    """
    N=len(G)-1

    TextoIn=Tex("Iniciador").move_to([-5,3,0]).set_color(BLACK)
    TextoGen=Tex("Generador").move_to([-5,-1,0]).set_color(BLACK)

    

    Separador=Line([-3,5,0], [-3,-5,0]).set_color(BLACK)

    Iniciador=VMobject().set_points_as_corners(I).scale_to_fit_width(3.5).move_to((TextoIn.get_center()+TextoGen.get_center())/2).set_color(BLACK).set_stroke(width=2)
    if Iniciador.get_height()>3:
        Iniciador.scale_to_fit_height(3).move_to((TextoIn.get_center()+TextoGen.get_center())/2)

    Generador=VMobject().set_points_as_corners(G).scale_to_fit_width(3.5).move_to((TextoGen.get_center()+[-5,-4,0])/2).set_color(BLACK).set_stroke(width=2)
    if Generador.get_height()>3:
        Generador.scale_to_fit_height(3).move_to((TextoGen.get_center()+[-5,-4,0])/2)


    #Toda esta parte genera los puntos del fractal y se asegura de que quepa en el marco y el estadio final se quede centrado
    if A==None:
        K=Koch(I,G,n)
    else:
        K=KochAlternoComplejo(I,G,n,A)
    Kmat=[np.array(k) for k in K ]
    Centro=np.array([2+1/18,0,0])
    if K[n][0].all()==K[n][-1].all():
        CM=np.array([np.mean(np.array(K[n])[:-1,0]),np.mean(np.array(K[n])[:-1,1]),0])
    else:
        CM=np.array([np.mean(np.array(K[n])[:,0]),np.mean(np.array(K[n])[:,1]),0])
    
    for k in range(n+1):
        Kmat[k]=Kmat[k]-np.tile(CM, (len(Kmat[k][:,0]),1))

    
    MAX_Y=np.max(np.abs(np.array(K[n])[:,1]))
    if MAX_Y>7.5/2:
        for k in range(n+1):
            Kmat[k]=Kmat[k]/MAX_Y*7.5/2
    MAX_X=np.max(np.abs(np.array(K[n])[:,0]))
    if MAX_X>5:
        for k in range(n+1):
            Kmat[k]=Kmat[k]/MAX_X*5
    
    
    for k in range(n+1):
        Kmat[k]=Kmat[k]+np.tile(Centro, (len(Kmat[k][:,0]),1))


    L=np.linalg.norm(G[0]-G[N])
    l=np.mean([np.linalg.norm(G[i]-G[i+1]) for i in range(N)])
    D=np.log(N)/np.log(L/l)

    Dimension=DecimalNumber(D,num_decimal_places=3, unit="...").move_to(Centro+3.5*DOWN).set_color(BLACK)
    Ig=Tex(r"$D\approx$").next_to(Dimension, LEFT).set_color(BLACK)
    Poli=[]
        
    for k in range(n+1):
        Poli.append(VGroup(*[Line(Kmat[k][j], Kmat[k][j+1]) for j in range(len(K[k])-1)]).set_stroke(width=2).set_color(BLACK))

    self.play(Write(VGroup(TextoIn, TextoGen)), Create(Separador))
    self.play(FadeIn(VGroup(Iniciador,Generador)))
    self.wait()
    Icop=Iniciador.copy()
    self.play(Transform(Icop, VMobject().set_points_as_corners(*[Kmat[0]]).set_stroke(width=2).set_color(BLACK)))
    self.add(Poli[0])
    self.remove(Icop)
    self.wait()
    for j in range(n):
        SEGS=len(Poli[j])
        Gcops=[]
        if 3/SEGS>=1/10:
            for k in range(SEGS):
                Gcops.append(Generador.copy())
                if j==0 and len(I)==2:
                    rt=1
                else:
                    rt=3/SEGS

                self.play(FadeOut(Poli[j][k]), Transform(Gcops[k], VMobject().set_points_as_corners(*[Kmat[j+1][N*k:N*(k+1)+1]]).set_stroke(width=2).set_color(BLACK)), run_time=rt)
            self.add(Poli[j+1])
            self.remove(Poli[j])
            for k in range(SEGS):
                self.remove(Gcops[k])
        else:
            self.play(*[ReplacementTransform(Poli[j][i], VMobject().set_points_as_corners(*[Kmat[j+1][N*i:N*(i+1)+1]]).set_stroke(width=2).set_color(BLACK)) for i in range(len(Poli[j]))])
            self.add(Poli[j+1])
            self.remove(Poli[j])
        self.wait()
    if Dim==True:
        self.play(Write(Ig))
        self.play(Write(Dimension))
        self.wait()
    if Titulo!=None:
        if Dim==True:
            self.play(FadeOut(VGroup(Ig,Dimension)))
        self.play(Poli[n].animate.move_to(ORIGIN), VGroup(Iniciador, Generador, Separador, TextoIn, TextoGen).animate.shift(5*LEFT))
        Tit=Tex(Titulo).scale(1.5).move_to(3.5*DOWN).set_color(BLACK)
        self.play(Write(Tit))
    self.wait()




class AnimaMiFractal(Scene):
    """
    Esta parte del código se encarga de ejecutar la ristra de animaciones de Receta con el fractal que has definido en MiFractal(). Cambia Dim=True a Dim=False si no quieres que te escriba su dimensión,
    o cambia el título por lo que más te apetezca. Receta va a hacer todo lo posible porque tu fractal quepa en la pantalla y no se solape con nada, pero puede que no lo logre: en ese caso, escala
    tu iniciador. Escalar el generador no tendrá ningún efecto. Ejecuta "manim emplatado.py AnimaMiFractal -pqm" para que funcione. Más información en el README.
    """
    def construct(self):
        Receta(self, *MiFractal(), Dim=True, Titulo="Mi Fractal")
    