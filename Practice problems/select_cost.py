import numpy as np
store = np.array(["X","X","Y","Z","Z])
cost = np.array([7, 8, 3, 7, 7])
select_cost = cost[store != "X"]
print(select_cost)

output: [3 7 7]
