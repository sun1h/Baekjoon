import java.util.*;

class Solution {
    public String solution(String s) {
        String[] tmp = s.split("");
        Arrays.sort(tmp, Collections.reverseOrder());
        String answer = String.join("",tmp);
        return answer;
    }
}