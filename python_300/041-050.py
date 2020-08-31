# 041
ticker = "btc_krw"
print (ticker.upper())

# 042
ticker = "BTC_KRW"
print (ticker.lower())

# 043
a = "hello"
print (a.capitalize())

# 044
file_name = "보고서.xlsx"
# print (file_name[-4:] == "xlsx")
print (file_name.endswith("xlsx"))

# 045
print (file_name.endswith(("xls", "xlsx")))

# 046
file_name = "2020_보고서.xlsx"
print (file_name.startswith("2020"))

# 047
a = "hello world"
print (a.split(" "))

# 049
date = "2020-05-01"
print (date.split("-"))

# 050
data = "  039490       "
# print (data.strip())
print (data.rstrip())