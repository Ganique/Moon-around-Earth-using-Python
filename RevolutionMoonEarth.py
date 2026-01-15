import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# ALL THE NUMERICAL VALUES(EQUATOR RADIUS, POLAR RADIUS AND DISTANCES) WERE TAKEN IN KILOMETRES THEN THEY WERE DIVIDED BY 1000 FOR DISPLAY REASONS

equator_RX = 6.3781370
equator_RY = 6.3781370
polar_R   = 6.357
radius_X = radius_Y = radius_Z = 1.7374
earthDmoon = 384.4
def earth(equator_RX, equator_RY, polar_R, n=100):
    # Paramètres angulaires
    u = np.linspace(0, 2*np.pi, n)   # longitude
    v = np.linspace(0, np.pi, n)     # colatitude

    U, V = np.meshgrid(u, v)

    # Coordonnées ellipsoïdales
    X = equator_RX * np.sin(V) * np.cos(U)
    Y = equator_RY * np.sin(V) * np.sin(U)
    Z = polar_R   * np.cos(V)

    return X, Y, Z

def moon(radius_X, radius_Y, radius_Z, n=100):
    # Paramètres angulaires
    u = np.linspace(0, 2*np.pi, n)   # longitude
    v = np.linspace(0, np.pi, n)     # colatitude

    U, V = np.meshgrid(u, v)

    # Coordonnées ellipsoïdales
    X =  radius_X* np.sin(V) * np.cos(U)
    Y =  radius_Y* np.sin(V) * np.sin(U)
    Z =  radius_Z* np.cos(V)

    return X, Y, Z
# In order to show the animation of Moon and Earth, we ARBITRAIRLY choose the distance moon-earth to 38.44. If we take 384.4 as the distance moon-earth, we will not see the animation.
def revolution(t, R_orbit=38.44, omega_orbit=0.1): #omega_orbit is the angular velocity of moon around the earth. The real value of the angular velocity of the Moon around the Earth is closed to 0.000003106 rad/s. If we take 0.000003106 rad/s as the angular velocity, the Moon will take more than 23 days to turn around the Earth.
    a, b = 1, 0.75 #The trajectory of Moon around the Earth is globally elliptical. a is the half major axis and b is the half small axis.
    x = a*R_orbit * np.cos(omega_orbit * t)
    y = b*R_orbit * np.sin(omega_orbit * t)
    z = 0
    return x, y, z


# Temps
dt = 0.5

# Objets
Xm, Ym, Zm = moon(radius_X, radius_Y, radius_Z)
X0, Y0, Z0 = earth(equator_RX, equator_RY, polar_R)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_zlim(-40, 40)
ax.set_box_aspect([1,1,1])

def update(frame):
    ax.cla() # clear the axes

    t = frame * dt

    # === Sphère centrale ===
    ax.plot_surface(X0, Y0, Z0, color='blue', alpha=0.9)


    # === Révolution orbitale de la lune ===
    tx, ty, tz = revolution(t)

    Xt = Xm + tx
    Yt = Ym + ty
    Zt = Zm + tz

    ax.plot_surface(Xt, Yt, Zt, color='grey', alpha=0.8)

    # In order to show the animation of Moon and Earth, we ARBITRARILY choose the distance moon earth to 38.44. If we take 384.4 as the distance moon-earth, we will not see the animation.
    ax.scatter(tx, ty, tz, color='black', s=38.44)

    ax.set_title(f"Revolution - Moon around Earth — t = {t:.2f}")
    ax.set_xlim(-40, 40)
    ax.set_ylim(-40, 40)
    ax.set_zlim(-40, 40)
    ax.set_box_aspect([1,1,1])

ani = FuncAnimation(fig, update, frames=300, interval=50)
plt.show()

