import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Constantes físicas
G = 1.0  
m1 = 1.0  
m2 = 1.0  


def two_body_ode(t, y):
    """
    Sistema de ecuaciones diferenciales que modela la interacción gravitacional
    entre dos cuerpos puntuales en dos dimensiones.
    
    Parámetros:
    - t: tiempo (requerido por solve_ivp aunque no se usa directamente)
    - y: vector de estado [x1, y1, x2, y2, vx1, vy1, vx2, vy2]
    
    Retorna:
    - Derivadas de las posiciones y velociaddes:
      [dx1/dt, dy1/dt, dx2/dt, dy2/dt, dvx1/dt, dvy1/dt, dvx2/dt, dvy2/dt]
    """
    x1, y1, x2, y2, vx1, vy1, vx2, vy2 = y

    # Vector distancia entre los cuerpos
    dx = x2 - x1
    dy = y2 - y1
    r = np.sqrt(dx**2 + dy**2)  # distancia euclideana

    # Fuerza gravitacional
    F = G * m1 * m2 / r**2

    # Aceleraciones (segunda ley de Newton)
    ax1 =  F * dx / m1
    ay1 =  F * dy / m1
    ax2 = -F * dx / m2
    ay2 = -F * dy / m2

    return [vx1, vy1, vx2, vy2, ax1, ay1, ax2, ay2]


#Condiciones iniciales
y0 = [-5.5, 0.7,     
       0.5, 0.6,     
      -2.0, -1.0,    
       1.0,  1.0]  

# Intervalo de tiempo de simulación
t_span = (0, 50000)
t_eval = np.linspace(*t_span, 50000)

# ecuaciones diferenciales resuletas
sol = solve_ivp(two_body_ode, t_span, y0, t_eval=t_eval, rtol=1e-9)

# Extraer las posiciones de cada cuerpo a lo largo del tiempo
x1 = sol.y[0]
y1 = sol.y[1]
x2 = sol.y[2]
y2 = sol.y[3]

#Animacion
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-500, 500)
ax.set_ylim(-500, 500)
ax.grid(True)
ax.set_title('Problema de los dos cuerpos')

# Trayectorias
trail1, = ax.plot([], [], 'b-', lw=1, label='Cuerpo 1')
trail2, = ax.plot([], [], 'r-', lw=1, label='Cuerpo 2')

# Representación de los cuerpos como puntos
body1, = ax.plot([], [], 'bo')
body2, = ax.plot([], [], 'ro')

def init():
    """
    Inicializa los elementos graficos vacíos para la animación.
    """
    trail1.set_data([], [])
    trail2.set_data([], [])
    body1.set_data([], [])
    body2.set_data([], [])
    return trail1, trail2, body1, body2

def update(frame):
    """
    Actualiza la posicion y trayectoria de los cuerpos para cada cuadro de animacion.
    
    Parámetros:
    - frame: indice del cuadro (paso temporal)
    """
    if frame >= len(x1):
        return trail1, trail2, body1, body2

    # Posiciones actuales
    x1_pos = x1[frame]
    y1_pos = y1[frame]
    x2_pos = x2[frame]
    y2_pos = y2[frame]

    # Actualización de trayectorias y puntos
    trail1.set_data(x1[:frame], y1[:frame])
    trail2.set_data(x2[:frame], y2[:frame])
    body1.set_data([x1_pos], [y1_pos])
    body2.set_data([x2_pos], [y2_pos])

    # Autoajuste de los límites de visualización para que siempre se vean ambos cuerpos
    x_min = min(x1_pos, x2_pos)
    x_max = max(x1_pos, x2_pos)
    y_min = min(y1_pos, y2_pos)
    y_max = max(y1_pos, y2_pos)
    margin = 100  # margen visual

    ax.set_xlim(x_min - margin, x_max + margin)
    ax.set_ylim(y_min - margin, y_max + margin)

    return trail1, trail2, body1, body2


# Control de velocidad: salta varios frames para que sea más rápida
step = 10
ani = FuncAnimation(
    fig,
    update,
    frames=range(0, len(t_eval), step),
    init_func=init,
    blit=True,
    interval=50  # ms entre cuadros
)

plt.legend()
plt.show()