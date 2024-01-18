class Solution {
    public int solution(int n) {
        int answer = 0;

        int[] dp = new int[100001];

        dp[0] = 0;
        dp[1] = 1;

        for (int i=2; i<=n; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567;   // 오버플로우가 발생하지 않게 여기서 1234567을 나누고 적용시키자.
        }

        answer = dp[n];

        return answer;
    }
}