You have the following DataFrame df:

  Month  Count
0   Jan     52
1   Apr     29
2   Mar     46
3   Feb      3

Code:
print(df.loc[df['Count'] == 46])

Output:
Month Count
0 Mar 46
