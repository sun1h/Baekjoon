class Solution {
    public int solution(String my_string) {
        int answer = 0;
        StringBuilder temp = new StringBuilder(); 
        
        for(char m : my_string.toCharArray()){
            if(Character.isDigit(m)){
                temp.append(m); 
            } else {
                if(temp.length() > 0){
                    answer += Integer.parseInt(temp.toString());
                    temp = new StringBuilder();
                }
            }
        }

        if(temp.length() > 0){
            answer += Integer.parseInt(temp.toString());
        }

        return answer;
    }
}
