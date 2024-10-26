import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> setNum = new HashSet<>();
        for(int i=0; i<numbers.length-1; i++){
            for(int j=i+1; j<numbers.length; j++){
                setNum.add(numbers[i]+numbers[j]);
            }
        }
        
        return setNum.stream().mapToInt(i->i).sorted().toArray();
    }
}