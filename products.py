#讀取檔案
products = []
with open('products.txt','r', encoding='utf-8') as f:# 用utf-8編碼方式讀取檔案
	for line in f:
		if '商品,價格' in line:
			continue #繼續,但跳到下一個迴圈
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#讓使用者輸入資料
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': # 逃出迴圈
		break
	price = input ('請輸入商品價格')
	price = int(price) # 將價格資訊轉換成整數資訊
	p = []
	p.append(name)
	p.append(price)   #以上三行可簡寫為p = [name, price]
	products.append(p)
print(products)  #印出全部的清單資訊

# 印出商品資訊
for p in products:
	print(p[0], '的價格是', p[1])  #印出清單中的第一個產品(清單索引1的價格(索引2)
	print(p[0][1]) #同上
a = products[1][1] # 大清單中的索引二中的索引二.也就是第二個商品的價格
b = products[1][0] # 大清單中的索引二中的索引一.也就是第二個商品的價格
print(a) 
print(b)

# 用w指令寫入成一個products.csv,csv是很常用的資料儲存格式,並存成utf-8編碼格式以便中文顯示
with open('products.csv', 'w', encoding='utf-8') as f:  
	f.write('商品，價格\n') #在寫入的資料表格第一欄位中加入標題，要注意編碼跟換行
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n' )  #合成一個大字串寫入f,每個屬性中間用逗點做區隔

