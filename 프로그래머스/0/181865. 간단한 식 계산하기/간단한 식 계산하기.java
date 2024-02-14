import java.util.*;

class Solution {
    public int solution(String binomial) {
        int answer = 0;
        String[] tmp = binomial.split(" ");
        System.out.print(Arrays.toString(tmp));
        if(tmp[1].equals("+")){
            answer = add(Integer.parseInt(tmp[0]),Integer.parseInt(tmp[2]));
        } else if(tmp[1].equals("-")){
            answer = subtract(Integer.parseInt(tmp[0]),Integer.parseInt(tmp[2]));
        }else{
            answer = multiply(Integer.parseInt(tmp[0]),Integer.parseInt(tmp[2]));
        }
        return answer;
    }
    
    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }
}