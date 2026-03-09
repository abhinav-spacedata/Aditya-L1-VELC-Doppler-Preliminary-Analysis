# Aditya-L1 VELC Solar Corona Analysis

## Abstract

This project presents a simplified spectroscopic analysis pipeline inspired by the Visible Emission Line Coronagraph (VELC) instrument onboard the Aditya-L1 mission. The study focuses on coronal emission from the Fe XIV (530.3 nm) spectral line and demonstrates how spectroscopic measurements can be used to investigate plasma properties in the solar corona.

The analysis includes spectral image visualization, radial intensity profiling, coronal brightness analysis, spectral line width estimation, Doppler velocity modelling, and solar wind acceleration interpretation.

---

## Scientific Background

The solar corona is the outermost atmosphere of the Sun and is characterized by extremely high temperatures (~1–2 million Kelvin). Understanding coronal plasma dynamics is essential for explaining coronal heating and the origin of the solar wind.

The **Visible Emission Line Coronagraph (VELC)** onboard **Aditya-L1** observes the solar corona between approximately **1.05 – 1.5 solar radii**.

VELC spectroscopy allows measurements of:

- coronal emission intensity  
- plasma velocity through Doppler shift  
- spectral line width (temperature proxy)  
- solar wind acceleration signatures  

One of the most prominent coronal spectral lines observed by VELC is the **Fe XIV 530.3 nm emission line**, also known as the **green coronal line**.

---

## Mathematical Modelling

### Doppler Velocity

The Doppler shift of a spectral line can be used to estimate plasma velocity.

v = c (Δλ / λ₀)

Where:

- v = plasma velocity  
- c = speed of light  
- Δλ = wavelength shift  
- λ₀ = rest wavelength (530.3 nm)

---

### Coronal Emission

Coronal emission intensity depends on electron density.

I ∝ nₑ²

Where:

- I = emission intensity  
- nₑ = electron density

Higher intensity generally indicates regions with higher plasma density.

---

### Temperature Proxy (Spectral Line Width)

Spectral line broadening provides an estimate of plasma temperature.

Δλ ∝ √(kT / m)

Where:

- Δλ = spectral line width  
- T = plasma temperature  
- m = ion mass

Broader spectral lines typically indicate higher temperature plasma.

---

### Solar Wind Acceleration

Solar wind acceleration can be approximated from velocity gradients.

a = dv / dr

Where:

- a = acceleration  
- v = velocity  
- r = radial distance from the Sun

---

## Solar Wind Analysis Pipeline

VELC FITS Spectral Data  
↓  
Spectral Image Visualization  
↓  
Radial Intensity Profile  
↓  
Coronal Brightness vs Height  
↓  
Spectral Line Width Analysis  
↓  
Doppler Velocity Modelling  
↓  
Solar Wind Velocity Mapping  
↓  
Solar Wind Acceleration Estimation  

---

## Figures

### VELC Spectral Image

![Spectral Image](figures/01_velc_spectral_image_fe14_530nm.png)

---

### Radial Intensity Profile

![Radial Intensity](figures/02_coronal_radial_intensity_profile.png)

---

### Coronal Brightness vs Height

![Brightness](figures/03_coronal_brightness_vs_height.png)

---

### Spectral Line Width

![Line Width](figures/04_spectral_line_width_temperature_proxy.png)

---

### Doppler Velocity Model

![Velocity](figures/05_doppler_velocity_model_fe14.png)

---

### Solar Wind Velocity Map

![Velocity Map](figures/06_solar_wind_velocity_map_velc.png)

---

### Solar Wind Acceleration

![Acceleration](figures/07_solar_wind_acceleration_profile.png)

---

## Results

The analysis reveals spatial variations in coronal emission intensity along the spectrograph slit.

Key observations:

- Coronal brightness decreases with increasing radial distance.  
- Spectral line broadening indicates hot plasma regions in the corona.  
- Doppler velocity modelling demonstrates how spectral pixel shifts correspond to plasma motion.  
- Brightness profiles suggest variations in coronal plasma density.  

These results illustrate how spectroscopic measurements can be used to study plasma dynamics in the solar corona.

---

## Visualizations

The repository also includes visualization videos demonstrating the analysis workflow and coronal structure interpretation.

Videos are available in the **videos/** directory.

---

## Conclusion

This project demonstrates a simplified solar spectroscopy analysis pipeline inspired by the Aditya-L1 VELC instrument.

The study highlights how spectroscopic data can be used to infer important coronal plasma properties including:

- emission intensity  
- density variations  
- temperature proxies  
- plasma velocity  
- solar wind acceleration  

Such analysis pipelines form the basis of modern solar physics research.

---

## Future Work

Possible extensions of this work include:

- extracting Doppler velocity directly from spectral line centroids  
- performing multi-slit spectral reconstruction  
- estimating coronal plasma density using emission diagnostics  
- comparison with **Solar Orbiter** observations  
- cross-analysis with **SOHO coronagraph data**

---

## Repository Structure

Aditya-L1-VELC-Solar-Corona-Analysis

analysis/  
   velc_coronal_analysis.py  
   velc_multi_observation_analysis.py  

data/  
   velc_sample.fits  

figures/  
   analysis plots  

videos/  
   visualization videos  

docs/  
   research notes  

README.md  
requirements.txt  
LICENSE  

---

## How to Run

Clone the repository

git clone https://github.com/YOUR_USERNAME/Aditya-L1-VELC-Solar-Corona-Analysis

Install dependencies

pip install -r requirements.txt

Run analysis

cd analysis  
python velc_coronal_analysis.py  

For multi-observation analysis:

python velc_multi_observation_analysis.py
