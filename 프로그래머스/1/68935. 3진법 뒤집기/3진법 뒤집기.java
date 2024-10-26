class Solution {
    public int solution(int n) {
        int answer = 0;
        StringBuilder t = new StringBuilder();
        
        while(true){
            if(n<3){
                t.append(n);
                break;
            }
            t.append(String.valueOf(n%3));
            n/=3;
        }
        t.reverse();
        
        for(int i=0; i<t.length();i++){
            answer+= Character.getNumericValue(t.charAt(i))*Math.pow(3,i);
        }
        return answer;
    }
}