def solve(n,d,x):
	
	return
if __name__ == "__main__":
	t = int(input())
	for tc in range(t):
		n,d = map(int,input().split())
		x = list(map(int,input().split(maxsplit=n)))
		ans = solve(n,d,x)
		print(f"Case #{tc}: {ans}")