import glob
import os
import numpy as np
parent_directory = './'
directory_name_pattern = '*'
matching_subdirectories = glob.glob(os.path.join(parent_directory, directory_name_pattern))

for subdir_path in matching_subdirectories:
    for file_name in os.listdir(subdir_path):
        if file_name.endswith('.npy'):
            npy_file_path = os.path.join(subdir_path, file_name)
            
            d = np.load(npy_file_path)

            # Extract columns from the loaded data
            q = d[:, 7:11]
            t = d[:, 0]
            w = d[:, 1:4]
            a = d[:, 4:7]
            V = d[:, -3:]

            # Calculate time differences
            difft = np.diff(t)

            # Define the time step
            dt = 5000 * 10**(-6)

            # Rearrange the quaternion columns
            q = q[:, [3, 0, 1, 2]]
            
            dV = a*dt + np.array([0, 0, -9.80665])*dt
            dVdt = dV / dt
            
            
            # Create a new file name for the result
            result_file_name = file_name.replace('.npy', '_velocity.npy')
            result_file_path = os.path.join(subdir_path, result_file_name)
            
            # Save the result as a new .npy file
            np.save(result_file_path, mean_value)
            
            # Print the result file path or do further processing
            print(f"Result saved as {result_file_path}")
            