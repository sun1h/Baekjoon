class Solution {
    public int solution(int n) {
        int mod = 1234567;
        int a = 0; 
        int b = 1; 
        int fib = 0; 

        for (int i = 2; i <= n; i++) {
            fib = (a + b) % mod; 
            a = b; 
            b = fib; 
        }

        return fib; 
    }
}
