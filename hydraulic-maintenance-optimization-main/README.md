# Hydraulic Solutions Maintenance Optimization

## Business Problem:

The core objective of this project is to minimize downtime and curb maintenance costs within hydraulic solutions. The endeavor addresses these challenges through the development of a robust predictive model with advanced condition monitoring. The ultimate goal is to provide actionable insights that optimize maintenance schedules by predicting failures and enhance the reliability of the hydraulic system.

## Dataset Overview:

The dataset, obtained from a hydraulic test rig, comprises sensor data from a primary working and a secondary cooling-filtration circuit. The system cyclically repeats load cycles, measuring process values such as pressures, volume flows, and temperatures. Four hydraulic components (cooler, valve, pump, and accumulator) have varying conditions quantitatively assessed. The dataset includes raw process sensor data structured as matrices, and annotations for target conditions are provided in 'profile.txt'.

## Data Details:

- **Sensor Types:**
  - Pressure sensors (PS1-PS6)
  - Motor power sensor (EPS1)
  - Volume flow sensors (FS1, FS2)
  - Temperature sensors (TS1-TS4)
  - Vibration sensor (VS1)
  - Virtual sensors for cooling efficiency (CE), cooling power (CP), and efficiency factor (SE)

- **Target Conditions (annotated in 'profile.txt'):**
  - Cooler condition (%)
  - Valve condition (%)
  - Internal pump leakage
  - Hydraulic accumulator (bar)
  - Stable flag indicating the stability of conditions

## Project Goals:

Develop a robust predictive model to:
- Minimize downtime in hydraulic solutions.
- Curb maintenance costs through advanced condition monitoring.
- Optimize maintenance schedules by predicting failures.
- Enhance the overall reliability of the hydraulic system.

## Requirements:
- Python 3.x
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

## Clone the repository:
git clone https://github.com/tokinsey/portfolio/edit/main/hydraulic-maintenance-optimization-main

## Navigate to the project directory: 
cd hydraulic-maintenance-optimization

## Contributing 
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments 
The project relies on open datasets provided by UCI Machine Learning Repository for analysis. Special thanks to them for making the data publicly available.

## Contact 
For any inquiries or feedback, please reach out.

Happy analyzing!
