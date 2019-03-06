package java.dataStructured;

import java.util.Arrays;
import java.util.Scanner;

public class AlgorithamClass {

	public static void main(String[] args) {
		int a[]= {15,8,69,1,63,4,100,3,00,786,2};
//		bubbleSort(a);
//		selectionSort(a);
//		quickSort(a);
		binarySearch(a);
	}

	public static void binarySearch(int a[])
	{
		Arrays.sort(a);
		for(int i : a) System.out.print(i+" , ");
		int min,max,position,item;
		min=0;max=a.length;position=-1;
		item= new Scanner(System.in).nextInt();
		position = binarySearchPerform(a,min,max,item);
		System.out.println("Position -> "+position);
	}
	
	private static int binarySearchPerform(int[] a, int min, int max, int item)
	{
		int mid,position=-1;
		if(max>=min)
		{
			mid=(min+max)/2;
			if(a[mid]==item)
			{
				return mid+1;
			}
			else if(a[mid]>item)
			{
				return binarySearchPerform(a, min, mid-1, item);
			}
			else if(a[mid]<item)
			{
				return binarySearchPerform(a, mid+1, max, item);
			}
		}
		return position;
	}
	
	public static void quickSort(int[] a)
	{
		sort(a,0,a.length-1);
		for(int i:a)System.out.println(i);
	}
	
	private static void sort(int[] a, int min, int max)
	{
		if(min < max)
		{
			int pos = partition(a, min, max);
			
			sort(a, min, pos-1);
			sort(a,pos+1,max);
		}
	}
	
	private static int partition(int a[], int min, int max)
	{
		int index = min-1;
		int pivot = a[max];
		
		for(int i=min;i<max;i++)
		{
			if(a[i]<pivot)
			{
				index++;
				int temp = a[index];
				a[index]=a[i];
				a[i]=temp;
			}
		}
		int temp = a[index+1];
		a[index+1]=a[max];
		a[max]=temp;
		return index+1;
	}
	
	public static void selectionSort(int[] a)
	{
		System.out.println("------ Start Selection Sort ------");
		for(int i=0;i<a.length;i++)
		{
			int pos=0;
			int temp=a[i];
			for(int j=i;j<a.length;j++)
			{
				if(temp>a[j])
				{
					pos=j;
					temp=a[j];
				}
			}
			if(pos!=0) {
				temp=a[i];
				a[i]=a[pos];
				a[pos]=temp;
			}
		}
		for(int i:a)System.out.println(i);
	}
	
	public static void bubbleSort(int[] a)
	{
		System.out.println("----- Start Bubble Sort -----");
		for(int i=0;i<a.length-1;i++)
		{
			for(int j=0;j<(a.length-i-1);j++)
			{
				if(a[j]>a[j+1])
				{
					int temp = a[j+1];
					a[j+1]=a[j];
					a[j]=temp;
				}
			}
		}
		for(int i:a)System.out.println(i); 
	}
}
