import numpy as np
import pandas as pd

def euler_to_rotation_matrix(euler_angles):
    # Extract individual angles
    roll = euler_angles[0]
    pitch = euler_angles[1]
    yaw = euler_angles[2]
    
    # Compute rotation matrices
    R_roll = np.array([[1, 0, 0],
                       [0, np.cos(roll), -np.sin(roll)],
                       [0, np.sin(roll), np.cos(roll)]])
    
    R_pitch = np.array([[np.cos(pitch), 0, np.sin(pitch)],
                        [0, 1, 0],
                        [-np.sin(pitch), 0, np.cos(pitch)]])
    
    R_yaw = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                      [np.sin(yaw), np.cos(yaw), 0],
                      [0, 0, 1]])
    
    # Combine rotation matrices
    R = np.dot(R_roll, np.dot(R_yaw, R_pitch))
    return R


input_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\EulerRawData.csv"
output_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\TwoBasisRawData.csv"

print("Conversion to 2BasisVector has started")

data = pd.read_csv(input_file_path)

# Convert Euler angles to rotation matrices and extract basis vectors
basis_vectors = []
for i, row in data.iterrows():
    # euler_angles are 3 values in a list.
    euler_angles = row[['rotation(roll)', 'rotation(pitch)', 'rotation(yaw)']].values
    rotation_matrix = euler_to_rotation_matrix(euler_angles)
    
    # return 3 values of x_basis vector. (extracts the 1st columns as a (3x1) vector). (1, 0, 0) is treated as a column vector.
    x_basis = np.dot(rotation_matrix, (1, 0, 0))
    # return 3 values of y_basis vector. (extracts the 2nd column as a (3x1) vector)
    y_basis = np.dot(rotation_matrix, (0, 1, 0))
    
    basis_vectors.append([*x_basis, *y_basis])
    
    print(f"X basis processed is:{x_basis}")

# Create DataFrame with basis vectors
columns = ['x_basis(X)', 'x_basis(Y)', 'x_basis(Z)', 
           'y_basis(X)', 'y_basis(Y)', 'y_basis(Z)']

basis_vectors_df = pd.DataFrame(basis_vectors, columns=columns)

# # Concatenate original data with basis vectors
# output_data = pd.concat([data, basis_vectors_df], axis=1)

data.insert(6, 'x_basis(X)', basis_vectors_df['x_basis(X)'])
data.insert(7, 'x_basis(Y)', basis_vectors_df['x_basis(Y)'])
data.insert(8, 'x_basis(Z)', basis_vectors_df['x_basis(Z)'])
data.insert(9, 'y_basis(X)', basis_vectors_df['y_basis(X)'])
data.insert(10, 'y_basis(Y)', basis_vectors_df['y_basis(Y)'])
data.insert(11, 'y_basis(Z)', basis_vectors_df['y_basis(Z)'])

data.drop(columns=['deltaseconds','rotation(roll)','rotation(pitch)','rotation(yaw)'], inplace=True)

data.to_csv(output_file_path, index=False)
print("2BasicVectors data saved to: ", output_file_path)
print("")

print("break point")