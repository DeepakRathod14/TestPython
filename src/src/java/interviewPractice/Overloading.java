package java.interviewPractice;

public class Overloading {
	public static void main(String[] args) {
		Overloading l = new Overloading();
		l.a(10,10l);
	}
	
	public void a() throws Exception
	{
		System.out.println("Default method"); 
	}
	
	public void a(int i, long j)
	{
		System.out.println("INT "+i+j);
	}
	
	public int a(long a, int b)
	{
		System.out.println("LONG "+a+b);
		return 0;
	}
	
	public Overloading get() {return this;}
}
