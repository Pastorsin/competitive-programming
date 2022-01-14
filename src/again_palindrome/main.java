/*
Java v1.8.0_151

https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1558
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;

class Main {

    public static long calculateCost(String word) {
        int N = word.length();
        long[][] DP = new long[N][N];

        // Base case
        // The cost of one character is 1
        for (int i = 0; i < N; i++) {
            DP[i][i] = 1;
        }

        for (int size = 1; size < N; size++) {
            for (int start = 0; start < N - size; start++) {
                int end = start + size;

                if (word.charAt(start) == word.charAt(end)) {
                    // Consider the middle because the extremes are the same
                    // (S[start+1..end] + S[start..end-1] - S[start+1..end-1])
                    // +
                    // (S[start+1..end-1] + 1)
                    DP[start][end] = DP[start + 1][end] + DP[start][end - 1] + 1;
                } else {
                    // Not considering the middle because the extremes are different
                    // and contains repeated characters
                    DP[start][end] = DP[start + 1][end] + DP[start][end - 1] - DP[start + 1][end - 1];
                }
            }
        }

        return DP[0][N - 1];
    }

    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int tests = input.nextInt();

        for (int i = 0; i < tests; i++) {
            String word = input.next();
            long cost = calculateCost(word);

            output.write(cost + "\n");
        }

        output.flush();
    }

}
