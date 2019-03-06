package java.dataStructured;

public class DoublyLinkListClass {
	
	Node head = null,tail=null;
	
	class Node
	{
		Node prev;
		Node next;
		int data;
		
		public Node(int data)
		{
			this.data=data;
		}
	}
	
	public void addData(int data)
	{
		Node newnode = new Node(data);
		if(head==null)
		{
			head=newnode;
			tail=newnode;
			head.prev=null;
			tail.next=null;
		}
		else
		{
			tail.next=newnode;
			newnode.prev=tail;
			newnode=tail;
			tail.next=null;
		}
	}
	
	public void printData()
	{
		Node current = head;
		if(current==null)
			System.out.println("List is emplty");
		else
		{
			while(current!=null)
			{
				System.out.println(current.data);
				current=current.next;
			}
		}
			
	}
	
	public static void main(String[] args) {
		DoublyLinkListClass dl = new DoublyLinkListClass();
		dl.addData(10);
		dl.addData(20);
		dl.addData(30);
		dl.addData(40);
		dl.printData();
	}
}
