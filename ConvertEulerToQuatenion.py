import numpy as np
import pandas as pd
import math
# from scipy.spatial.transform import Rotation
import torch

def x_rotation_matrix(angle_rad):
    """
        Get X rotation matrix given X angle in radians
        Arguments:
            angle_rad (float): X rotation in radians
            device (device): device tensor is on
    """
    return torch.tensor([[1, 0, 0],
                        [0, math.cos(angle_rad), -math.sin(angle_rad)],
                        [0, math.sin(angle_rad), math.cos(angle_rad)]],
                        dtype=torch.float32)
 
 
def y_rotation_matrix(angle_rad):
    """
        Get Y rotation matrix given Y angle in radians
        Arguments:
            angle_rad (float): Y rotation in radians
            device (device): device tensor is on
    """
    return torch.tensor([[math.cos(angle_rad), 0, math.sin(angle_rad)],
                        [0, 1, 0],
                        [-math.sin(angle_rad), 0, math.cos(angle_rad)]],
                        dtype=torch.float32)
 
 
def z_rotation_matrix(angle_rad):
    """
        Get Z rotation matrix given Z angle in radians
        Arguments:
            angle_rad (float): Z rotation in radians
            device (device): device tensor is on
    """
    return torch.tensor([[math.cos(angle_rad), -math.sin(angle_rad), 0],
                        [math.sin(angle_rad), math.cos(angle_rad), 0],
                        [0, 0, 1]],
                        dtype=torch.float32)

# tensor input
def euler_to_rotation_matrix(radians_xyz):
    """
        Get rotation matrix given XYZ angles in radians
        Comments:
            radians_xyz (tensor): [X, Y, Z] angles in radians
            rotation order: XYZ (multiply Z first, then Y then X)
    """
    x_rotation = x_rotation_matrix(radians_xyz[0][0]) # putting rotX into X rotation matrix
    y_rotation = y_rotation_matrix(radians_xyz[0][1]) # ditto respectively
    z_rotation = z_rotation_matrix(radians_xyz[0][2])
 
    # multiply Z first, then Y then X. order XYZ
    rot_mat = torch.matmul(y_rotation, z_rotation)
    rot_mat = torch.matmul(x_rotation, rot_mat)
    return rot_mat

def rotmat2quat_torch(R):
    """
    Converts a rotation matrix to quaternion
    batch pytorch version ported from the corresponding numpy method above
    :param R: N * 3 * 3
    :return: N * 4
    """
    # this is numpy function
    rotdiff = R - R.transpose(1, 2)
    r = torch.zeros_like(rotdiff[:, 0])
    r[:, 0] = -rotdiff[:, 1, 2]
    r[:, 1] = rotdiff[:, 0, 2]
    r[:, 2] = -rotdiff[:, 0, 1]
    r_norm = torch.norm(r, dim=1)
    sintheta = r_norm / 2
    r0 = torch.div(r, r_norm.unsqueeze(1).repeat(1, 3) + 0.00000001)
    t1 = R[:, 0, 0]
    t2 = R[:, 1, 1]
    t3 = R[:, 2, 2]
    costheta = (t1 + t2 + t3 - 1) / 2
    theta = torch.atan2(sintheta, costheta)
    q = torch.zeros(R.shape[0], 4).float().to(R.device)
    q[:, 0] = torch.cos(theta / 2)
    q[:, 1:] = torch.mul(r0, torch.sin(theta / 2).unsqueeze(1).repeat(1, 3))
 
    return q

# all data collected is in radians
input_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\EulerRawData2.csv"
output_file_path = r"C:\Users\alroy.chiang\UEProjects\Saved\CubeData\QuatRawData2.csv"

print("Convert Euler To Quaternion has began running")

# Load your dataset from the CSV file
data = pd.read_csv(input_file_path)

# Extract Euler angles from the dataset
euler_angles = data[['rotation(roll)', 'rotation(pitch)', 'rotation(yaw)']].values

# empty data frame to be inserted into 'data' df to replace rotation (roll pitch yaw) columns with quart w, x, y, z
# List to store the quaternions for each Euler angle set [rotX, rotY, rotZ]
quaternions = []

# euler == Euler angle set [rotX, rotY, rotZ]
for euler in euler_angles:
    t = torch.tensor(euler)
    t = t.unsqueeze(0)
    rot_mat = euler_to_rotation_matrix(t)
    rot_mat = rot_mat.unsqueeze(0)
    q = rotmat2quat_torch(rot_mat) # single row quartenion (w, x, y, z ) i checked and double confirmed online calculator

    # converting tensor into numpy array
    q_numpyArr = q.numpy()
    
    # removing 1 dimension out from array
    q_numpyArr = np.squeeze(q_numpyArr)
    
    # add quarternion to 'quaternions' list
    quaternions.append(q_numpyArr)
    
    array_string = ' '.join(map(str, q_numpyArr))
    
    # print(array_string +" is being processed")

# i havent test this part out yet. it doesnt seem like it can convert till here.
# Create the DataFrame of Quartenion angles
quart_df = pd.DataFrame(quaternions, columns=['quaternion(w)', 'quaternion(x)', 'quaternion(y)', 'quaternion(z)'])

# Add quaternion columns to the original DataFrame
data = pd.concat([data, quart_df], axis=1)
data.drop(columns=['Unnamed: 0','rotation(roll)','rotation(pitch)','rotation(yaw)'], inplace=True)

# desired order
new_order = [ 
    "tickcount",
    "deltaseconds",
    "resetframe",
    "position(x)",
    "position(y)",
    "position(z)",
    "quaternion(w)",
    "quaternion(x)",
    "quaternion(y)",
    "quaternion(z)",
    "linearVelocity(x)",
    "linearVelocity(y)",
    "linearVelocity(z)",
    "angularVelocity(x)",
    "angularVelocity(y)",
    "angularVelocity(z)"]

data = data[new_order]

# Save the modified DataFrame
data.to_csv(output_file_path, index=False)

print('Euler To Quartenion script has completed running')
print('breakpoint')

# for testing only
# x, y, z = [angle * math.pi / 180 for angle in euler_angles[588, :]]

# # adding a new dimension just to fit into rotmat2quat_torch() function
# t = torch.tensor([x,y,z])
# t = t.unsqueeze(0)
# rot_mat = euler_to_rotation_matrix(t)
# rot_mat = rot_mat.unsqueeze(0)
# q = rotmat2quat_torch(rot_mat)

# print('breakpoint')