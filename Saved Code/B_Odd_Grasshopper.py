for q in range(int(input())):
	a, b = map(int, input().split())
	for i in range(((b // 4) * 4 + 1),b+1):
		a = a-i if a%2==0 else a+i
	print(a)