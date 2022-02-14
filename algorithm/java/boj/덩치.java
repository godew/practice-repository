package boj;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int idx = 0;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		ArrayList<ArrayList<Integer>> list = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			ArrayList<Integer> tmp = new ArrayList<Integer>();
			tmp.add(sc.nextInt());
			tmp.add(sc.nextInt());
			list.add(tmp);
		}
		
		int[] res = new int[list.size()];
		for (int i = 0; i < list.size()-1; i++) {
			for (int j = i + 1; j < list.size(); j++) {
				ArrayList<Integer> tmpi = list.get(i);
				ArrayList<Integer> tmpj = list.get(j);
				if (tmpi.get(0) > tmpj.get(0) && tmpi.get(1) > tmpj.get(1)) {
					res[j]++;
				} else if (tmpi.get(0) < tmpj.get(0) && tmpi.get(1) < tmpj.get(1)) {
					res[i]++;
				}
			}
		}
		
		Arrays.stream(res).forEach(x -> {
			if (idx < res.length - 1) {
				System.out.print(x+1 + " ");
			} else {
				System.out.print(x+1);
			}
			idx++;
		});
		sc.close();
	}
}
