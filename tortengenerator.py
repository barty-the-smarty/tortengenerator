import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse

# ==========================================
# Einstellungen
# ==========================================

NUM_SLICES = 13 # Anzahl der Tortenstücke
NUM_LEAVES = 8  # Anzahl der Blätter an den Röschen
RADIUS = 1.0

# ==========================================
# Zeichenfläche
# ==========================================

fig, ax = plt.subplots(figsize=(8,8))
ax.set_aspect("equal")
ax.set_xlim(-1.15, 1.15)
ax.set_ylim(-1.15, 1.15)
ax.axis("off")

# Hintergrund
fig.patch.set_facecolor("white")

# ==========================================
# Tortenboden
# ==========================================

cake = Circle(
    (0,0),
    RADIUS,
    facecolor="#F8E8D0",
    edgecolor="black",
    linewidth=3
)

ax.add_patch(cake)

# ==========================================
# Zuckerrand
# ==========================================

for i in range(NUM_SLICES*8):
    a = math.radians(i * 360 / (NUM_SLICES*8))
    x = 0.95*math.cos(a)
    y = 0.95*math.sin(a)

    ax.add_patch(
        Circle(
            (x,y),
            0.025,
            facecolor="white",
            edgecolor="#DDDDDD",
            linewidth=0.5
        )
    )

# ==========================================
# Schnitte
# ==========================================

for i in range(NUM_SLICES):

    angle = math.radians(i * 360 / NUM_SLICES)

    x = RADIUS * math.cos(angle)
    y = RADIUS * math.sin(angle)

    ax.plot(
        [0,x],
        [0,y],
        color="black",
        linewidth=1.2
    )

# Mittelpunkt

ax.add_patch(
    Circle(
        (0,0),
        0.01,
        color="black"
    )
)

# ==========================================
# Röschen
# ==========================================

rose_radius = 0.78

for i in range(NUM_SLICES):

    angle = math.radians((i+0.5) * 360 / NUM_SLICES)

    x = rose_radius * math.cos(angle)
    y = rose_radius * math.sin(angle)

    # Blätter

    #for offset in (-25,25):
    for l in range (NUM_LEAVES):

        offset = math.radians(l * 360 / NUM_LEAVES)
        a = angle + offset
        
        lx = x + 0.06*math.cos(a)
        ly = y + 0.06*math.sin(a)

        leaf = Ellipse(
            (lx,ly),
            width=0.11,
            height=0.05,
            angle=math.degrees(a),
            facecolor="#4CAF50",
            edgecolor="#2E7D32",
            linewidth=0.5
        )

        ax.add_patch(leaf)

    # Rose außen

    ax.add_patch(
        Circle(
            (x,y),
            0.065,
            facecolor="#FF8FB1",
            edgecolor="#B03060",
            linewidth=1
        )
    )

    # Rose innen

    ax.add_patch(
        Circle(
            (x,y),
            0.045,
            facecolor="#FFC0D5",
            edgecolor="#B03060",
            linewidth=0.6
        )
    )

    # Spirale

    xs=[]
    ys=[]

    for t in range(100):
        r=0.00045*t
        phi=t*0.35
        xs.append(x+r*math.cos(phi))
        ys.append(y+r*math.sin(phi))

    ax.plot(xs,ys,color="#B03060",linewidth=0.7)

# ==========================================
# Anzeigen
# ==========================================

plt.show()
