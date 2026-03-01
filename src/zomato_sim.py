import pandas as pd
import numpy as np
np.random.seed(42)
n_orders=500
true_kpt=np.random.normal(15,4,n_orders)
rider_arrival_delay=np.random.uniform(2,10,n_orders)
manual_for_signal=true_kpt+rider_arrival_delay
sensor_noise=np.random.normal(0,1.5,n_orders) 
proposed_signal=true_kpt+sensor_noise
df=pd.DataFrame({
    'True_KPT':true_kpt,
    'Manual_Button':manual_for_signal,
    'Proposed_Sensors':proposed_signal
})
df['Manual_Error']=abs(df['Manual_Button'] - df['True_KPT'])
df['Proposed_Error']=abs(df['Proposed_Sensors'] - df['True_KPT'])
print("--- Simulation Results (Minutes of Error) ---")
print(f"Average Error (Manual Button): {df['Manual_Error'].mean():.2f} mins")
print(f"Average Error (Proposed Sensors): {df['Proposed_Error'].mean():.2f} mins")
print(f"Improvement: {((df['Manual_Error'].mean() - df['Proposed_Error'].mean()) / df['Manual_Error'].mean())*100:.1f}%")