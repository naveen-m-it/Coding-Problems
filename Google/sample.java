class sample{
	static boolean binarySearch(int[] arr,int x){
		int low = 0;
		int high = arr.length-1;
		while (low<=high){
			int mid = low+(high-low)/2;
			if(arr[mid]==x){
				return true;
			}
			else if (arr[mid]<x) {
				low=mid+1;
			}
			else{
				high=mid-1;
			}
		}
		return false;

	}
	public static void main(String args[]){
		System.out.println("Hello Wolrd");
		String s1 = "Naveen";
		String s2 = "Naveen";
		int[] array ={1,2,3,4,5};
		int x = 6;
		System.out.println(binarySearch(array,x));
	}
}
