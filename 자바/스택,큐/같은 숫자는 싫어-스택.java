// 정답 리스트에 문제에서 주어진 배열의 첫번째 원소 값을 넣은 후
// 문제에서 주어진 배열에서 루프를 돌려가며
// 정답 리스트의 마지막 값을 빼오고 해당 값과 for문의 값이 같으면 같은 값이 연속으로 온 것이므로 한번만 넣고
// 서로 다르면 빼왔던 마지막 값과 for문의 값을 차례로 넣어준다.

import java.util.*;
public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(arr[0]);

        for (int i : arr) {
            int standard = answer.remove(answer.size() - 1);

            if (i == standard) {
                answer.add(i);
            } else {
                answer.add(standard);
                answer.add(i);
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();  // stream()과 mapToInt() 메소드를 이용하여 ArrayList를 int[] 배열로 변환한 것
    }
}


