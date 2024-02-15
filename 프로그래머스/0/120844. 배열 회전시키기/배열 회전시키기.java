import java.util.*;
import java.util.stream.*;

class Solution {
    public ArrayList<Integer> solution(int[] numbers, String direction) {
        int len = numbers.length;
        ArrayList<Integer> answer = new ArrayList<Integer>();

        if(direction.equals("right")){
            answer.add(numbers[len-1]);
            answer.addAll(Arrays.stream(numbers, 0, len-1).boxed().collect(Collectors.toList()));
        } else {
            answer.addAll(Arrays.stream(numbers, 1, len).boxed().collect(Collectors.toList()));
            answer.add(numbers[0]);
        }

        return answer;
    }
}
