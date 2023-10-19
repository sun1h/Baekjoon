class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        int meat = n;
        int service = 0;
        while(meat>=10){
            meat = meat - 10; 
            service+=1;
        }
        answer = 12000*n+2000*(k-service);
        return answer;
    }
}