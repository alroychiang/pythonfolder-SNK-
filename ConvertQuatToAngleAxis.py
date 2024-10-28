import numpy as np
import pandas as pd

def quaternion_to_axisangle(quaternion, with_magnitude = False):
    if quaternion is None:
        return None
    theta = np.arccos(quaternion[0]) # taking 'w' omega value
    theta_s = np.sin(theta)
    if theta_s > 1e-3: # to ensure we dont divide by zero
        # takes i,j,k and divide by sin(theta) which 'normalizes' the vector part of the quaternion. 'u' is a unit vector
        u = [q/theta_s for q in quaternion[1:]] 
    else:
        u = [1,0, 0.0, 0.0]
    theta *= 2
    if with_magnitude: # returns a single column vector with 3 values 
        axis_angle = np.array(u, dtype=np.float32)*theta
    else: # returns a axis + angle(theta) separately
        axis_angle = np.array(u+[theta], dtype=np.float32)
    return axis_angle

input_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\QuatRawData2.csv"
output_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\AxisAngleRawData2.csv"

# Load your dataset from the CSV file
data = pd.read_csv(input_file_path)

# template dataframe
new_data = data[['tickcount', 'deltaseconds', 'resetframe', 'position(x)', 'position(y)', 'position(z)', 'linearVelocity(x)', 'linearVelocity(y)', 'linearVelocity(z)', 'angularVelocity(x)', 'angularVelocity(y)', 'angularVelocity(z)']]

# Computing angle_axis components and appending to the end of the dataframe on the right
new_data['axisAngleX'] = data.apply(lambda row: quaternion_to_axisangle([
    row['quaternion(w)'], row['quaternion(x)'], row['quaternion(y)'], row['quaternion(z)']
    ], with_magnitude=True)[0], axis=1)

new_data['axisAngleY'] = data.apply(lambda row: quaternion_to_axisangle([
    row['quaternion(w)'], row['quaternion(x)'], row['quaternion(y)'], row['quaternion(z)']
    ], with_magnitude=True)[1], axis=1)

new_data['axisAngleZ'] = data.apply(lambda row: quaternion_to_axisangle([
    row['quaternion(w)'], row['quaternion(x)'], row['quaternion(y)'], row['quaternion(z)']
    ], with_magnitude=True)[2], axis=1)

# Rearrange the columns in the desired order
new_data = new_data[['tickcount', 'deltaseconds', 'resetframe', 'position(x)', 'position(y)', 'position(z)', 'axisAngleX', 'axisAngleY', 'axisAngleZ',
                 'linearVelocity(x)', 'linearVelocity(y)', 'linearVelocity(z)', 'angularVelocity(x)', 'angularVelocity(y)', 'angularVelocity(z)']]

new_data.to_csv(output_file_path, index=False)