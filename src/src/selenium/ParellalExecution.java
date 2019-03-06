package selenium;

import org.testng.annotations.Optional;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class ParellalExecution {
	
	@Test
	@Parameters({"example1","example2"})
	public void test01(@Optional("Rathod") String ex1, String ex2)
	{
		System.out.println("Test-01 "+Thread.activeCount()); 
		System.out.println("Example1 = "+ex1);
		System.out.println("Example2 = "+ex2);
	}
	
	@Test
	public void test02()
	{
		System.out.println("Test-02 "+Thread.activeCount()); 
		
	}
	
	@Test
	public void test03()
	{
		System.out.println("Test-03 "+Thread.activeCount()); 
		
	}
}
