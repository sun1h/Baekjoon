class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];

        for(int i=0; i<emergency.length; i++){
            for(int j=i; j<emergency.length; j++){
                if(emergency[j]>emergency[i]){
                    answer[i]+=1;
                }else{
                    answer[j]+=1;
                }
            }
        }
        return answer;
    }
}