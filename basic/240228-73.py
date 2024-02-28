# Q. 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 
#    정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.


# S. 중복된 원소는 없습니다.
#    1 ≤ emergency의 길이 ≤ 10
#    1 ≤ emergency의 원소 ≤ 100


a={12:13, "dfs":"dfs",14:"dfsf"}
print(list(a.items()))

#!
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]



# def solution(emergency):
#     e = sorted(emergency,reverse=True)
#     return [e.index(i)+1 for i in emergency]


# def solution(emergency):
#     arr = []
#     for i in emergency:
#         idx = 1
#         for j in emergency:
#             if i < j:
#                 idx += 1
#         arr.append(idx)
#     return arr