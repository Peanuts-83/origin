import numpy as np

north = np.array([14,12,3,20])
east = np.array([9,5,23,10])
south = np.array([60,42,36,90])
west = np.array([23,28,91,73])

stores_matrix = np.concatenate((north,east,south,west), axis=0)
stores_matrix = stores_matrix.reshape(4,4)
# ou:
stores_matrix = np.vstack([north, east, south, west])
prices = np.array([1.5,4.25,6.0,25.99])

revenu = [sum(stores_matrix[n]*prices) for n in range(len(stores_matrix))]
# ou:
revenu = stores_matrix @ prices

print(stores_matrix @ prices)
print(sum(stores_matrix @ prices))
