import sys

N, M = map(int, input().split())

minPackage = 1001                         # 문제에서 주어지는 값 중 가장 큰 값을 기준으로 잡는다.
minPiece = 1001

for _ in range(M):                        # 입력된 패키지, 낱개 가격이랑 위 기준 값이랑 비교해 작은값으로 지정﻿
    package, piece = map(int, sys.stdin.readline().split())
    minPackage = min(minPackage, package)
    minPiece = min(minPiece, piece)

result = 0

pacakageNum = N // 6                      # 패키지 단위
pieceNum = N % 6                          # 낱개 단위의 나머지


# 패키지(6개) 단위에서의 가격 비교
if minPackage > minPiece*6:               # 낱개가 패키지보다 더 저렴할 때
    result += N * minPiece                # 낱개로 전부 구매하면 끝이지만

else:
    # 패키지가 더 저렴할 때는 패키지 단위로 구매후 남은 낱개도 다시 가격비교해서 더하기
    result += pacakageNum * minPackage    # 패키지 단위 구매

    # 패키지 단위 구매후 후에도 낱개가 남은 상황에서의 가격 비교
    if minPackage >= minPiece * pieceNum: # 패키지 보다 낱개가 더 싸면  낱개로 구매
        result += pieceNum * minPiece     # 낱개로

    else:                                 # 패키지가 더 싸면
        result += minPackage              # 패키지 1개 구매

print(result)
