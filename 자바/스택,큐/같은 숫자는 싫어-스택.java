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

        return answer.stream().mapToInt(i -> i).toArray();  // stream()과 mapToInt() 메소드를 이용하여 ArrayList를 int[]로 변환한 것
    }
}


