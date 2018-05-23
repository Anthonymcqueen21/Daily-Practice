This is the DataFrame df:

         class  test1  test2
name                        
Jasmine      1     92     62
Martin       2     56     34
Nick         1     11     32
Sarah        2     12     45

 
Code: print(df.reset_index())


Output:    name  class  test1  test2
0  Jasmine      1     92     62
1   Martin      2     56     34
2     Nick      1     11     32
3    Sarah      2     12     45
