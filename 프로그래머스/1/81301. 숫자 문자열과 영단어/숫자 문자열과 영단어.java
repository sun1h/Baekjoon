class Solution {
    public int solution(String s) {
        String[] words = {"zero", "one", "two", "three", "four", 
                          "five", "six", "seven", "eight", "nine"};
        String answer = "";
        String tmp = "";
        
        for(char c:s.toCharArray()){
            if(Character.isDigit(c)){
                answer+=c;
            }else{
                tmp+=c;
                for(int i=0; i<words.length; i++){
                    if(tmp.equals(words[i])){
                        answer += i;
                        tmp="";
                    }
                }
            }  
        }
        
        return Integer.parseInt(answer);
    }
}