n,q=map(int, input().split())
if n==1:
	n=n+1
for i in range(n,q):
	flag=0
	for j in range(2,i//2):
		if i%j==0:
			flag=1
			break
	if flag==0:
		print(i,end=' ')
