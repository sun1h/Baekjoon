class Solution {
    public int solution(int hp) {
        int answer = 0;
        
        int g = hp/5;
        answer += g;
        hp = hp - g*5;
        
        int s = hp/3;
        answer += s;
        hp = hp - s*3;
        
        answer += hp;
        
        return answer;
    }
}