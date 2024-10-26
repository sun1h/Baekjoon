class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int le = p.length();
        long pValue = Long.parseLong(p); 

        for (int i = 0; i <= t.length() - le; i++) {
            long tmp = Long.parseLong(t.substring(i, i + le));
            if (tmp <= pValue) {
                answer++;
            }
        }
        return answer;
    }
}