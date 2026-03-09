0# Aditya-L1 VELC Solar Corona Analysis

## Abstract

This project presents a simplified spectroscopic analysis pipeline inspired by the Visible Emission Line Coronagraph (VELC) instrument onboard the Aditya-L1 solar mission. The analysis focuses on the Fe XIV (530.3 nm) coronal emission line to investigate plasma properties in the solar corona.

The workflow demonstrates how spectroscopic observations can be used to analyze coronal emission intensity, plasma density variations, temperature proxies, Doppler velocity signatures, and solar wind acceleration trends.

The project includes visualization and analysis of coronal structures derived from VELC spectral data.

---

## Scientific Background

The solar corona is the outermost atmosphere of the Sun and exhibits extremely high temperatures reaching approximately **1–2 million Kelvin**. Understanding the corona is essential for explaining several fundamental solar phenomena including:

- coronal heating
- plasma dynamics
- solar wind origin

The **Visible Emission Line Coronagraph (VELC)** onboard **Aditya-L1** observes the solar corona between approximately **1.05 – 1.5 solar radii**.

VELC spectroscopy allows scientists to measure:

- coronal emission intensity  
- Doppler velocity of plasma  
- spectral line width (temperature proxy)  
- solar wind acceleration signatures  

One of the strongest coronal spectral lines observed by VELC is the **Fe XIV 530.3 nm emission line**, commonly referred to as the **green coronal line**.

---

## Mathematical Modelling

### Doppler Velocity

The Doppler shift of spectral lines allows estimation of plasma velocity.

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

Regions with higher emission intensity usually correspond to denser plasma structures.

---

### Temperature Proxy (Spectral Line Width)

Spectral line broadening can provide information about plasma temperature.

Δλ ∝ √(kT / m)

Where:

- Δλ = spectral line width  
- T = plasma temperature  
- m = ion mass

Broader spectral lines indicate higher thermal or non-thermal plasma motion.

---

### Solar Wind Acceleration

Solar wind acceleration can be estimated from velocity gradients.

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

# Figures and Observational Analysis

## 1. VELC Spectral Image

![Spectral Image](figures/01_velc_spectral_image_fe14_530nm.png)

This image represents the spatial and spectral intensity distribution of coronal emission recorded by VELC. Bright regions correspond to stronger coronal emission and typically indicate higher plasma density or active coronal structures.

---

## 2. Radial Intensity Profile

![Radial Intensity](figures/02_coronal_radial_intensity_profile.png)

The radial intensity profile illustrates how emission intensity varies along the radial direction of the solar corona. The decreasing intensity trend reflects the reduction of plasma density with increasing distance from the solar surface.

---

## 3. Coronal Brightness vs Height

![Coronal Brightness](figures/03_coronal_brightness_vs_height.png)

This plot shows the variation of coronal brightness with increasing height above the solar surface. The decrease in brightness confirms the gradual thinning of the coronal plasma.

---

## 4. Spectral Line Width (Temperature Proxy)

![Line Width](figures/04_spectral_line_width_temperature_proxy.png)

Spectral line width provides a proxy for estimating coronal plasma temperature. Broader spectral lines suggest higher thermal motion or turbulence within the corona.

---

## 5. Doppler Velocity Model

![Velocity](figures/05_doppler_velocity_model_fe14.png)

This model demonstrates the relationship between spectral pixel shift and Doppler velocity. Positive shifts represent redshift while negative shifts represent blueshift, indicating plasma motion along the line of sight.

---

## 6. Solar Wind Velocity Map

![Velocity Map](figures/06_solar_wind_velocity_map_velc.png)

This velocity map represents a simplified distribution of plasma flow within the VELC field of view. Such maps are useful for identifying potential solar wind source regions.

---

## 7. Solar Wind Acceleration Profile

![Acceleration](figures/07_solar_wind_acceleration_profile.png)

The acceleration profile shows how solar wind velocity changes with height in the corona. Increasing acceleration indicates outward plasma flow into interplanetary space.

---

## 8. Coronal Density Proxy

![Density](figures/08_coronal_density_proxy.png)

This plot represents the relative density distribution in the solar corona derived from emission intensity. Higher values correspond to denser plasma regions.

---

## 9. Coronal Temperature Map

![Temperature](figures/09_coronal_temperature_map.png)

The temperature map represents spatial variations in coronal temperature proxies derived from spectral line width measurements.

---

## 10. 3D Solar Corona Model

![3D Corona](figures/10_3d_solar_corona_model.png)

This 3D visualization illustrates a conceptual representation of the solar corona structure within the VELC field of view, highlighting the spatial extent of coronal plasma.

---

## Results

The analysis reveals several key characteristics of the solar corona:

- Coronal emission intensity decreases with increasing radial distance.
- Spectral line broadening suggests plasma temperatures of approximately 1–2 million Kelvin.
- Doppler velocity modelling demonstrates potential plasma outflows in the corona.
- Brightness and density variations indicate structured plasma distributions.

These results demonstrate how spectroscopic observations can provide insight into coronal plasma dynamics and solar wind formation.

---

## Visualizations

The repository includes visualization videos demonstrating the spectral analysis workflow and coronal structure interpretation.

Videos are available in the **videos/** directory.

---

## Conclusion

This project demonstrates a simplified solar spectroscopy analysis pipeline inspired by the Aditya-L1 VELC instrument.

The analysis highlights how spectroscopic measurements can be used to infer key coronal plasma properties including:

- emission intensity distribution
- plasma density variation
- temperature proxies
- Doppler velocity signatures
- solar wind acceleration trends

Such analysis pipelines form the basis of modern solar physics research.

---

## Future Work

Possible extensions of this project include:

- extracting Doppler velocity directly from spectral line centroids  
- performing Gaussian fitting of spectral lines  
- estimating coronal plasma density using emission diagnostics  
- comparison with **Solar Orbiter observations**  
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

git clone https://github.com/abhinav-spacedata/Aditya-L1-VELC-Solar-Corona-Analysis

Install dependencies

pip install -r requirements.txt

Run analysis

cd analysis  
python velc_coronal_analysis.py  

For multi-observation analysis:

python velc_multi_observation_analysis.py
