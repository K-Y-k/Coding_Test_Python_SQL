class Solution {
    public int solution(int[] arr) {
        int answer = 1;

        for (int i : arr) {
            answer = lcm(answer, i);
        }

        return answer;
    }


    // 최대공약수 함수
    private static int gcd(int a, int b) {
        if (a % b == 0) {
            return b;
        } else  {
            return gcd(b, a % b);
        }
    }

    // 최소공배수
    private static int lcm(int a, int b) {
        return a * b / gcd(a, b); // 공식
    }
}