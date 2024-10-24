class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int le = num_list.length;
        if(le>10){
            for(int i=0; i<le; i++){
                answer += num_list[i];
            }
        }else{
            answer = 1;
            for(int i=0; i<le; i++){
                answer *= num_list[i];
            }
        }
        return answer;
    }
}