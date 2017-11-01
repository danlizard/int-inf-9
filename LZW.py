S = input()
X = []
for i in range(0, len(S)):
    if S[i] not in X:
        X.append(S[i])
cd = ''
a=''
for i in range(0, len(S)):
	a += S[i]
	if a not in X:
		X.append(a)
		if i == len(S):
			cd += str(S.index(a))
			break
		cd += str(S.index(a[:-1]))
		a = a[-1]
print(*X)
print(cd)
input()