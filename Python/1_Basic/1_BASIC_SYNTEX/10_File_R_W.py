txt_file = open("save.txt", 'w', newline='')
temp = '''
Hi my name is minsoo
Hello Python
I like animals
'''
txt_file.write(temp)

txt_file.close()

import csv

links = ['https://google.com/',
        'https://naver.com/',
        'https://youtube.com/',
        'https://nate.com/',
        'https://amazon.com/',
        'https://minsoo-kim.kro/',
        'https://gongsaemi.com/']

with open("save.csv", 'w', newline='') as f:
    linkst = csv.writer(f)
    linkst.writerow(links)

f.close()

with open("/Users/vision/academy/python/Python_JW/save.csv", 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)
        
# print(new_link)


# save = open("save.txt", 'r', encoding="utf-8-sig", delimiter='.') # r : read mode // w : read-write

# save_datas = save.readlines()       # read() : Whole text in list  

# for save_data in save_datas:
#     print(save_data)

# for save_data in save_datas:
#     print(save_data)
# save.write("Hello \nWorld \nI'm so tired")

f.close()
