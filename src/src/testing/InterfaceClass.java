package testing;

import java.util.stream.Stream;

public class InterfaceClass implements Testing2,Testing
{

	@Override
	public void method1(String str) {
		System.out.println("Chotu");
		Testing.logger("Test");
	}

	@Override
	public void method2(String str) {
		System.out.println("Motu");
	}

	@Override
	public void log(String str) {
	}
	
	public boolean isNull(String str) {
		System.out.println("Impl Null Check");
		return str == null ? true : false;
	}
	
	public static void main(String args[]){
		InterfaceClass obj = new InterfaceClass();
		obj.print("");
		obj.isNull("abc");

		Stream<Integer> stream = Stream.of(1,2,3,4);
		System.out.println(stream.count());
	}
	
	public static void test()
	{
		System.out.println("Do something");
	}
}
