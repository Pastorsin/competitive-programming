import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;

class Main {

    public static boolean isPalinword(String word) {
        int N = word.length();

        if (N < 4) {
            return false;
        }

        String firstPalindromeFound = null;
        // TODO - Replace by string length
        int firstSize = -1;

        for (int size = 2; size < N; size++) {
            for (int start = 0; start < N - size; start++) {
                int end = start + size;

                // Extremes are equals
                if (word.charAt(start) == word.charAt(end)) {
                    String substring = word.substring(start, end + 1);
                    String reversed = new StringBuilder(substring).reverse().toString();

                    // Palindrome found
                    if (substring.equals(reversed)) {
                        // Store the first palindrome
                        if (firstPalindromeFound == null) {
                            firstPalindromeFound = substring;
                            firstSize = size;
                        }
                        // Equals size and differents strings
                        else if (firstSize == size && !firstPalindromeFound.equals(substring)) {
                            return true;
                        }
                        // Differents size and not embedded strings
                        else if (firstSize != size && !substring.contains(firstPalindromeFound)) {
                            return true;
                        }
                    }
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