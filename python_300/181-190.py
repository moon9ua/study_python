# 182
stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]

# 183
stock = {
    "시가": [100, 200, 300],
    "종가": [80, 210, 330]
}

# 185
apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)): # 인덱스에 대한 반복문
    # for j in range(len(apart[i])):
        # print(apart[i][j], "호")
for i in apart: # 리스트에 대한 반복문
    for j in i:
        print(j, "호")

# 186
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i:
        print(j, "호")