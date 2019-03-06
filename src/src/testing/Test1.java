package testing;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.concurrent.CopyOnWriteArrayList;
import javax.swing.plaf.synth.SynthScrollBarUI;

public class Test1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("This is sample test program now it is running...");
//		iteratMap();
//		list();
//		hashSet();
		collectionMethods();
	}

	
	public static void iteratMap()
	{
		HashMap<Integer, String> map = new HashMap<Integer,String>();
		map.put(1, "Athho");
		map.put(2, "Bobo");
		map.put(3, "Chucho");
		map.put(4, "Dobo");
		map.put(5, "Ego");
		map.put(6, "Faltu");
		
		map.forEach((k,v)-> System.out.println("Key : "+k+" - Val : "+v));
	}
	
	public static void list()
	{
		ArrayList<Integer> al = new ArrayList<Integer>();
		al.add(10);
		al.add(20);
		al.add(30);
		al.add(40);
		al.add(50);
		al.forEach(a->System.out.println(a));
	}
	
	public static void collectionMethods()
	{
//		List<String> lss = Collections.emptyList();
//		ls = Collections.unmodifiableList(ls);
		List<String> ls = new ArrayList<String>();
//		Collections.sort(ls, null);
		ls.add("Test");
		ls.add("Some");
		ls.forEach(l -> System.out.println(l));
		
		CopyOnWriteArrayList<String> cwal = new CopyOnWriteArrayList<String>(ls);
		Iterator<String> itr = cwal.iterator();
		while(itr.hasNext())
		{
			System.out.println(itr.next());
			cwal.add("Bug");
		}
	}
	
	public static void hashSet() {
//		HashSet set = new HashSet();
//		Hashtable table = new Hashtable();
//		table.put(null, null);
//		table.put(null, null);
//		table.put(null, null);
//		table.put(null, null);
//		set.add(1);
//		set.add(null);
//		set.add(null);
	}
}
