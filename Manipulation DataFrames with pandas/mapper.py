You have the following DataFrame df:

       eggs  salt  spam
month                  
jan      47  12.0    17
feb     110  50.0    31
mar     221  89.0    72
apr      77  87.0    20
may     132   0.0    52
jun     205  60.0    55

Code:
mapper = {True: 'high', False: 'low'}
df['new'] = (df['eggs'] > 100).map(mapper)
print(df)s

Output:

       eggs  salt  spam   new
month                        
jan      47  12.0    17   low
feb     110  50.0    31  high
mar     221  89.0    72  high
apr      77  87.0    20   low
may     132   0.0    52  high
jun     205  60.0    55  high
