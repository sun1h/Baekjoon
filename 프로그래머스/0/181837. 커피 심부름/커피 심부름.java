class Solution {
    public int solution(String[] order) {
        int answer = 4500*order.length;
        for(String o:order){
            if(o.contains("latte")){
                answer+=500;
            }
        }
        return answer;
    }
}