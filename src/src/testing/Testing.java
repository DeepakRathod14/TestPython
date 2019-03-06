package testing;

public interface Testing {

	void method1(String str);

	default void log(String str) {
		System.out.println("I1 logging::" + str);
	}
	
	static void logger(String s)
	{
		System.out.println(s);
	}
	
}
