INTEGRANTES
- MATEO VANEGAS
- ANDRES GARCÍA
- LUIS SANCHEZ


# Simulación del Problema de los Dos y Tres Cuerpos en Python

## Introducción
El problema de los cuerpos en interacción gravitacional es un pilar de la física clásica. Mientras que el problema de dos cuerpos tiene soluciones analíticas exactas y predecibles, el problema de tres cuerpos presenta un comportamiento caótico y no tiene una solución general conocida. Este proyecto utiliza métodos numéricos para simular ambos escenarios, basándose en las ecuaciones de Newton y conceptos extraídos del documento _"The Three-Body Problem"_ de Juhan Frank (2006, LSU).

---

## Ecuaciones Diferenciales Utilizadas

### Problema de Dos Cuerpos

La fuerza gravitacional se modela con la Ley de Gravitación Universal de Newton que establece que toda partícula con masa ejerce una fuerza de atracción sobre otra partícula con masa, y esta fuerza es proporcional al producto de sus masas e inversamente proporcional al cuadrado de la distancia que las separa. En el contexto de una simulación de dos cuerpos que se atraen gravitacionalmente (por ejemplo, dos planetas o estrellas), esta ley se traduce en una ecuación que describe cómo varía su aceleración a lo largo del tiempo debido a esa interacción.

\[ \vec{a}_i = G \cdot \frac{m_j (\vec{r}_j - \vec{r}_i)}{|\vec{r}_j - \vec{r}_i|^3} \]

En nuestro proyecto, esta ecuación fue implementada directamente en el código doscuerpos.py, dentro de la función que define el sistema de ecuaciones diferenciales. Específicamente, se calcula el vector que une ambos cuerpos, se obtiene la distancia entre ellos, y a partir de ello se evalúan las componentes de aceleración. Estas ecuaciones coinciden con la forma simplificada de las ecuaciones presentadas en el documento (Ecuación 1) para dos cuerpos sin influencia externa.

### Problema de Tres Cuerpos

Cuando se extiende el análisis a un sistema con tres cuerpos que interactúan entre sí mediante la fuerza gravitacional, la dinámica se vuelve significativamente más compleja. Cada cuerpo experimenta fuerzas de atracción gravitacional no sólo por uno, sino por los otros dos cuerpos simultáneamente.

La aceleración total que experimenta un cuerpo  𝑖 está dada por la suma de las aceleraciones individuales causadas por los otros cuerpos   𝑗  , tal como se expresa en la siguiente ecuación:

\[ \vec{a}_i = G \sum_{j \neq i} \frac{m_j (\vec{r}_j - \vec{r}_i)}{|\vec{r}_j - \vec{r}_i|^3} \]

Estas ecuaciones replican el modelo clásico Newtoniano para el sistema de tres cuerpos que se describe en el documento PDF, ecuación (1), con i, j, k siendo las permutaciones de los tres cuerpos.


En el archivo `trescuerpos.py`, estas ecuaciones se implementan explícitamente en la función `three_body_ode`, donde se calcula la fuerza neta que actúa sobre cada masa sumando las contribuciones individuales de las otras dos


---

## Implementación

- Lenguaje: Python 
- Bibliotecas: `numpy`, `matplotlib`, `scipy`
- Integrador numérico: `solve_ivp` de `scipy.integrate` con `rtol=1e-9`
- Visualización: Animaciones con `matplotlib.animation.FuncAnimation`

Los scripts se encuentran en:
- `doscuerpos.py`: simulación del sistema de dos cuerpos.
- `trescuerpos.py`: simulación del sistema de tres cuerpos.

---

## Resultados y Observaciones

### Dos Cuerpos
En la simulación de dos cuerpos, el comportamiento es bastante predecible. Ambos cuerpos giran en torno a un punto común llamado centro de masa, como si estuvieran “bailando” uno alrededor del otro. La forma de sus trayectorias es elíptica, lo cual tiene sentido, ya que según la teoría de Kepler y la ley de gravitación de Newton, los cuerpos que se atraen gravitacionalmente en el espacio suelen moverse en órbitas cónicas (elipses, circunferencias, parábolas o hipérbolas).

Durante toda la simulación, los cuerpos mantienen una distancia relativamente estable entre sí y no se alejan indefinidamente ni colisionan. Esto confirma que el sistema es estable y que la solución numérica que implementamos está funcionando correctamente. También se observa que la velocidad de cada cuerpo cambia ligeramente a lo largo de su trayectoria, lo cual es coherente con la conservación de la energía mecánica: los cuerpos se aceleran cuando se acercan entre sí y se desaceleran al alejarse.

