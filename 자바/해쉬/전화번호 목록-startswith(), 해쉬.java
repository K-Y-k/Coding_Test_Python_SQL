// 정렬후 startswith 방식: 다음 번호 문자가 접두어를 가지는지 startswith()를 이용해 확인할 수 있다.

import java.util.*;

public class Solution {
    public boolean solution(String[] phoneBook) {
        boolean answer = true;

        Arrays.sort(phoneBook);                               // 문자열 길이 순으로 정렬

        for (int i = 0; i < phoneBook.length - 1; i++) {
            if (phoneBook[i+1].startsWith(phoneBook[i])) { // 다음 원소가 현재 원소의 접두어인지 확인
                return false;
            }
        }

        return answer;
    }
}



// 딕셔너리를 사용한 방식: 각 번호를 딕셔너리에 담고
//                     전화번호부를 각 조회할 때 각 번호 하나씩 접두사에 추가하면서
//                     현재 접두사가 딕셔너리에 담긴 것이 있지만 전화번호부의 전체 형태가 동일하지 않는 것이면 접두사가 겹친 것이므로 False

import java.util.*;

public class Solution {
    public boolean solution(String[] phoneBook) {
        boolean answer = true;
        HashMap<String, Integer> temp = new HashMap<>();

        for (String number : phoneBook) {
            temp.put(number, 1);
        }

        for (String phone_number : phoneBook) {
            String prefix = "";

            for (char digit : phone_number.toCharArray()) {
                prefix += digit;
                if (temp.containsKey(prefix) && !prefix.equals(phone_number)) {
                    return false;
                }
            }
        }

        return answer;
    }
}