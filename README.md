# KOCHCINA

### Descripción:
Dos scripts en python para generar curvas de Koch personalizadas y animarlas con `manim`. Código compañero del vídeo "Cómo cocinar tu propio fractal"

### Requerimientos:
Necesitarás las librerías `numpy` y `matplotlib` para poder ejecutar `horno.py`, además de `random` para poder generar fractales aleatorios. Para poder ejecutar `emplatado.py`, necesitarás además tener `manim` (Yo usé Manim Community v0.18.1).

### Quickstart:
Una vez tengas todos los paquetes instalados, sitúate en la carpeta donde has guardado los dos archivos y ejecuta `manim emplatado.py AnimaMiFractal -pqm` en una terminal. Espera un poco a que procese la animación, y deberías obtener un vídeo de una curva de Koch por pantalla. Cuando quieras cambiar tu fractal, abre el fichero `emplatado.py`, y dentro de la función `MiFractal`, modifica los puntos de `I` y de `G`, cambia `n` para cambiar el grado de resolución, o añade una alternancia en `A`.

### Funcionamiento y uso:
#### Rol de cada script
`horno.py` contiene funciones que calculan todos los puntos de las curvas de Koch que le introduzcas y otra función que realiza un dibujo estático. No necesita a `manim` y las salidas de sus funciones pueden usarse para otros fines. También incluye varias curvas "precocinadas". `emplatado.py` contiene una función `MiFractal` en la que se puede definir el iniciador, generador, número de pasos y alternancia (opcional), otra, `Receta`, que define todas las animaciones que se producirán por pantalla y finalmente una escena de `manim`, llamada `AnimaMiFractal`. 

#### Definir iniciadores y generadores
Los iniciadores (I) y generadores (G) están definidos como una lista de las coordenadas de sus esquinas. Tienen que ser almacenados como arrays de vectores con tres coordenadas `[x,y,0]` (`manim` utiliza siempre vectores tridimensionales, aunque la animación sea bidimensional).
Por ejemplo, `I=np.array([[-2,0,0], [2,1,0]])` define como iniciador el segmento que empieza en (-2,0) y acaba en (2,1). Si quieres crear un polígono, no olvides repetir el primer punto al final para cerrarlo.

#### Obtener un dibujo
Una vez hayas definido I, G, y un número de etapas n, puedes ejecutar la función `Dibujo(I,G,n)` que hay definida en `horno.py` para obtener un dibujo de tu fractal.

#### Obtener una animación
En `emplatado.py`, define I, G, y n en la función `MiFractal`. Después, ejecuta en una terminal `manim emplatado.py AnimaMiFractal -pqm` para obtener una animación. Puedes sustituir `-pqm` por `-pqh` para una animación de alta calidad, o por `-pql` para calidad baja, si quieres un resultado más rápido. Recomendamos que no animes fractales con una n mayor que 9, puede llevarle mucho rato a tu dispositivo. `MiFractal` tiene, por defecto, una curva de Koch clásica y tres curvas "precocinadas" en comentarios: descoméntalas para verlas. Si quieres cambiarle el nombre a tu fractal, ve al final del archivo y, dentro de AnimaMiFractal, busca `Titulo="Mi Fractal"` y cámbialo por lo que quieras.

#### Alternancias
Esto es lo que en el vídeo llamo "Cambio de orientación", y en el código se representa como una A. Hay dos formas de hacer alternancias: una soportada por `KochAlterno` y la otra por `KochAlternoComplejo`. Por defecto, `Dibujo` y `Receta` siempre van a usar `KochAlternoComplejo`. Una alternancia en el paso i-ésimo de construcción es una lista con tantos números como segmentos tiene la curva del paso anterior, y que solo contiene 1's o -1's. Un 1 indica que no se da la vuelta al generador al colocarse en ese segmento, y un -1 que sí. Por ejemplo, `[1,-1,-1,1]` quiere decir que le des la vuelta al generador cuando lo pongas en el segundo y en el tercer segmento. `KochAlternoComplejo` requiere que le des una alternancia para cada paso, y por tanto debe definirse como una lista de listas de alternancia. Si una de las listas se agota, volverá a empezar desde el principio. `KochAlterno` trabaja con una misma lista de alternancia para todos los pasos. Si quieres ver como generar una una alternancia aleatoria, consulta la curva precocinada `Aleatoria` de `horno.py`.

#### Uso avanzado
Puedes usar las funciones `Koch`, `KochAlterno` y `KochAlternoComplejo` para obtener las esquinas de las diferentes etapas de tu fractal como una lista. Devuelven una lista de n+1 elementos, uno por etapa, incluyendo simplemente el iniciador, y cada elemento es una lista conteniendo las coordenadas de las esquinas de la curva correspondiente a esa etapa.

Si sabes de manim, puedes cambiar a tu gusto `Receta` para obtener animaciones distintas.

### Créditos
Código por Jesús Gacías Franco.
