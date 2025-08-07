import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Constantes físicas
G = 1.0
m1 = 1.0
m2 = 1.0
m3 = 1.0

# Sistema de ecuaciones diferenciales para tres cuerpos
def three_body_ode(t, y):
    x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3 = y
    
    def compute_force(xa, ya, xb, yb, ma, mb):
        dx = xb - xa
        dy = yb - ya
        r = np.sqrt(dx**2 + dy**2) + 1e-10  # evitar división por cero
        F = G * ma * mb / r**2
        return F * dx, F * dy

    # Fuerzas sobre cada cuerpo
    fx12, fy12 = compute_force(x1, y1, x2, y2, m1, m2)
    fx13, fy13 = compute_force(x1, y1, x3, y3, m1, m3)
    fx21, fy21 = -fx12, -fy12
    fx23, fy23 = compute_force(x2, y2, x3, y3, m2, m3)
    fx31, fy31 = -fx13, -fy13
    fx32, fy32 = -fx23, -fy23

    # Aceleraciones
    ax1 = (fx12 + fx13) / m1
    ay1 = (fy12 + fy13) / m1
    ax2 = (fx21 + fx23) / m2
    ay2 = (fy21 + fy23) / m2
    ax3 = (fx31 + fx32) / m3
    ay3 = (fy31 + fy32) / m3

    return [
        vx1, vy1, vx2, vy2, vx3, vy3,
        ax1, ay1, ax2, ay2, ax3, ay3
    ]

# Condiciones iniciales: posiciones (x, y) y velocidades (vx, vy) de cada cuerpo
y0 = [
    -5.0, 0.0,     # x1, y1
     5.0, 0.0,     # x2, y2
     0.0, 8.66,    # x3, y3 (colocarlos formando un triángulo equilátero)
    0.5, 1.0,      # vx1, vy1
   -0.5, 1.0,      # vx2, vy2
    0.5, -1.0      # vx3, vy3
]

# Tiempo de simulación
t_span = (0, 500)
t_eval = np.linspace(*t_span, 5000)

# Resolver las ecuaciones
sol = solve_ivp(three_body_ode, t_span, y0, t_eval=t_eval, rtol=1e-9)

# Extraer posiciones
x1, y1 = sol.y[0], sol.y[1]
x2, y2 = sol.y[2], sol.y[3]
x3, y3 = sol.y[4], sol.y[5]

# ------------------- ANIMACIÓN -------------------
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid(True)
ax.set_title('Problema de los tres cuerpos')

# Trayectorias
trail1, = ax.plot([], [], 'b-', lw=1, label='Cuerpo 1')
trail2, = ax.plot([], [], 'r-', lw=1, label='Cuerpo 2')
trail3, = ax.plot([], [], 'g-', lw=1, label='Cuerpo 3')

# Cuerpos
body1, = ax.plot([], [], 'bo')
body2, = ax.plot([], [], 'ro')
body3, = ax.plot([], [], 'go')

def init():
    trail1.set_data([], [])
    trail2.set_data([], [])
    trail3.set_data([], [])
    body1.set_data([], [])
    body2.set_data([], [])
    body3.set_data([], [])
    return trail1, trail2, trail3, body1, body2, body3

def update(frame):
    if frame >= len(x1):
        return trail1, trail2, trail3, body1, body2, body3

    # Posiciones actuales
    x1_pos, y1_pos = x1[frame], y1[frame]
    x2_pos, y2_pos = x2[frame], y2[frame]
    x3_pos, y3_pos = x3[frame], y3[frame]

    # Actualizar trayectorias y cuerpos
    trail1.set_data(x1[:frame], y1[:frame])
    trail2.set_data(x2[:frame], y2[:frame])
    trail3.set_data(x3[:frame], y3[:frame])
    body1.set_data([x1_pos], [y1_pos])
    body2.set_data([x2_pos], [y2_pos])
    body3.set_data([x3_pos], [y3_pos])

    # Ajustar los límites del gráfico para que siempre se vean los cuerpos
    x_all = [x1_pos, x2_pos, x3_pos]
    y_all = [y1_pos, y2_pos, y3_pos]
    margin = 10
    ax.set_xlim(min(x_all) - margin, max(x_all) + margin)
    ax.set_ylim(min(y_all) - margin, max(y_all) + margin)

    return trail1, trail2, trail3, body1, body2, body3

# Control de velocidad
step = 10
ani = FuncAnimation(
    fig,
    update,
    frames=range(0, len(t_eval), step),
    init_func=init,
    blit=True,
    interval=100
)

plt.legend()
plt.show()
