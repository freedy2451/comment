data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
#print(len(data))
#print(data[0])        
print("檔案讀取完了，總共有{}筆資料".format(len(data)))

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print("留言平均長度是", sum_len/len(data))   

#留言長度篩選
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("一共有", len(new), "筆留言小於100")        
print(new[0])
print(new[1])