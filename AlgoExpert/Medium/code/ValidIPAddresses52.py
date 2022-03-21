def validIPAddresses(string):
    # Write your code here.
	validIpList = []
	buildIp = ['','','','']
    for i in range(1, min(len(string),4)):
		buildIp[0] = string[:i]
		if not isValid(buildIp[0]):
			continue
		
		for j in range(i+1, min(len(string),i+4)):
			buildIp[1] = string[i:j]
			if not isValid(buildIp[1]):
				continue
			for k in range(j+1, min(len(string),j+4)):
				buildIp[2] = string[j:k]
				buildIp[3] = string[k:]
				if not isValid(buildIp[2]):
					continue
				if not isValid(buildIp[3]):
					continue
				validIpList.append('.'.join(buildIp))
	return validIpList
	
def isValid(string):
	if int(string) > 255:
		return False
	else:
		return len(str(int(string))) == len(str(string))