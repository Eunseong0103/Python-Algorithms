# Q. 머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다.
#    피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 
#    모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

# S. 1 ≤ n ≤ 100

def solution(n):
    answer=1
    while (answer*6) % n !=0:
        answer+=1
    
    return answer


#! 최대 공약수란?
# 둘 이상의 정수의 공약수 중에서 가장 큰 것을 말합니다.
# greatest common divisor 라 부르며 약자로 gcd 라 합니다. 이 약자를 그대로 함수 이름으로 사용하는 걸로 보입니다.

# math.gcd( 숫자들 )

#! 최소 공배수란?
# 둘 이상의 정수의 공배수 중에서 가장 작은 것을 말합니다.
# least common multiple을 줄여서 lcm이라 부르고, 이것으로 함수 이름을 정한 것으로 판단됩니다.

# math.lcm ( 숫자들 )