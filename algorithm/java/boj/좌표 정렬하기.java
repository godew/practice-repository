package boj;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
	
	static class Coordinate {
		int x;
		int y;
		
		public Coordinate(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		ArrayList<Coordinate> list = new ArrayList<>();
		
		for (int i = 0; i < n; i++) {
			list.add(new Coordinate(sc.nextInt(), sc.nextInt()));
		}
		
		Collections.sort(list, (a, b) -> {
			if (a.x == b.x){
				return a.y - b.y;
			} else {
				return a.x - b.x;
			}
		});
		
		for (Coordinate c : list) {
			System.out.println(c.x + " " + c.y);
		}
		sc.close();
	}
}
