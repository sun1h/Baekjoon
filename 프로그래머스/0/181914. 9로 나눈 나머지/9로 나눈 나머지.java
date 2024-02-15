import java.math.BigInteger;

class Solution {
    public int solution(String number) {
        BigInteger bigNumber = new BigInteger(number);
        BigInteger result = bigNumber.mod(BigInteger.valueOf(9));

        return result.intValue();
    }
}
