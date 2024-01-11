import java.util.*;
class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;

        // 오름차순 정렬
        Arrays.sort(A);
        Arrays.sort(B);

        for (int i=0; i<A.length; i++) {
            answer += A[i] * B[B.length - 1 - i]; // 인덱스를 끝에서부터 가져와서 역순으로 나타냄  Arrays.sort()는 Collections.reverseOrder()가 안됨..
        }

        return answer;
    }
}


// Collections.reverseOrder()는 Integer클래스와 String 클래스만 가능하기에
// int 배열 -> Integer 배열로 변환시키고 사용해야 한다.
class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;

        Integer[] B_Integer = Arrays.stream(B).boxed().toArray(Integer[]::new);

        Arrays.sort(A);
        Arrays.sort(B_Integer, Collections.reverseOrder());

        for (int i=0; i<A.length; i++) {
            answer += A[i] * B_Integer[i];
        }

        return answer;
    }
}