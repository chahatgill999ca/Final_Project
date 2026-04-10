import pandas as pd
import numpy as np

# Create 1000 records of motor data
df = pd.DataFrame({
    # CHANGE 'S' TO 's' HERE 👇
    'Timestamp': pd.date_range(start='2026-04-10', periods=1000, freq='s'),
    'Physical_Sensor': np.random.normal(70, 2, 1000), 
    'Digital_Twin': np.random.normal(70, 2, 1000),   
    'Machine_RPM': np.random.randint(1000, 5000, 1000)
})

# Add Quality Issues
df.loc[0:49, 'Physical_Sensor'] = np.nan  
df['Digital_Twin'] = df['Physical_Sensor'] + 5 
df.loc[990:999, 'Machine_RPM'] = -1       

df.to_csv('motor_data.csv', index=False)
print("Step 1 Complete: motor_data.csv created!")