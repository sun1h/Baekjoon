class Solution {
    public int solution(int n) {
        int answer = 1;
        
        for(int i=1; i<n; i++){
            int total = 0;
            int addNum = i;
            while(total<=n){
                if(total==n){
                    ++answer;
                    break;
                }
                total+=addNum;
                ++addNum;          
            }           
        }
        return answer;
    }
}