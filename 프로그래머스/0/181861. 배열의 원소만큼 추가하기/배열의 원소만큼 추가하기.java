import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> answer = new ArrayList<>(); // 타입 지정 및 생성자 호출

        // arr의 각 원소에 대해
        for (int i = 0; i < arr.length; i++) {
            // arr[i]의 값만큼 answer에 추가
            for (int j = 0; j < arr[i]; j++) {
                answer.add(arr[i]);
            }
        }

        // ArrayList를 int[]로 변환하여 반환
        return answer.stream().mapToInt(i -> i).toArray(); // stream() 및 toArray() 수정
    }
}
