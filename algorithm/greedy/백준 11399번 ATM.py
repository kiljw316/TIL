N = int(input())  # 사람의 수
P = list(map(int, input().split()))  # 각 사람이 돈을 인출하는데 걸리는 시간

"""
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력하기 위해선
자신의 직전 사람의 인출 시간이 최소가 되어야 한다.
즉 먼저 뽑는 사람의 인출 시간을 줄이면 최종 시간의 합의 최솟값을 구할 수 있다. 
"""
P.sort()  # 오름차순 정리

# 첫 번쨰 방법
# withdraw_time_per_person = [P[0]]  # 각 사람마다 인출하기까지의 소요 시간 저자, 첫 번쨰 사람은 바로 인출
#
# for p in P[1:]:  # 두 번쨰 사람부터 누적 시간 저장
#     withdraw_time_per_person.append(withdraw_time_per_person[-1] + p)  # 이전 사람까지의 누적 시간 + 자신이 인출하는데 걸리는 시간
#
# print(sum(withdraw_time_per_person))  # 각 사람이 돈을 인출하는데 필요한 시간의 총합


# 두 번쨰 방법
total = 0  # 각 사람이 돈을 인출하는데 필요한 시간의 총합 
waiting = 0  # 각 사람이 돈을 인출하기까지 기다리는 시간

for p in P:
    waiting += p
    total += waiting

print(total)
