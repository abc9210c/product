# 讀取檔案

with open('product.csv', 'r', encoding='utf-8') as f:
	for line in f:
		s = line.strip().split(',')
		# name, price = line.strip().split(',')
		# product.append([name, price])
		# 不用print(s)
		# name = s[0]
		# price =s[1]
		print(s)
#print(product)


product = []

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	p = []
	p.append(name)
	p.append(price)
	#p = [name, price]
	product.append(p)
	#product.append([name, price])
print(product)

for p in product:
	print(p[0], '價格是', p[1])


with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in product:
	    f.write(p[0] + ',' + p[1] + '\n')
