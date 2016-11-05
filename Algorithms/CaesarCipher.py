n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
tmp=[]
for c in s:
    val = ord(c)
    if (val >= 65 and val <=90):
        tmp.append(chr(65 + ((val-65+k) % 26)))
    elif (val >=97 and val <=122):
        tmp.append(chr(97 + ((val-97+k) % 26)))
    else:
        tmp.append(c)
print ''.join(tmp)
