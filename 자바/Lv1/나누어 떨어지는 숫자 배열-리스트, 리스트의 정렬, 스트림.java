import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> answer = new ArrayList();

        for (int i=0; i<arr.length; i++) {
            if (arr[i] % divisor == 0) {
                answer.add(arr[i]);
            }
        }

        Collections.sort(answer);           // ArrayList 정렬
        // Collections.sort(answer, Collections.reverseOrder());

        if (answer.size() == 0) {
            answer.clear();
            answer.add(-1);
        }

        return answer.stream()               // ArrayList를 배열로 변환
                .mapToInt(i->i)
                .toArray();
    }
}