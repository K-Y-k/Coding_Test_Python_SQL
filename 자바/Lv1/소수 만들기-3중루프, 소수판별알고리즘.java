class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int sum =0;

        for (int i=0; i<nums.length; i++) {             // 3개의 숫자를 조합하기 위해 3중 루프로 하나씩 조회
            for (int j=i+1; j<nums.length; j++) {
                for (int k=j+1; k<nums.length; k++) {
                    sum = nums[i] + nums[j] + nums[k];

                    if (isPrime(sum)) {                 // 소수이면 카운팅
                        answer++;
                    }
                }
            }
        }

        return answer;
    }

    private boolean isPrime(int num) {
        if (num < 2) {                         // 0과 1은 소수가 아니다.
            return false;
        }

        for (int i=2; i<=Math.sqrt(num); i++){ // 1은 소수가 아니기 때문에 i=2부터 조회한다. 제곱근까지 소수가 아닌지 확인하면 된다.
            if (num % i == 0) {                // 나누어 떨어지면 소수가 아니므로 false
                return false;
            }
        }

        return true;                           // 위에서 모두 조회해보았지만 나누어 떨어지지 않으면 소수이므로 true
    }
}