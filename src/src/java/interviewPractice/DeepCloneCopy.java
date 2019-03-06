package java.interviewPractice;

class Test3 {
	int a=10;
	int b=10;
}

class Test4 implements Cloneable{
	int x=10;
	int y=10;
	
	Test3 t1 = new Test3();

	public Object clone() throws CloneNotSupportedException
	{
		Test4 t = (Test4)super.clone();
		t.t1 = new Test3();
		return t;
	}

}

public class DeepCloneCopy {

	int id;
	String name;

	DeepCloneCopy(int i, String n) {
		id = i;
		name = n;
	}

	DeepCloneCopy(DeepCloneCopy s) {
		id = s.id;
		name = s.name;
	}

	void display() {
		System.out.println(id + " " + name);
	}
	
	public static void main(String args[]) throws CloneNotSupportedException {
		
		DeepCloneCopy s1 = new DeepCloneCopy(111, "Deepak");
		DeepCloneCopy s2 = new DeepCloneCopy(s1);
		s1.display();
		s2.display();
		
		Test4 t2 = new Test4();
		t2.x=100;
		t2.y=200;
		t2.t1.a=500;
		t2.t1.b=1000;

		Test4 t22 = (Test4)t2.clone();
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
