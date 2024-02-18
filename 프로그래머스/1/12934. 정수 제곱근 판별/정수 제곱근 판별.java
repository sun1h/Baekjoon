class Solution {
    public long solution(long n) {
        long answer = -1;
        double sqrt = Math.sqrt(n);
        long check = (long) sqrt;
        
        if(check == sqrt){
            answer = (check+1)*(check+1);
        }
        return answer;
    }
}