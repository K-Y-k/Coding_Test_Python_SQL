// 의상의 조합의 경우의 수만 구하는 것이므로
// 1. 딕셔너리로 각 종류에 맞는 것을 카운팅하는데 카운팅할 때 해당 종류의 의상을 착용 안할 수도 있으므로 입지 않는 것 까지해서 +1 해줘야한다.
// 2. 위 적용한 카운팅 된 것끼리 곱해서 조합의 경우의 수를 구한다.
// 3. 추가로 모두 착용하지 않을 수는 없으므로 최종적으로 -1을 해준다.


import java.util.*;

public class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> clothesDic = new HashMap<>(); // 해쉬 선언

        for (String[] item : clothes) {                   // 받아온 clothes의 값과 카테고리를 모두 조회해서
            String type = item[1];                        // 옷의 카테고리(타입)

            if(!clothesDic.containsKey(type)) {           // 해쉬에 없으면 착용하지 않는 경우의 수까지 생각해서 2부터 시작하게 초기화한다.
                clothesDic.put(type, 2);
            } else {                                      // 해쉬에 있으면 +1 해줌
                clothesDic.put(type, clothesDic.get(type) + 1);
            }
        }

        int answer = 1;                           // 모두 곱셈하는 조합 연산을 위해 1로 초기화

        for (int count : clothesDic.values()) {  // 최종 카운팅한 것을 가져와
            answer *= count;                     // 각 카테고리의 카운팅한 개수를 곱해줌
        }

        return answer - 1;                       // 모두 착용하지 않는 경우를 제외하고 반환
    }
}