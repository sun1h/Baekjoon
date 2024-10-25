class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int num = 0;
        int check = x;
        while(x>=1){
            num += x%10;
            x /= 10;
        }
        if(check%num!=0){
            answer = false;
        }
        return answer;
    }
}