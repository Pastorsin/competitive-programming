/*
Java v1.8.0_151

https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=193
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Scanner;

/*
Cases:

1. ALOLDOD: Found 2 palindromes and break iteration
2. ABAB: Found 2 palindromes overlaps
3. ZABAZXABAX: Found 2 palindromes with same middle
4. ABAD: Not found

*/

class Pair {
    int x;
    int y;

    Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;

        Pair pair = (Pair) o;

        if (x != pair.x)
            return false;
        return y == pair.y;
    }

    @Override
    public int hashCode() {
        int result = x;
        result = 31 * result + y;
        return result;
    }
}

class Main {

    public static boolean isPalinword(String word) {
        int N = word.length();

        // Needs N >= 4 to find least 2 palindromes in the word
        if (N < 4) {
            return false;
        }

        // Dynamic Programming Table
        // Rows and columns are indexed by the length of the word
        // Cells store if subword is palindrome or not
        HashMap<Pair, Boolean> DP = new HashMap<>();

        String firstPalindromeFound = null;

        // Size = 1: Base case only True if the characters are the same (e.g. "AA")
        // Size > 1: Extremes are equals and the middle is a palindrome (DP subproblems)
        // Is necessary try all sizes due to the cases AabcA, BabcB, etc.
        for (int size = 1; size < N; size++) {
            for (int start = 0; start < N - size; start++) {
                int end = start + size;

                Pair extremes = new Pair(start, end);
                Pair middle = new Pair(start + 1, end - 1);

                // Check if the extremes are equals and the middle is a palindrome
                if (word.charAt(start) == word.charAt(end) && (!DP.containsKey(middle) || DP.get(middle))) {
                    // Mark as palindrome
                    DP.put(extremes, true);

                    // Check if contains more than 2 characters
                    if (size > 1) {
                        String palindrome = word.substring(start, end + 1);

                        // Save the first palindrome found
                        if (firstPalindromeFound == null) {
                            firstPalindromeFound = palindrome;
                        }
                        // Check if palindrome not embedded in the first palindrome
                        else if (!palindrome.contains(firstPalindromeFound)) {
                            return true;
                        }
                    }

                } else {
                    // Mark as not palindrome
                    DP.put(extremes, false);
                }
            }

        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        while (input.hasNextLine()) {
            String[] words = input.nextLine().split("\\s+");

            for (String word : words) {
                if (isPalinword(word)) {
                    output.write(word + "\n");
                }
            }
        }

        output.flush();
    }
}