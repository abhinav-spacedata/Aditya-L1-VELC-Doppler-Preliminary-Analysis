# ==========================================
# VELC Multi Observation Analysis
# ==========================================

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import os

data_folder = "../data"

files = [
    "velc_2024_01_16.fits",
    "velc_2024_01_29.fits"
]

for file in files:

    file_path = os.path.join(data_folder, file)

    print("Processing:", file)

    hdul = fits.open(file_path)
    data = hdul[0].data

    # Spectral Image
    plt.figure(figsize=(8,6))

    plt.imshow(data, cmap="inferno", origin="lower")
    plt.colorbar(label="Intensity")

    plt.title(f"VELC Spectral Image ({file})")

    plt.xlabel("Spectral Pixels")
    plt.ylabel("Spatial Pixels")

    save_name = file.replace(".fits","")

    plt.savefig(f"../figures/{save_name}_spectral.png", dpi=300)


    # Radial Intensity

    center = data.shape[0]//2

    profile = np.mean(data[center-5:center+5,:], axis=0)

    plt.figure(figsize=(7,5))

    plt.plot(profile)

    plt.title(f"Radial Intensity Profile ({file})")

    plt.xlabel("Radial Pixel")
    plt.ylabel("Mean Intensity")

    plt.grid()

    plt.savefig(f"../figures/{save_name}_radial_intensity.png", dpi=300)


    # Coronal Brightness

    brightness = np.mean(data, axis=1)

    plt.figure(figsize=(7,5))

    plt.plot(brightness)

    plt.title(f"Coronal Brightness vs Height ({file})")

    plt.xlabel("Spatial Pixel")
    plt.ylabel("Mean Intensity")

    plt.grid()

    plt.savefig(f"../figures/{save_name}_brightness.png", dpi=300)


plt.show()

print("Multi observation analysis complete")
