import pandas as pd

df = pd.read_csv('motor_data.csv')

# 1. Check for Missing Values (Completeness)
missing = df.isnull().sum()
missing.to_csv('missingsummary.csv')

# 2. Check for Negative RPM (Validity)
invalid = df[df['Machine_RPM'] < 0]
invalid.to_csv('invalidvaluecounts.csv')

# 3. Check for Sync Lag (Consistency)
df['Sync_Error'] = abs(df['Physical_Sensor'] - df['Digital_Twin'])
df[['Timestamp', 'Sync_Error']].to_csv('sync_analysis.csv', index=False)

print("Step 2 Complete: Analysis CSV files created!")