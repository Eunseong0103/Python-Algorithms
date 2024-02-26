# Q. 정수 배열 num_list와 정수 n이 매개변수로 주어집니다. 
#   num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.
#   num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로 num_list를 2 * 4 배열로 다음과 같이 변경합니다. 
#   2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.

# S. num_list의 길이는 n의 배 수개입니다.
#   0 ≤ num_list의 길이 ≤ 150
#   2 ≤ n < num_list의 길이


def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer



#! 주의 
# 원본 코드에서 answer = [[]]으로 초기화했을 때, append()를 사용하면 새로운 부분 리스트가 비어있는 리스트에 추가되어 
# [[], [1, 2, 3, 4], [5, 6, 7, 8]]와 같은 형태가 됩니다. 
# 이는 초기에 빈 리스트가 있어서 새로운 리스트가 그 빈 리스트에 추가되는 효과를 낳습니다.