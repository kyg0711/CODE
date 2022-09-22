# 문제 3003번
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개

chess = [1,1,2,2,2,8] # 정해진 체스 말의 수대로 리스트틀 만듦.

a = list(map(int,input().split())) # map(적용시킬 함수, 적용할 값들) 
# list()를 이용하여 a라는 빈 list를 만들고 map()으로 입력 받은 값을 하나씩 int로 수행해줌.

for i in range(6): 
# range()는 0부터 괄호 안 값 미만만큼 반복 하기 때문에 0,1,2,3,4,5까지 총 6번 반복
    print(chess[i] - a[i], end= ' ') # chess의 i번째 index 값에 a의 i번째 index 값을 뺀 결과를 end로 공백을 만들어 출력


