import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        while(!s.equals("1")){
            ++answer[0];
            String tmp = s.replace("0","");
            answer[1] += s.length()-tmp.length();
            s = Integer.toBinaryString(tmp.length());
        }
        return answer;
    }

}