import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('motor_data.csv')
df['Sync_Error'] = abs(df['Physical_Sensor'] - df['Digital_Twin'])

plt.figure(figsize=(10,5))
plt.plot(df['Timestamp'][:100], df['Physical_Sensor'][:100], label='Physical Motor')
plt.plot(df['Timestamp'][:100], df['Digital_Twin'][:100], label='Digital Twin', linestyle='--')
plt.title('Synchronization Gap: Physical vs Digital')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sync_gap_chart.png')
print("Step 3 Complete: Graph saved as sync_gap_chart.png!")