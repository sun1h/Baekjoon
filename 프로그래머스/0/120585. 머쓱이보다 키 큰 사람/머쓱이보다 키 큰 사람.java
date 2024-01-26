import java.util.*;

class Solution {
    public int solution(int[] array, int height) {
        int answer = array.length;
        Arrays.sort(array);
        for (int i=0; i<array.length; i++){
            System.out.println(array[i]);
            if (array[i]>height){
                break;
            }else{
                answer-=1;
            }
        }
        return answer;
    }
}