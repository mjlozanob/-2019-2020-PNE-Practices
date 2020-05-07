import re

text = 'msg=hi sisters%'

m = re.search('=(.+?)%', text)
print(m.group(1))