### Tres Cuerpos
En el caso de los tres cuerpos, el panorama cambia completamente. Aunque las condiciones iniciales pueden parecer simples o incluso simétricas, el comportamiento del sistema se vuelve rápidamente impredecible. Los cuerpos comienzan moviéndose de forma ordenada, pero conforme pasa el tiempo, las trayectorias empiezan a volverse más caóticas. Esto significa que pequeños cambios en la posición o la velocidad de alguno de los cuerpos pueden generar trayectorias completamente diferentes.

En la animación se pueden ver momentos donde dos cuerpos se acercan mucho y el tercero parece alejarse, o incluso se forman estructuras en forma de lazo o espiral. A veces, parece que dos cuerpos “se alían” para formar una especie de órbita binaria mientras el tercero se va alejando, pero luego las interacciones cambian y todo el sistema se reorganiza.

Este tipo de comportamiento es típico en el problema de los tres cuerpos y fue uno de los primeros ejemplos de lo que hoy conocemos como sistemas caóticos. Justamente, en el documento teórico que usamos como base, se menciona que la dificultad del problema está en que las ecuaciones están acopladas: la aceleración de cada cuerpo depende de los otros dos al mismo tiempo (como lo indica el “segundo término” en la ecuación 5 del PDF), lo que hace que no se puedan resolver de forma exacta con una fórmula simple.

En resumen, la simulación refleja muy bien cómo un sistema tan sencillo en apariencia puede volverse increíblemente complejo, lo que lo hace fascinante tanto desde el punto de vista físico como computacional.

---

## Comparación con la Teoría

### Basado en el documento "The Three-Body Problem" (Frank, 2006):
- Las ecuaciones diferenciales que se implementaron en los scripts de Python están directamente inspiradas en las que aparecen en la sección 2 del documento. - Allí se explican las ecuaciones de movimiento newtonianas para tres cuerpos con masas arbitrarias, y cómo estas pueden expresarse como un sistema acoplado de ecuaciones vectoriales. Nuestro código traduce esa misma lógica a funciones que resuelven la aceleración neta sobre cada cuerpo sumando las fuerzas de los otros dos.

- En particular, los resultados de la simulación del sistema de tres cuerpos muestran comportamientos similares al problema pitagórico de Burrau, mencionado en la sección 5 del documento. Al igual que en ese caso, se observa que dos cuerpos pueden terminar atrapados en una órbita conjunta, mientras el tercero se aleja de forma caótica o incluso “escapa” del sistema, dependiendo de las condiciones iniciales.

- Todo esto refleja claramente el fenómeno de caos determinista que fue estudiado por Poincaré. Aunque el sistema es completamente determinista (sin azar involucrado), pequeñas diferencias en las condiciones iniciales generan trayectorias completamente diferentes. Esta sensibilidad al estado inicial es una de las principales características del comportamiento caótico, y es justamente lo que hace tan complejo e interesante el estudio del problema de los tres cuerpos.

---

## Comentarios del Código

- Las funciones `two_body_ode` y `three_body_ode` implementan las ecuaciones de aceleración basadas en la gravedad newtoniana.
- Las condiciones iniciales se eligen para evidenciar estabilidad (2 cuerpos) y caos (3 cuerpos).
- Se agregan márgenes dinámicos a los ejes para mantener visibles a los cuerpos durante la animación.

---

## Conclusiones
- Con la simulación del problema de dos cuerpos, pudimos ver claramente que el comportamiento es bastante estable y predecible. Los cuerpos siguen trayectorias elípticas como dice la teoría, y todo se comporta como uno esperaría según las leyes de Newton.

- Pero al pasar al problema de tres cuerpos, la cosa cambia totalmente. Aunque los valores iniciales parezcan simples, el sistema se vuelve caótico muy rápido. Es impresionante cómo con apenas un pequeño cambio en la posición o velocidad de uno de los cuerpos, todo el sistema se comporta distinto. Literalmente, no hay forma de predecir exactamente qué va a pasar a largo plazo.

- En general, este proyecto nos ayudó a entender mejor cómo funcionan estos sistemas desde el punto de vista físico y computacional. Verlo en código y animación lo hizo mucho más fácil de comprender que solo con fórmulas en papel. Además, nos dimos cuenta de lo potente que es usar herramientas como Python para estudiar fenómenos que, de otra forma, serían imposibles de resolver a mano.

---

## Referencias
- Frank, Juhan (2006). _The Three-Body Problem_. LSU Lecture Notes.
- SciPy Documentation: https://docs.scipy.org/
- Valtonen & Karttunen (2006). _The Three-Body Problem_. Cambridge University Press.
- El Problema de los Tres Cuerpos, una Visualización del CAOS del Cosmos:https://www.youtube.com/watch?v=427vNUBNguw 