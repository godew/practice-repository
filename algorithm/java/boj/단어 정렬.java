package boj;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		HashSet<String> set = new HashSet<String>();
		for (int i = 0; i < n; i++) {
			set.add(sc.next());
		}
		
		ArrayList<String> res = new ArrayList<String>(set);
		
		Collections.sort(res, (a,b) -> {
			if (a.length() == b.length()) {
				return a.compareTo(b);
			} else {
				return a.length() - b.length();
			}
		});
		
		res.stream().forEach(System.out::println);
		sc.close();
	}
}
