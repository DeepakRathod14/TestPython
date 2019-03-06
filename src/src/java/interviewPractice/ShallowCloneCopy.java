package java.interviewPractice;

class Test1 {
	int a=10;
	int b=10;
}

class Test2 implements Cloneable{
	int x=10;
	int y=10;
	
	Test1 t1 = new Test1();

	public Object clone() throws CloneNotSupportedException
	{
		return super.clone();
	}

}

public class ShallowCloneCopy {

	int id;
	String name;

	ShallowCloneCopy(int i, String n) {
		id = i;
		name = n;
	}

	ShallowCloneCopy(ShallowCloneCopy s) {
		id = s.id;
		name = s.name;
	}

	void display() {
		System.out.println(id + " " + name);
	}
	
	public static void main(String args[]) throws CloneNotSupportedException {
		
		ShallowCloneCopy s1 = new ShallowCloneCopy(111, "Deepak");
		ShallowCloneCopy s2 = new ShallowCloneCopy(s1);
		s1.display();
		s2.display();
		
		Test2 t2 = new Test2();
		t2.x=100;
		t2.y=200;
		t2.t1.a=500;
		t2.t1.b=1000;

		Test2 t22 = (Test2)t2.clone();
		t22.t1.a=10;
		t22.t1.b=20;
		t22.x=30;
		t22.y=40;
		System.out.println("-------- AFTER CLONE -------");
		System.out.println(t2.x);
		System.out.println(t22.x);
		System.out.println(t2.y);
		System.out.println(t22.y);
		System.out.println(t2.t1.a);
		System.out.println(t22.t1.a);
		System.out.println(t2.t1.b);
		System.out.println(t22.t1.b);
	}
}
