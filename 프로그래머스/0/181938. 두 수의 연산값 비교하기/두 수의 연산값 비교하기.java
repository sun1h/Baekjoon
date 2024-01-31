class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String sa = Integer.toString(a);
        String sb = Integer.toString(b);
        String n = sa + sb;
        int num1 = Integer.parseInt(n);
        int num2 = 2*a*b;
        if(num1>num2){
            answer = num1;
        }else{
            answer = num2;
        }
        return answer;
    }
}