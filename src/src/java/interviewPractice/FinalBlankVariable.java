package java.interviewPractice;

public class FinalBlankVariable {

	int id;  
	String name;  
	final String COLLAGE;
	static final String PAN_CARD_NUMBER;
	
	static {PAN_CARD_NUMBER="AKNPRP";}
	
	public FinalBlankVariable(int id, String name, String collage)
	{
		this.id=id;
		this.name=name;
		COLLAGE=collage;
	}
	
	public static void main(String[] args) {
		final int i;
		i=20;
		System.out.println(i);
	}
	
	public void test()
	{
		final int i;
		i=10;
		System.out.println(i);
	}
	
	public void test2(final int i)
	{
		System.out.println(i);
//		System.out.println(i++);
	}
}
