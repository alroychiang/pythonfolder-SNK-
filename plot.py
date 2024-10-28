import pandas as pd
import matplotlib.pyplot as plt
import re

# remember to manually change the column heading in the raw csv file before executing this python file

# WEIGHTS = False
VARIABLES = True
WMDI = False
LOSS = False
FEATURE_PLOT = False

# if WEIGHTS == True:
#     # plot weights graph
#     # every 36 values is a tensor (1 iteration)
#     weightsdf = pd.read_csv(r'C:\Users\alroy.chiang\UEProjects\Saved\CubeData\Weights&Bias\Weights.csv')
#     plt.scatter(weightsdf["Index"], weightsdf["Weights"], label='NoFloorEulerWeights 36 values', color='blue', marker='o', s = 20)
#     plt.xlabel("Iteration Index Number (No. of times the model has been fed tensors)", fontdict=None, labelpad=None)
#     plt.ylabel("Weights", fontdict=None, labelpad=None)
#     plt.title("Weights changing over time")
#     plt.legend()
#     plt.show()


if VARIABLES == True:
    # plot bias graph
    # every 6 values is a tensor (1 iteration)
    ycol = 'weightsAndBiasMixed'
    vardf = pd.read_csv(f'C:\\Users\\alroy.chiang\\UEProjects\\Saved\\CubeData\\Weights&Bias\\{ycol}.csv')
    col = vardf.columns[1]
    plt.scatter(vardf["Index"], vardf[col], label= ycol, color='red', marker='x', s=20)
    plt.xlabel("idk actually", fontdict=None, labelpad=None)
    plt.ylabel("the value of the current variable i guess", fontdict=None, labelpad=None)
    plt.title("variable values right before the model is saved")
    plt.legend()
    plt.show()

# bias matrix divergence identity (for weights)
if WMDI == True:
    # plot BMDI graph
    WMDIdf = pd.read_csv(r'C:\Users\alroy.chiang\UEProjects\Saved\CubeData\Weights&Bias\EulerWeights.csv')
    col = WMDIdf.columns[1]
    plt.scatter(WMDIdf["Index"], WMDIdf[col], label='EulerWeight', color='red', marker='x', s=20)
    plt.xlabel("Iteration Index Number", fontdict=None, labelpad=None)
    plt.ylabel("Weight", fontdict=None, labelpad=None)
    plt.title("Weight changing over time")
    plt.legend()
    plt.show()


# Plot Loss vs Iteration
if LOSS == True:
    Lossdf = pd.read_csv(r'C:\Users\alroy.chiang\UEProjects\Saved\CubeData\LossCSVs\AngleAxisDataTrainingLoss.csv')
    col = Lossdf.columns[1]
    plt.scatter(Lossdf["Index"], Lossdf[col], label='Loss', color='red', marker='x', s=20)
    plt.xlabel("Iteration Index Number", fontdict=None, labelpad=None)
    plt.ylabel("Loss", fontdict=None, labelpad=None)
    plt.title("Loss changing over iteration")
    plt.legend()
    plt.show()
    

# Plot Feature value vs Iteration
if FEATURE_PLOT == True:
    filename = "PredictionCSVs\\InferencePredictionLVZ" # for inference
    Featuredf1 = pd.read_csv(f'C:\\Users\\alroy.chiang\\UEProjects\\Saved\\CubeData\\{filename}.csv')
    col1 = Featuredf1.columns[1]
    
    plt.scatter(Featuredf1["Index"], Featuredf1[col1], label=col1, color='red', marker='x', s=20)
    
    # Read the second CSV file and plot its data
    filename2 = "PredictionCSVs\\AngleAxisTrainingPredictionLVZ" # for training
    Featuredf2 = pd.read_csv(f"C:\\Users\\alroy.chiang\\UEProjects\\Saved\\CubeData\\{filename2}.csv")
    col2 = Featuredf2.columns[1]
    
    plt.scatter(Featuredf2["Index"], Featuredf2[col2], label=col2, color='blue', marker='o', s=20)
    
    # Set plot labels and title
    plt.xlabel("Iteration Index Number")
    plt.ylabel(f"{filename} vs {filename2}")
    plt.title("plot")
    plt.legend()
    
    # Show the plot
    plt.show()