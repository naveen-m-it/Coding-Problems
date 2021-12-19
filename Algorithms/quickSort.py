# Quick Sort
class QuickSort:
	def __init__(self,arr,low,high) -> None:
		self.arr = arr
		self.low = low
		self.high = high
		self.quickSort(arr,low,high)

	def partition(self,array, low, high):
		pivot = array[high]
		i = low - 1
		for j in range(low, high):
			if array[j] <= pivot:
				i = i + 1
				(array[i], array[j]) = (array[j], array[i])
		(array[i + 1], array[high]) = (array[high], array[i + 1])
		return i + 1
	
	def quickSort(self,array, low, high):
		if low < high:
			pi = self.partition(array, low, high)
			self.quickSort(array, low, pi - 1)
			self.quickSort(array, pi + 1, high)


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    low = 0
    high = len(arr)
    MergeSort(arr,low,high-1)
    for i in range(high):
        print(arr[i],end=" ")
    print()