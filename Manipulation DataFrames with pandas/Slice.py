You have the following DataFrame df:

              eggs  salt  spam
apr portugal    44    18     5
    usa         36    95    63
feb france      93    56    10
    spain       67    20    88
jan england     90    33    93
    ireland     62    21    94
jun germany     96    75    79
    italy       52    99     7
mar china       83    43    19
    india        5     6    98
    

Code:
print(df.loc[(slice(None), 'ireland'),'spam'])

Output:
jan ireland 94
Name: spam, dtype: int64

