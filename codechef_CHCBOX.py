for _ in range(int(input())):
	n = int(input())
	w = list(map(int, input().split()))
	max_val = max(w)
	lf = []
	l = []
	for i in w:
		if i < max_val:
			l.append(i)
		else:
			lf.append(len(l))
			l = []
	lf[0] += len(l)
	n = n//2
	count = 0
	print(lf)
	for k in lf:
		c = k - n + 1
		c = max(c,0)
		count += c
	print(count)
