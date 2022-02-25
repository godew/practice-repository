package boj;

import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String tmp = sc.nextLine();
		List<Integer> list = tmp.chars().map(x -> x - 48).boxed().collect(Collectors.toList());
		list.sort((a,b) -> b-a);
		list.stream().forEach(System.out::print);
		sc.close();
	}
}
