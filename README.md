# Final_Project
# Data Quality in Digital Twin Systems

# Project Overview 
This project deals with Topic T4 of the COMP 331 project list. It explores the problems of ensuring good quality data synchronization between the physical and virtual sensors. With a Python-based simulation of a factory motor, the project determines and evaluates data quality dimensions like Completeness, Validity and Synchronization Consistency. 

# Problem Definition 
When using digital twins, the real world systems and their digital equivalents must be synchronized to prevent inaccuracies. In this project, special attention is paid to:
# Completeness: The sensor packets must be detected to complete the profiles of the data.
# Validity: Recording physically impossible values (e.g., negative RPM).
# Synchronization: Determining the "Sync Gap" or digital update lag between physical events and digital updates. 

# Project Structure 
The repository is sorted into the following scripts:

# generate_data.py: Generates 1,000 samples of motor data with induced quality problems (missing values and lags).
# analyze_data.py: Data profiling will be done to create quality summaries that are in CSV format.
# create_plots.py: Plots the synchronization gap between the physical and digital states. 

# Experimental Results 
The analysis yielded the following evidence of data quality problems:

# missingsummary.csv: Records 50 gaps in the temperature sensor data.

# invalidvaluecounts.csv: The invalid records are pointed out with 10 negative RPM records of the motor.

# sync gap chart.png: A graphical representation of a 5-degree temperature difference between the physical and virtual models that remained constant.  

# How to Run 
