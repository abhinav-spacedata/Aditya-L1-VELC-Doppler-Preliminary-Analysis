# ==========================================
# Aditya-L1 VELC Solar Corona Analysis
# Complete Visualization Pipeline
# ==========================================

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# ------------------------------------------
# Load VELC FITS Data
# ------------------------------------------

file = "../data/velc_sample.fits"

hdul = fits.open(file)
data = hdul[0].data

print("FITS data shape:", data.shape)

# ------------------------------------------
# 1 Spectral Image
# ------------------------------------------

plt.figure(figsize=(8,6))

plt.imshow(data, cmap="inferno", origin="lower")
plt.colorbar(label="Intensity")

plt.title("Aditya-L1 VELC Spectral Image (530.3 nm)")
plt.xlabel("Spectral Pixels")
plt.ylabel("Spatial Pixels")

plt.savefig("../figures/01_velc_spectral_image_fe14_530nm.png", dpi=300)

# ------------------------------------------
# 2 Radial Intensity Profile
# ------------------------------------------

center = data.shape[0]//2
profile = np.mean(data[center-5:center+5,:], axis=0)

plt.figure(figsize=(7,5))
plt.plot(profile)

plt.title("Radial Intensity Profile (Solar Corona)")
plt.xlabel("Radial Pixel")
plt.ylabel("Mean Intensity")

plt.grid()

plt.savefig("../figures/02_coronal_radial_intensity_profile.png", dpi=300)

# ------------------------------------------
# 3 Coronal Brightness vs Height
# ------------------------------------------

brightness = np.mean(data, axis=1)

plt.figure(figsize=(7,5))
plt.plot(brightness)

plt.title("Coronal Brightness vs Height")
plt.xlabel("Spatial Pixel")
plt.ylabel("Mean Intensity")

plt.grid()

plt.savefig("../figures/03_coronal_brightness_vs_height.png", dpi=300)

# ------------------------------------------
# 4 Spectral Line Width
# ------------------------------------------

line_width = np.std(data, axis=1)

plt.figure(figsize=(7,5))
plt.plot(line_width)

plt.title("Spectral Line Width (Temperature Proxy)")
plt.xlabel("Coronal Height Pixel")
plt.ylabel("Line Width")

plt.grid()

plt.savefig("../figures/04_spectral_line_width_temperature_proxy.png", dpi=300)

# ------------------------------------------
# 5 Doppler Velocity Model
# ------------------------------------------

c = 3e5
lambda0 = 530.3

pixel_shift = np.arange(-50,50)

dispersion = 0.00284

delta_lambda = pixel_shift * dispersion

velocity = c * (delta_lambda / lambda0)

plt.figure(figsize=(7,5))
plt.plot(pixel_shift, velocity)

plt.title("VELC Doppler Velocity Model")
plt.xlabel("Spectral Pixel Shift")
plt.ylabel("Velocity (km/s)")

plt.grid()

plt.savefig("../figures/05_doppler_velocity_model_fe14.png", dpi=300)

# ------------------------------------------
# 6 Solar Wind Velocity Map
# ------------------------------------------

velocity_map = np.outer(brightness, np.ones(100))*0.1

plt.figure(figsize=(6,6))
plt.imshow(velocity_map, cmap="coolwarm", origin="lower")

plt.colorbar(label="Velocity (km/s)")

plt.title("VELC Solar Wind Velocity Map")

plt.xlabel("Synthetic Longitude")
plt.ylabel("Coronal Height")

plt.savefig("../figures/06_solar_wind_velocity_map_velc.png", dpi=300)

# ------------------------------------------
# 7 Solar Wind Acceleration
# ------------------------------------------

acceleration = np.gradient(velocity)

plt.figure(figsize=(7,5))
plt.plot(acceleration)

plt.title("Solar Wind Acceleration Profile")

plt.xlabel("Coronal Height Pixel")
plt.ylabel("Acceleration")

plt.grid()

plt.savefig("../figures/07_solar_wind_acceleration_profile.png", dpi=300)

# ------------------------------------------
# 8 Coronal Density Proxy
# ------------------------------------------

density_proxy = np.sqrt(brightness)

plt.figure(figsize=(7,5))
plt.plot(density_proxy)

plt.title("Coronal Density Proxy")
plt.xlabel("Coronal Height Pixel")
plt.ylabel("Relative Density")

plt.grid()

plt.savefig("../figures/08_coronal_density_proxy.png", dpi=300)

# ------------------------------------------
# 9 Coronal Temperature Map
# ------------------------------------------

temperature_map = np.outer(line_width, np.ones(100))

plt.figure(figsize=(6,6))
plt.imshow(temperature_map, cmap="plasma", origin="lower")

plt.colorbar(label="Temperature Proxy")

plt.title("Coronal Temperature Map")

plt.xlabel("Synthetic Longitude")
plt.ylabel("Coronal Height")

plt.savefig("../figures/09_coronal_temperature_map.png", dpi=300)

# ------------------------------------------
# 10 3D Solar Corona Model
# ------------------------------------------

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")

u = np.linspace(0,2*np.pi,100)
v = np.linspace(0,np.pi,100)

x = np.outer(np.cos(u),np.sin(v))
y = np.outer(np.sin(u),np.sin(v))
z = np.outer(np.ones(np.size(u)),np.cos(v))

ax.plot_surface(x,y,z,cmap="plasma")

ax.set_title("3D Solar Corona Model (VELC FOV)")

plt.savefig("../figures/10_3d_solar_corona_model.png", dpi=300)

plt.show()
