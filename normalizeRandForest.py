from sklearn import preprocessing
import numpy as np

x_array = np.array([0.038, 0.017, 0.045, 0.012, 0.036, 0.098, 0.036, 0.042, 0.025, 0.130, 0.020, 0.053, 0.154, 0.052, 0.158, 0.064, 0.021])
normalized_arr = preprocessing.normalize([x_array])
print(normalized_arr)
