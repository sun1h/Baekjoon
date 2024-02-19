class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for(int i=4; i<=n; i++){
            int tmp = 1;
            for(int j=2; j<=i; j++){
                if(i%j==0){
                    tmp+=1;
                }
            }
            if(tmp >=3){
                answer+=1;
            }
        }
        return answer;
    }
}