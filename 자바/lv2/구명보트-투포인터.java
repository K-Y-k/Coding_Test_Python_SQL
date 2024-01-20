import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;

        Arrays.sort(people);                                // 오름차순으로 정렬한 후
 
        int left = 0;                                       // 최소값의 인덱스과
        int right = people.length - 1;                      // 최대값의 인덱스를 지정한 후

        while (left <= right) {                             // 모든 인덱스를 조회할 때까지 반복
            if (people[left] + people[right] <= limit) {    // 최소값과 최대값이 한도값보다 작거나 같으면 이 최초무게인 사람과 최대무게인 사람이 보트에 탈 수 있으므로 
                left += 1;                                  // 두명이 보트에 탄 것으로 가정하여 각 인덱스를 처리한다.
                right -= 1;
            } else {                                        // 합이 한도값보다 큰 경우는 혼자 타야하므로
                right -= 1;                                 // 최대값의 인덱스만 조정
            }

            answer += 1;                                    // 사람이 탑승한 구명보트를 카운트
        }

        return answer;
    }
}