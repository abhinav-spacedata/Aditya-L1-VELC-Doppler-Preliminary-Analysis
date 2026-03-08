Aditya-L1-VELC-Solar-Corona-Analysis
# Aditya-L1 VELC Solar Corona Analysis

## Abstract
This project demonstrates a simplified solar spectroscopy analysis pipeline inspired by the Visible Emission Line Coronagraph (VELC) onboard the Aditya-L1 mission. The analysis focuses on coronal emission from the Fe XIV 530.3 nm spectral line to study plasma properties such as density, temperature proxies, and Doppler velocity signatures related to solar wind acceleration.

---

## Scientific Background
The solar corona is a highly dynamic plasma environment with temperatures exceeding 1–2 million Kelvin. Spectroscopic observations allow scientists to infer plasma properties using emission intensity, Doppler shifts, and spectral line broadening.

VELC observes the corona in the range of approximately **1.05–1.5 solar radii**.

---

## Mathematical Modelling

### Doppler Velocity
v = c (Δλ / λ₀)

Where:
- v = plasma velocity  
- c = speed of light  
- Δλ = wavelength shift  
- λ₀ = rest wavelength (530.3 nm)

### Coronal Emission
I ∝ ne²

Where:
- I = emission intensity  
- ne = electron density

### Temperature Proxy
Spectral line width relates to plasma temperature.

---

## Solar Wind Analysis Pipeline

VELC Spectral Data  
↓  
Spectral Image  
↓  
Radial Intensity Profile  
↓  
Coronal Brightness vs Height  
↓  
Spectral Line Width  
↓  
Doppler Velocity Model  
↓  
Solar Wind Velocity Map  
↓  
Solar Wind Acceleration

---

## Figures

![Spectral Image](figures/01_velc_spectral_image_fe14_530nm.png)

![Radial Intensity](figures/02_coronal_radial_intensity_profile.png)

![Coronal Brightness](figures/03_coronal_brightness_vs_height.png)

---

## Results
The analysis highlights spatial variations in coronal emission intensity and provides a simplified framework to interpret plasma dynamics using spectroscopic measurements.

---

## Future Work
- Real Doppler velocity extraction from spectral line centroid shifts  
- Multi-slit spectral reconstruction  
- Cross-analysis with Solar Orbiter and SOHO data
