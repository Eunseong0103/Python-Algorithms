# Q. 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 
#    배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

# S. 3 ≤ numbers의 길이 ≤ 20
#    direction은 "left" 와 "right" 둘 중 하나입니다.


def solution(numbers, direction):
    answer=[]
    if direction=='right':
        return [numbers[(i-1)%len(numbers)] for i in range(len(numbers))]
    elif direction =="left" :
       return [numbers[(i+1)%len(numbers)] for i in range(len(numbers))]
    return answer


# def solution(numbers, direction):
#     return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
