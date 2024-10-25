class Solution {
    public int solution(int num) {
        int answer = 0;
        long n = num;
        
        while(n!=1){
            ++answer;
            if(answer>=500){
                return -1;
            }
            n = cal(n);
        }
        return answer;
    }
    
    public long cal(long n){
        if(n%2==0){
            return n/2;
        }else{
            return n*3+1;
        }
    }
}