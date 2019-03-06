package java.interviewPractice;

public class BClass extends AClass{

	public static void main(String[] args) {
		AClass a = new BClass();
		a.set(10);
		((BClass)a).get();
	}
	
	public void get() {System.out.println("B class method");}

	public void getB() {System.out.println("Own method");}
	
//	public void set(int i) {System.out.println("B-Class Set I val : "+i);}
}
