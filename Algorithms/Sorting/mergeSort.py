# Merge Sort
class MergeSort:
	def __init__(self,arr,low,high):
		self.arr = arr
		self.low = low
		self.high = high
		self.mergeSort(arr,low,high)

	def mergeSort(self,arr,low,high):
		if low<high:
			mid = low+(high-low)//2
			self.mergeSort(arr,low,mid)
			self.mergeSort(arr,mid+1,high)
			self.sort(arr,low,mid,high)

	def sort(self,arr,low,mid,high):
		n1 = mid-low+1
		n2 = high-mid
		L = [0]*n1
		R = [0]*n2
		for i in range(n1):
			L[i] = arr[low+i]
		for j in range(n2):
			R[j] = arr[mid+1+j]
		i=0
		j=0
		k=low
		while i<n1 and j<n2:
			if L[i]<R[j]:
				arr[k] = L[i]
				i+=1
			else:
				arr[k]=R[j]
				j+=1
			k+=1
		while i<n1:
			arr[k]=L[i]
			i+=1
			k+=1
		while j<n2:
			arr[k]=R[j]
			j+=1
			k+=1


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    low = 0
    high = len(arr)
    MergeSort(arr,low,high-1)
    for i in range(high):
        print(arr[i],end=" ")
    print()