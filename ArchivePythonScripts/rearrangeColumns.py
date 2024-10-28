import pandas as pd

input_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\TwoBasisRawDataNormalized.csv"
output_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\TwoBasisRawDataNormalized.csv"

# Load the CSV file into a DataFrame
data = pd.read_csv(input_file_path)

# Rearrange the columns in the desired order
# new_data = data[['Unnamed: 0', 'tickcount', 'position(x)', 'position(y)', 'position(z)', 'axisAngleX', 'axisAngleY', 'axisAngleZ', 'linearVelocity(x)', 'linearVelocity(y)', 'linearVelocity(z)', 'angularVelocity(x)', 'angularVelocity(y)', 'angularVelocity(z)']]

data = data.drop('deltaseconds', axis=1)

# Save the rearranged DataFrame to a new CSV file
data.to_csv(output_file_path, index=False)