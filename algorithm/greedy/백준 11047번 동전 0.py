import sys

N, K = map(int, sys.stdin.readline().split())  # N = 동전의 개수, K = 가지고 있는 돈

coins = []  # 동전 종류별 요소 저장
coin_count = 0  # 필요한 동전의 개수, 오름차순 정렬

for _ in range(N):
    coins.append(int(sys.stdin.readline()))  # 동전 종류 입력

while coins:  # 필요한 동전의 개수가 최솟값이 되려면 가장 가치가 높은 동전을 가능한한 최대로
    coin = coins.pop()
    if coin <= K:  # 남은 거스름돈보다 동전의 가치가 낮을 때 
        coin_count += K // coin  # 해당 동전을 최대로 가지고 갈 수 있는 개수
        K %= coin  # 남은 금액
        if K == 0:  # 남은 금액이 0원이면 종료 
            break

print(coin_count)
