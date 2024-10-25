class Solution {
    private int answer = 0;
    
    public int solution(int left, int right) {
        for(int i=left; i<=right; i++){
            cal(i);
        }
        return answer;
    }
    
    public void cal(int n){
        int tmp = 1;
        for(int i=2; i<=n; i++){
            if(n%i==0){
                ++tmp;
            }
        }
        answer += tmp%2==0? n: -n;
    }
}