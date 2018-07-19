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
df.index = df.index.str.replace('jan', 'JAN')
print(df)

Output:
eggs  salt  spam
month                  
JAN      47  12.0    17
feb     110  50.0    31
mar     221  89.0    72
apr      77  87.0    20
may     132   0.0    52
jun     205  60.0    55
