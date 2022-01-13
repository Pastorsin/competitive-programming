/*
Java v1.8.0_151

https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1394
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;

class Main {

    public static String makePalindrome(String word, int[][] DP) {
        int N = word.length();

        int cost = DP[0][N - 1];

        if (cost == 0) {
            return word;
        }

        char[] buffer = new char[N + cost];

        // Pointer to the start and of the BUFFER
        int bufferStart = 0;
        int bufferEnd = buffer.length - 1;

        // Pointer to the start and of the WORD
        int start = 0;
        int end = N - 1;

        while (start < end) {
            if (word.charAt(start) == word.charAt(end)) {
                // If the characters are equal, then we can copy them
                buffer[bufferStart++] = word.charAt(start);
                buffer[bufferEnd--] = word.charAt(end);

                start++;
                end--;
            } else {
                // If the characters are not equal, then we need to
                // choose the character with minor cost
                int costLeft = DP[start][end - 1];
                int costRight = DP[start + 1][end];

                if (costLeft < costRight) {
                    buffer[bufferStart++] = word.charAt(end);
                    buffer[bufferEnd--] = word.charAt(end);

                    end--;
                } else {
                    buffer[bufferStart++] = word.charAt(start);
                    buffer[bufferEnd--] = word.charAt(start);

                    start++;
                }
            }
        }

        if (start == end) {
            buffer[bufferStart] = word.charAt(start);
        }

        return String.copyValueOf(buffer);
    }

    public static int[][] calculateCosts(String word) {
        int N = word.length();

        /* Determine cost */

        // Dynamic Programming Table
        // Rows and columns are indexed by the length of the word
        // Cells store if subword is palindrome or not
        int[][] DP = new int[N][N];

        // Size = 1: Base case only True if the characters are the same (e.g. "AA")
        // Size > 1: Extremes are equals and the middle is a palindrome (DP subproblems)
        // Is necessary try all sizes due to the cases AabcA, BabcB, etc.
        for (int size = 1; size < N; size++) {
            for (int start = 0; start < N - size; start++) {
                int end = start + size;
                int cost;

                // If extremes are equals => no cost
                // Else => min(DP[start, end - 1], DP[start + 1, end]) + 1
                if (word.charAt(start) == word.charAt(end)) {
                    cost = DP[start + 1][end - 1];
                } else {
                    cost = Math.min(DP[start][end - 1], DP[start + 1][end]) + 1;
                }

                DP[start][end] = cost;
            }
        }

        return DP;
    }

    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        while (input.hasNext()) {
            String word = input.nextLine();

            int[][] DP = calculateCosts(word);
            int cost = DP[0][DP.length - 1];

            String palindrome = makePalindrome(word, DP);

            output.write(cost + " " + palindrome + "\n");
        }

        output.flush();
    }

}