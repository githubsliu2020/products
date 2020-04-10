#檢查預備檔案是否存在
import os # operating system 模組

#讀取檔案
def read_file(filename):
    products = [] #產生空清單
    with open(filename,'r', encoding='utf-8') as f:# 用utf-8編碼方式讀取檔案
        for line in f:
            if '商品,價格' in line:
                continue #繼續,但跳到下一個迴圈
            name, price = line.strip().split(',') #整個撈出來的字串用逗點切割(split),並且去掉換行符號(strip)
            products.append([name, price])
    return products


#讓使用者輸入資料
def user_input(products):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q': # 逃出迴圈
            break
        price = input ('請輸入商品價格')
        price = int(price) # 將價格資訊轉換成整數資訊
        products.append([name,price])
    print(products)  #印出全部的清單資訊
    return products


# 印出商品資訊
def print_product(products):
    for p in products:
        print(p[0], '的價格是', p[1])  #印出清單中的第一個產品(清單索引1的價格(索引2)


# 寫入檔案
def write_file(filename, products):
    with open('filename', 'w', encoding='utf-8') as f:  
        f.write('商品，價格\n') #在寫入的資料表格第一欄位中加入標題，要注意編碼跟換行
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n' )  #合成一個大字串寫入f,每個屬性中間用逗點做區隔

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): #檢查模組中的路徑下是不是有一個叫做products.csv的檔案
        print('yeah!找到檔案了!')
        products = read_file(filename)
    else :
        print('找不到檔案....')

    products = user_input(products)
    print_product(products)
    write_file('product.csv', products)

main()