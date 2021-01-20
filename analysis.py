data = []
count = 0
with open('reviews.txt','r') as f: 
	for comment in f:
		data.append(comment)
		count += 1
		if count % 1000 == 0:
			print (len(data))
print ('檔案讀取好了!總共有',len(data),'筆資料喔')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	
print('平均是',sum_len/len(data))

