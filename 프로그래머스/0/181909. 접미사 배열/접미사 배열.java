import java.util.*;

class Solution {
    public String[] solution(String myString) {
        int len = myString.length();
        String[] answer = new String[len];

        for (int i = 0; i < len; i++) {
            answer[i] = myString.substring(i, len);
        }

        Arrays.sort(answer);

        return answer;
    }
}
