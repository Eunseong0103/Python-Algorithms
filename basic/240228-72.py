# Q. 문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 
#    한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.


# S. 0 < s의 길이 < 1,000
#    s는 소문자로만 이루어져 있습니다.



def solution(s):
    answer=""
    for i in s:
        if s.count(i)==1:
            answer+=i
    lst=sorted(answer)   
    return "".join(lst)

#! count 함수는 문자열,리스트, 집합 iterable자료형 에서 쓰이는 메서드