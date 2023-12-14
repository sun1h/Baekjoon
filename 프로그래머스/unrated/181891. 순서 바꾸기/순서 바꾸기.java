import java.util.*;

class Solution {
    public ArrayList solution(int[] num_list, int n) {
        ArrayList answer = new ArrayList<>();
        Integer[] post = Arrays.stream(Arrays.copyOfRange(num_list, n, num_list.length)).boxed().toArray(Integer[]::new);
        Integer[] pre = Arrays.stream(Arrays.copyOfRange(num_list, 0, n)).boxed().toArray(Integer[]::new);
        
        Collections.addAll(answer, post);
        Collections.addAll(answer, pre);

        return answer;
    }
}