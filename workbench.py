import pandas as pd

df = pd.read_csv(r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\AxisAngleRawDataNormalized.csv")

# Filter the DataFrame to find rows where resetframe is 1
resetframe_ones = df[df['resetframe'] == 1]

# Extract and print the tickcount values corresponding to those rows
tickcount_values = resetframe_ones['tickcount']
tickcount_ones = set(tickcount_values)

if tickcount_values.empty:
    print("No tickcount values where resetframe is 1.")
else:
    print("Tickcount values where resetframe is 1:")
    print(tickcount_ones)