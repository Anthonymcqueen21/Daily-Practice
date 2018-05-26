Data Frame
MONTH  day  year     session_id
a     JAN    7  2015       17357
b     FEB    8  2015       10011

for i, q in loginx.iterows():
    logins.loc[i,'month'] = q['MONTH'].lower()
print(logins)

output: 
MONTH  day  year  session_id Month
a   JAN    7  2015       17357   jan
b   FEB    8  2015       10011   feb
