import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        int[] arr = Arrays.stream(s.split(" "))
                          .mapToInt(i->Integer.parseInt(i))
                          .sorted()
                          .toArray();
        answer+=arr[0]+" "+arr[arr.length-1];
        
        return answer;
    }
}