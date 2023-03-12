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
#篩選有good
good = []
'''
for d in data:
    if "good" in d:
        good.append(d)
'''
#快寫法
good = [d for d in data if 'good in d']
print(good[0])


print("一共有{}筆留言提到good".format(len(good)))     
print(new[0])

#文字記數
wc = {} #word count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增KEY進字典   
for word in wc:
    if wc[word] > 100:
        print(wc[word])

while True:
    a = input('請問你想查什麼字: ')        
    if a == 'q':
        print('感謝使用')
        break 
    if a in wc:    
        print(a, '出現次數為: ', wc[a])
    else:
        print('這個字沒出現過')    
        
    
