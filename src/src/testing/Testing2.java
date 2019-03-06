package testing;

public interface Testing2 {

	void method2(String str);

	default void log(String str) {
		System.out.println("I1 logging::" + str);
	}
	
	static void logger(String s)
	{
		System.out.println(s);
	}
	
	default void print(String str) {
		if (!isNull(str))
			System.out.println("MyData Print::" + str);
	}

	static boolean isNull(String str) {
		System.out.println("Interface Null Check");

		return str == null ? true : "".equals(str) ? true : false;
	}
}
