The string recipe = 'I need 10 strawberries and 2 apples. 'is in the environment

import re
print(re.findall("\d+[a-z]+',recipe))

output: ['10 strawberries', '2 apples']
