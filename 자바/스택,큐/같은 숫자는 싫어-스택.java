// 리스트로 푼 방식
// 리스트 맨 앞에 문제에서 주어진 배열의 첫 원소를 넣고
// 루프를 1인덱스부터 조회하여 앞의 인덱스의 값과 다르면 리스트에 넣어주었다.

import java.util.*;
public class Solution {
    public int[] solution(int []arr) {
        List<Integer> answer = new ArrayList<>();
        answer.add(arr[0]);

        for (int i=1; i<arr.length; i++) {
            if (arr[i-1] != arr[i]) {
                answer.add(arr[i]);
            }
        }

        return answer.stream().mapToInt(i->i).toArray();  // stream()과 mapToInt() 메소드를 이용하여 ArrayList를 int[] 배열로 변환한 것
    }
}



// 스택 활용 방식
// 정답 리스트에 문제에서 주어진 배열의 첫번째 원소 값을 넣은 후
// 문제에서 주어진 배열에서 루프를 돌려가며
// 정답 리스트의 마지막 값을 빼오고
// 빼왔던 값과 for문의 현재 값이 같으면 같은 값이 연속으로 온 것이므로 빼왔던 값만 다시 넣어주고
// 서로 다르면 빼왔던 값과 for문의 현재 값을 차례로 넣어준다.

public class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();

        Stack<Integer> stack = new Stack<>();
        stack.add(arr[0]);

        for (int i : arr){
            int standard = stack.pop();   // 정답 리스트의 마지막 값을 빼오고

            if (i == standard) {          // 빼왔던 값과 for문의 현재 값이 같으면 같은 값이 연속으로 온 것이므로 빼왔던 값만 다시 넣어주고
                stack.push(standard);
            } else {                      // 서로 다르면 빼왔던 값과 for문의 현재 값을 차례로 넣어준다.
                stack.push(standard);
                stack.push(i);
            }
        }

        return stack.stream().mapToInt(i->i).toArray();
    }
}

