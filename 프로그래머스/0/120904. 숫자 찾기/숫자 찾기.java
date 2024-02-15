class Solution {
    public int solution(int num, int k) {
        String n = Integer.toString(num);
        String str = Integer.toString(k);
        
        int position = n.indexOf(str);
        
        return position >= 0 ? position + 1 : -1;
    }
}
