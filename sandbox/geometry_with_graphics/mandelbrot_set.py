# Jim McCleery, September 2024
# Fast Mandelbrot set with smooth colorful shading
# Black background, bright colors, no title, no color bar

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Image resolution
# Larger values give a sharper image, but take more computation.
# ------------------------------------------------------------
WIDTH = 1400
HEIGHT = 1400

# ------------------------------------------------------------
# Maximum number of iterations
# Points that do not escape after this many steps are treated
# as belonging to the Mandelbrot set.
# ------------------------------------------------------------
MAX_ITER = 300

# ------------------------------------------------------------
# Viewing window in the complex plane
# This is the standard full Mandelbrot view.
# ------------------------------------------------------------
RE_MIN, RE_MAX = -2.2, 1.0
IM_MIN, IM_MAX = -1.6, 1.6

# ------------------------------------------------------------
# Create a rectangular grid of complex numbers:
# C = x + iy
# ------------------------------------------------------------
real = np.linspace(RE_MIN, RE_MAX, WIDTH)
imag = np.linspace(IM_MIN, IM_MAX, HEIGHT)
Re, Im = np.meshgrid(real, imag)
C = Re + 1j * Im

# ------------------------------------------------------------
# Start with z = 0 for every point in the grid.
# smooth will hold smooth escape values for coloring.
# mask keeps track of points that have not yet escaped.
# ------------------------------------------------------------
Z = np.zeros_like(C, dtype=np.complex128)
smooth = np.zeros(C.shape, dtype=float)
mask = np.ones(C.shape, dtype=bool)

# ------------------------------------------------------------
# Iterate z = z^2 + c
# For points that escape, compute a smooth escape-time value:
#
#     nu = n + 1 - log(log|z|)/log(2)
#
# This removes harsh color banding and gives smooth transitions.
# ------------------------------------------------------------
for n in range(MAX_ITER):
    Z[mask] = Z[mask] * Z[mask] + C[mask]

    escaped_now = np.abs(Z) > 2
    newly_escaped = escaped_now & mask

    if np.any(newly_escaped):
        abs_z = np.abs(Z[newly_escaped])
        smooth[newly_escaped] = n + 1 - np.log(np.log(abs_z)) / np.log(2)

    mask[newly_escaped] = False

# ------------------------------------------------------------
# Points that never escaped are considered inside the set.
# Give them the value 0 so they can be colored black.
# ------------------------------------------------------------
smooth[mask] = 0

# ------------------------------------------------------------
# Plot the Mandelbrot set
# "turbo" gives very bright, vivid colors.
# Setting vmin=1 helps keep the interior black.
# ------------------------------------------------------------
plt.figure(figsize=(10, 10), facecolor="black")
plt.imshow(
    smooth,
    extent=[RE_MIN, RE_MAX, IM_MIN, IM_MAX],
    origin="lower",
    cmap="turbo",
    vmin=1
)

# Remove axes and extra border for a clean image
plt.axis("equal")
plt.axis("off")
plt.gca().set_facecolor("black")
plt.tight_layout(pad=0)

plt.show()
