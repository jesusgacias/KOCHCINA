# KOCHCINA

### Descripción:
Dos scripts en python para generar curvas de Koch personalizadas y animarlas con el paquete manim. Código compañero del vídeo "Cómo cocinar tu propio fractal"

### Requerimientos:
Necesitarás los paquetes `numpy` y `matplotlib` para poder ejecutar `horno.py`, además del paquete random para poder generar fractales aleatorios. Para poder ejecutar `emplatado.py`, necesitarás además tener `manim` (Yo usé Manim Community v0.18.1).

### Quickstart:
Una vez tengas todos los paquetes instalados, sitúate en la carpeta donde has guardado los dos archivos y ejecuta `manim emplatado.py AnimaMiFractal -pqm` en una terminal. Espera un poco a que procese la animación, y deberías obtener un vídeo de una curva de Koch por pantalla. Cuando quieras cambiar tu fractal, abre el fichero `emplatado.py`, y dentro de la función MiFractal(), modifica los puntos de `I` y de `G`, cambia `n` para cambiar el grado de resolución, o añade una alternancia en `A`.

### Funcionamiento y uso:
#### Iniciadores y generadores:
Los iniciadores (I) y generadores (G) están definidos como una lista de las coordenadas de sus esquinas. Tienen que ser almacenados como arrays de vectores con tres coordenadas `[x,y,0]` (`manim` utiliza siempre vectores tridimensionales, aunque la animación sea bidimensional).
Por ejemplo, `I=np.array([[-2,0,0], [2,1,0]])` define como iniciador el segmento que empieza en (-2,0) y acaba en (2,1). Si quieres crear un polígono, no olvides repetir el primer punto.

#### Obtener un dibujo
Una vez tengas I, G, y un número de etapas seleccionado (n), puedes ejecutar Dibujo(I,G,n) en 

#### Alternancias:
Esto es lo que en el vídeo llamo "Cambio de orientación". 


####
`horno.py` se encarga de calcular todos los puntos de tu fractal con las funciones `Koch`, `KochAlterno` y `KochAlternoComplejo`. Además, la función `Dibujo` te permite ver un dibujo sencillo de tu fractal antes de animarlo.
