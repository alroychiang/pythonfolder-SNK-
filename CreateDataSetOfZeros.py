import pandas as pd
import numpy as np

output_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\ones.csv"

# creating a dataframe full of zeros
feature_list = [",", "tickcount", "position(x)", "position(y)", "position(z)", "rotation(roll)", "rotation(pitch)", "rotation(yaw)", "linearVelocity(x)", "linearVelocity(y)", "linearVelocity(z)", "angularVelocity(x)", "angularVelocity(y)", "angularVelocity(z)"]
df = pd.DataFrame(1, index=np.arange(1000000), columns=feature_list) 
# print(df) 

df.to_csv(output_file_path, index=False)
print("Normalized data saved to: ", output_file_path)
print("")