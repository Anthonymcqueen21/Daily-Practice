The following code has been run:

import pandas as pd
list_keys = ['Country', 'Total']
list_values = [['United States', 'Soviet Union', 'United Kingdom'], [1118, 473, 273]]

Script:
zipped = list(zip(list_keys, list_values))
data = dict(zipped)
df = pd.DataFrame(data)
print(df.head())

Output:
     Country Total
0 United States 1118
1 Soviet Union 473
2 United Kingdom 273
