import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter

fig = plt.figure(figsize=(16, 8))
axes = [fig.add_subplot(2, 4, i+1, projection='3d') for i in range(8)]

# Use lower mesh resolution for speed, but keep quality
u = np.linspace(0, 2 * np.pi, 60)
v = np.linspace(0, np.pi, 30)
U, V = np.meshgrid(u, v)

# Animation update function
def update(frame):
    t = frame * 0.05
    # 1. Breathing fractal sphere
    ax = axes[0]
    ax.clear()
    R = 1 + 0.3 * np.sin(6 * U + t) * np.cos(4 * V + t) + 0.15 * np.sin(12 * U - 2 * t)
    X = R * np.cos(U) * np.sin(V)
    Y = R * np.sin(U) * np.sin(V)
    Z = R * np.cos(V)
    ax.plot_surface(X, Y, Z, cmap='Spectral', edgecolor='none')
    ax.set_title('Breathing Fractal Sphere')
    ax.set_axis_off()
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_zlim(-2, 2)

    # 2. Morphing torus-Möbius-wave
    ax = axes[1]
    ax.clear()
    t2 = (frame % 150) / 150.0
    w1 = np.abs(np.sin(np.pi * t2))
    w2 = np.abs(np.sin(np.pi * (t2 + 1/3)))
    w3 = np.abs(np.sin(np.pi * (t2 + 2/3)))
    wsum = w1 + w2 + w3
    w1 /= wsum; w2 /= wsum; w3 /= wsum
    X1 = (2 + np.cos(V)) * np.cos(U)
    Y1 = (2 + np.cos(V)) * np.sin(U)
    Z1 = np.sin(V)
    X2 = (1 + 0.5 * np.cos(U / 2) * np.sin(V) - 0.5 * np.sin(U / 2) * np.sin(2 * V)) * np.cos(U)
    Y2 = (1 + 0.5 * np.cos(U / 2) * np.sin(V) - 0.5 * np.sin(U / 2) * np.sin(2 * V)) * np.sin(U)
    Z2 = 0.5 * np.sin(U / 2) * np.sin(V) + 0.5 * np.cos(U / 2) * np.sin(2 * V)
    X3 = np.cos(U) * (2 + 0.5 * np.sin(3 * V + 2 * t2 * np.pi))
    Y3 = np.sin(U) * (2 + 0.5 * np.sin(3 * V + 2 * t2 * np.pi))
    Z3 = np.cos(V + 2 * t2 * np.pi)
    X = w1 * X1 + w2 * X2 + w3 * X3
    Y = w1 * Y1 + w2 * Y2 + w3 * Y3
    Z = w1 * Z1 + w2 * Z2 + w3 * Z3
    ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none')
    ax.set_title('Morphing Torus/Möbius/Wave')
    ax.set_axis_off()
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-2, 2)

    # 3. Twisting double helix surface
    ax = axes[2]
    ax.clear()
    X = np.cos(U) * (1 + 0.3 * np.sin(4 * V + t))
    Y = np.sin(U) * (1 + 0.3 * np.sin(4 * V + t))
    Z = V + 0.5 * np.sin(2 * U + t)
    ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')
    ax.set_title('Twisting Double Helix')
    ax.set_axis_off()
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_zlim(-1, 4)

    # 4. Animated gyroid
    ax = axes[3]
    ax.clear()
    X = np.sin(U + t) * np.cos(V + t)
    Y = np.sin(V + t) * np.cos(U + t)
    Z = np.sin(U + V + t)
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_title('Animated Gyroid')
    ax.set_axis_off()
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5); ax.set_zlim(-1.5, 1.5)

    # 5. Pulsating star surface
    ax = axes[4]
    ax.clear()
    R = 1 + 0.5 * np.sin(5 * U + t) * np.sin(3 * V + t)
    X = R * np.cos(U) * np.sin(V)
    Y = R * np.sin(U) * np.sin(V)
    Z = R * np.cos(V)
    ax.plot_surface(X, Y, Z, cmap='autumn', edgecolor='none')
    ax.set_title('Pulsating Star')
    ax.set_axis_off()
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_zlim(-2, 2)

    # 6. Animated Klein bottle projection
    ax = axes[5]
    ax.clear()
    X = (2 + np.cos(U / 2) * np.sin(V + t) - np.sin(U / 2) * np.sin(2 * V + t)) * np.cos(U)
    Y = (2 + np.cos(U / 2) * np.sin(V + t) - np.sin(U / 2) * np.sin(2 * V + t)) * np.sin(U)
    Z = np.sin(U / 2) * np.sin(V + t) + np.cos(U / 2) * np.sin(2 * V + t)
    ax.plot_surface(X, Y, Z, cmap='winter', edgecolor='none')
    ax.set_title('Animated Klein Bottle')
    ax.set_axis_off()
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-2, 2)

    # 7. Expanding/contracting hyperboloid
    ax = axes[6]
    ax.clear()
    X = np.cosh(V) * np.cos(U)
    Y = np.cosh(V) * np.sin(U)
    Z = np.sinh(V + 0.5 * np.sin(t))
    ax.plot_surface(X, Y, Z, cmap='cividis', edgecolor='none')
    ax.set_title('Expanding Hyperboloid')
    ax.set_axis_off()
    ax.set_xlim(-5, 5); ax.set_ylim(-5, 5); ax.set_zlim(-5, 5)

    # 8. Animated flower surface
    ax = axes[7]
    ax.clear()
    R = 1 + 0.4 * np.sin(8 * U + 4 * t) * np.cos(6 * V + 2 * t)
    X = R * np.cos(U) * np.sin(V)
    Y = R * np.sin(U) * np.sin(V)
    Z = R * np.cos(V)
    ax.plot_surface(X, Y, Z, cmap='spring', edgecolor='none')
    ax.set_title('Animated Flower')
    ax.set_axis_off()
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_zlim(-2, 2)

ani = FuncAnimation(fig, update, frames=120, interval=33, blit=False)
plt.tight_layout()

# Save animation as video (good quality, faster)
writer = FFMpegWriter(fps=30, metadata=dict(artist='You'), bitrate=2500)
print('Saving video, please wait...')
ani.save('eight_animations.mp4', writer=writer)
print('Video saved as eight_animations.mp4! You can now play it.')
# plt.show()  # Commented out to avoid backend issues when saving