
// Math.sqrt(n)은 제곱근인 수를 구해주는 함수
// Math.pow(n, n2)은 제곱근인 n의 ^n2 거듭제곱을 해주는 함수

// 여기서 주의할 점은 형변환!
// Math.sqrt(n)은 제곱근을 구하기 위해 루트를 씌우므로 소수점이 나올 수 있어 double
// 소수점이 나오는 결과를 정수만 표현하기 위해 다시 long으로 강제 형변환

class Solution {
    public long solution(long n) {
        long answer = 0;

        double n_sqrt = Math.sqrt(n);             // Math.sqrt(n)은 제곱근인 수를 구해주는 함수


        if (Math.pow((long) n_sqrt, 2) == n) {
            answer = (long) Math.pow(n_sqrt+1, 2);  // Math.pow(n, n2)은 제곱근인 n의 ^n2 거듭제곱을 해주는 함수
        } else {
            answer = -1;
        }

        return answer;
    }
}