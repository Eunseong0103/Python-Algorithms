# Q. 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록
#    solution 함수를 완성해주세요.


# S. 1 ≤ array의 길이 ≤ 100
#    1 ≤ array의 원소 ≤ 100
#    1 ≤ n ≤ 100
#    가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.



#! 먼저 작은 수를 앞으로 뺴주면 된다....
def solution(array, n):
    array.sort()
    temp = []

    for i in array :
        temp.append( abs(n-i) )

    return array[temp.index(min(temp))]