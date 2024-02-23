# Q. 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
#    my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.



# S.1 < my_string의 길이 < 100
#   0 ≤ num1, num2 < my_string의 길이
#   my_string은 소문자로 이루어져 있습니다.
#   num1 ≠ num2

def solution(my_string, num1, num2):
    answer = ''
    for i in range(0,len(my_string)):
        if num1==i:
            answer+=my_string[num2]
        elif num2==i:
            answer+=my_string[num1]
        else:
             answer+=my_string[i]
            
    return answer

# def solution(my_string, num1, num2):
#     s = list(my_string)
#     s[num1],s[num2] = s[num2],s[num1]
#     return ''.join(s)
  

#! join() 메서드는 주로 리스트 안에 있는 요소들을 연결하는데 사용됩니다. 
#! 만약 단순히 문자열끼리 직접 이어붙이려면 + 연산자를 사용하면 됩니다.  