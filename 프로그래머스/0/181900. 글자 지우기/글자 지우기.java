import java.util.*;

class Solution {
    public String solution(String my_string, int[] indices) {
        StringBuilder sb = new StringBuilder(my_string);

        // 앞에서부터 짜르면 배열 순서가 달라지니깐 뒤에서 부터 짜르기
        Arrays.sort(indices);
        for (int i = indices.length - 1; i >= 0; i--) {
            sb.deleteCharAt(indices[i]);
        }

        return sb.toString();
    }
}
