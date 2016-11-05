import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int count = 0;
        int max = 0;
        while (n > 0) {
            if (n%2 == 1) {
                count ++;
            } else {
                max = Math.max(max, count);
                count = 0;
            }
            n = n>>1;
        }
        System.out.println(Math.max(count, max));
    }
}
