You have the following DataFrame df:

  Month  Count
0   Jan     52
1   Apr     29
2   Mar     46
3   Feb      3


Scipt:
print(df.loc[df['Month'] == 'Feb'])

Output:
Month Count
3 Feb 3
