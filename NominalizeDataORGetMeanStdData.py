import pandas as pd
import numpy as np

# SWITCH (at any one point 1 of these must be true only)
GetNorminalizedData = True
GetMeanStdData = True
SAVE_OVERWRITE = True


input_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\AxisAngleRawData2.csv"

print("Norm and std dev conversion file has begun")

# main()
df = pd.read_csv(input_file_path)

temp = df.copy()
temp = temp.drop(labels = ["tickcount", "deltaseconds", "resetframe"], axis=1)
feature_means = temp.mean()
feature_std_devs = temp.std()

# converting series object to dataframe
mean_df = feature_means.to_frame(name = "Mean")
std_df = feature_std_devs.to_frame(name = "Std Dev")
mean_std_df = pd.concat([mean_df, std_df], axis=1)


# to check if any std_devs are value 0
# just print out 'feature_std_devs' itself. it shows every feature's respective std_devs. If no 0 means all good.
print("Feature_mean is: ", feature_means)
print("")
print("Feature_std_dev is: ", feature_std_devs)

# z-normalization
normalized_df = df.copy()
normalized_df.iloc[:, 3:] = (normalized_df.iloc[:, 3:] - feature_means) / feature_std_devs

if GetNorminalizedData == True:
    # getting normalized data csv file
    output_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\AxisAngleRawData2Normalized.csv"
    if SAVE_OVERWRITE == True:
        normalized_df.to_csv(output_file_path, index=False)
        print("Normalized data saved to: ", output_file_path)
        print("")

if GetMeanStdData == True:
    # getting mean and standard deviation csv files
    mean_std_filepath = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\MeanStdData\AxisAngleRawData2Mean&StdDevData.csv"
    if SAVE_OVERWRITE == True:
        mean_std_df.to_csv(mean_std_filepath, index = True)
        print("mean_std data saved to: ", mean_std_filepath)
        print("")