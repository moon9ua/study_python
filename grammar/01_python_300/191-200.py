# 191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

# for i in data:
#     for j in i:
#         print (j + j * 0.014)

# 193
# result = []
# for i in data:
#     for j in i:
#         result.append(j + j * 0.014)
# print(result)

# 194
# result = []
# for i in data:
#     row = []
#     for j in i:
#         row.append(j * 1.014)
#     result.append(row)
# print (result)

# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    print(i[3])