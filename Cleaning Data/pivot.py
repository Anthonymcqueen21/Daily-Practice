Here is a preview of the DataFrame df:

   class     name  test1  test2
0      1     Nick     11     32
1      2    Sarah     12     45
2      1  Jasmine     92     62
3      2   Martin     56     34


print(df.pivit_table(index = ['class']))

output:

       test1  test2
class              
1       51.5   47.0
2       34.0   39.5
