Here is the DataFrame df:

           A
0  time.1.15
1  time.1.16
2  time.2.15
3  time.3.14

Code: df['new_col'] = df['A'].str.split('.').str.get(1)

Output:

          A new_col
0  time.1.15       1
1  time.1.16       1
2  time.2.15       2
3  time.3.14       3
