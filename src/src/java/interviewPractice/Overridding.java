package java.interviewPractice;

public class Overridding extends Overloading{
	
	public void a() throws InterruptedException
	{
		Thread.sleep(1000);
		System.out.println("Overriding");
	}
	
	public void a(int i)
	{
		System.out.println(i);
	}
	
	public Overridding get() {return this;}
}
