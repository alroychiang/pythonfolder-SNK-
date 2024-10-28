import pandas as pd

# Specify the input and output file paths
input_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\EulerRawData.csv"
output_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\DataSetofOnes.csv"

print("Python script is activated")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_file_path)

# Keep the first three columns of data
first_two = df.iloc[:, :2]

remaining_df = df.iloc[:, 3:]

remaining_df = remaining_df.apply(lambda x: pd.Series([1] * len(x), index=x.index))

combined_df = pd.concat([first_two, remaining_df], axis=1)

print("Python script is finished")

# Write the new DataFrame to a CSV file
combined_df.to_csv(output_file_path, index=False)