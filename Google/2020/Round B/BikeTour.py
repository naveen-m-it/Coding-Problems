def solve(n,h):
	count = 0
	start = h[0]
	peak = 0
	for i in range(1,n):
		if h[i]>start and peak<=h[i]:
			if peak<h[i]:
				count=1
				peak=h[i]
			else:
				peak = h[i]
				count+=1
	return count
if __name__ == "__main__":
	t = 1
	for tc in range(t):
		n = int(input())
		h = list(map(int,input().split()))
		ans = solve(n,h)
		print(f"Case #{tc+1}: {ans}")