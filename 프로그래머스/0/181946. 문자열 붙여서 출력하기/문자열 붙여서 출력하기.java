import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        String answer = "";
        Scanner sc = new Scanner(System.in);
        // String a = sc.next();
        // answer += a;
        // String b = sc.next();
        // answer += b;
        while (sc.hasNext()) {  
            answer += sc.next(); 
        }
        System.out.println(answer);
    }
}