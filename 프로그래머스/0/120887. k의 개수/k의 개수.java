class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        char K = Integer.toString(k).charAt(0);
        for(int num=i; num<=j; num++){
            String tmp = Integer.toString(num);
            for(char t:tmp.toCharArray()){
                if(t == K){
                    answer += 1;
                }
            }
                
        }
        return answer;
    }
}
