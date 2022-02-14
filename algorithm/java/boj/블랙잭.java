package boj;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		sc.nextLine();
		int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::valueOf).toArray();
		int res = -1;
		for(int i = 0; i < n-2; i++) {
			for(int j = i+1; j < n-1; j++) {
				for(int k = j+1; k < n; k++) {
					int tmp = arr[i] + arr[j] + arr[k];
					if (tmp <= m) {
						res = Math.max(res, tmp);
					}
				}
			}
		}
		System.out.println(res);
		sc.close();
	}
}

