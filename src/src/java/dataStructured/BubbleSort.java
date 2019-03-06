package java.dataStructured;

import java.util.Arrays;
import java.util.Scanner;

public class BubbleSort {
	public static void main(String[] args) {
		bubbleSort();
	}

	public static void bubbleSort() {
		int arr[] = { 101, 56, 78, 6, 9, 0, 165, 4 };
		int n=arr.length;
		for (int i = 0; i < n - 1; i++) {
			System.out.println(" I Starting : "+i+ " -> End : "+(n-1));
			for (int j = 0; j < n - i - 1; j++) {
				System.out.println(" J Starting : "+j+ " -> End : "+(n-i-1));
				System.out.println("arr[j] > arr[j + 1]  : "+arr[j] +">"+ arr[j + 1]);
				if (arr[j] > arr[j + 1]) {
					// swap temp and arr[i]
					int temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
				}
			}
		}
		
		for (int i = 0; i < arr.length; i++)
			System.out.println(arr[i]);
	}

	// Starting from 0 index then compare it with next index,
	// if next index is less then then copy its possition and compare next iteration
	// with then possition value till end of loop.
	public static void selectionSort() {
		int a[] = { 101, 56, 78, 6, 9, 0, 165, 4 };
		for (int i = 0; i < a.length - 1; i++) {
			int temp = a[i];
			int pos = 0;
			for (int j = i + 1; j < a.length; j++) {
				if (a[j] < temp) {
					pos = j;
					temp = a[j];
				}
			}
			int higherVal = a[i];
			a[i] = a[pos];
			a[pos] = higherVal;
		}

		for (int i : a)
			System.out.println(i);
	}

	public static void binarySearch() {
		int[] a = { 10, 9, 7, 101, 23, 44, 12, 78, 34, 23 };
		Arrays.sort(a);
		int beg = 0;
		Scanner sc = new Scanner(System.in);
		int searchItem = sc.nextInt();
		int possition = bSearch(a, beg, (a.length - 1), searchItem);
		System.out.println("Search Item Possition is " + possition);
		System.out.println("Search Item Value is : " + a[possition - 1]);
	}

	private static int bSearch(int[] a, int beg, int end, int searchItem) {
		if (end >= beg) {
			int mid = (beg + end) / 2;
			if (a[mid] == searchItem) {
				return mid + 1;
			} else if (a[mid] < searchItem) {
				return bSearch(a, mid++, end, searchItem);
			} else if (a[mid] > searchItem) {
				return bSearch(a, beg, mid--, searchItem);
			}
		}
		return -1;
	}

	public static void correctBubbleSort() {
		int[] a = { 10, 9, 7, 101, 23, 44, 12, 78, 34, 23 };
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				System.out.println("a[i] < a[j] : " + a[i] + a[j]);
				if (a[i] < a[j]) {
					int temp = a[i];
					System.out.println("temp : " + temp);
					a[i] = a[j];
					a[j] = temp;
					System.out.println(a.toString());
				}
			}
		}
		System.out.println("Printing Sorted List ...");
		for (int i = 0; i < 10; i++) {
			System.out.println(a[i]);
		}
	}
}
