# 내가 푼 방식
# 캐시 리스트를 만들어서 
# 현재 값이 캐시에 있으면 캐시에 있는 기존 것을 지우고 최근 위치로 옮겨준 후 실행시간을 적용하고
# 캐시에 없으면 캐시 크기의 조건에 맞게 넣어주고 실행시간을 적용하였다.  

# 내가 부족했던 점
# 1. 캐시에 있어도 캐시 위치의 기존 것을 삭제하고 다시 최근 위치에 넣어줘야했다.
# 2. 캐시 사이즈가 0인 경우는 따로 처리해주기


def solution(cacheSize, cities):
    answer = 0
    cache = []                                    # 캐시 리스트를 선언
    
    if cacheSize == 0:                            # 캐시 사이즈가 0인 경우는 무조건 실행시간이 (개수 x 5)로 되므로 따로 처리
        answer = len(cities) * 5
    else:           
        for i in cities:
            if i in cache or i.lower() in cache:  # 캐시에 있으면
                cache.remove(i.lower())           # 기존 것을 지우고
                cache.append(i.lower())           # 최근 위치로 옮겨준 후
                answer += 1                       # 실행시간을 적용
                
            else:                                 # 캐시에 없으면
                if len(cache) == cacheSize:       # 캐시 크기의 조건에 맞게 처리해주었다.      
                    cache.pop(0)
                    cache.append(i.lower())
                    answer += 5
                else:                           
                    cache.append(i.lower())
                    answer += 5
    
    return answer