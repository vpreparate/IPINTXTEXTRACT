import glob
import re
from tkinter import *

root = Tk()

root.title("TEXT IP HUNTER")
root.geometry('600x600')

img = PhotoImage(file='Wallet PLEASE 0.00051.png')
label_img = Label(image=img)
label_img.pack(side=RIGHT, padx=10)

def button_clicked1():
    file_list = glob.glob('*.txt')
 
    combined_file = open('combined_file.txt', 'w')
 
    for file_name in file_list:
        f = open(file_name)
        combined_file.write(f.read())
        combined_file.write('\n')
        f.close()
 
    combined_file.close()

def button_clicked2():
    with open("combined_file.txt", "r") as file:
    # заменить IP.txt на имя файла

        txt = file.read()

        out_txt = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", txt)
    

    f = open("good.TXT", "w")
    con = "\n".join(out_txt)
    f.write(con)
    f.close()

def button_clicked3():
    #Открываем файл
    with open('good.TXT', 'r') as file:
        #Создаем список
        words = []
        #Читаем данные из файла
        data = file.readlines()
        #Для каждой строки
        for line in data:
            #Для каждого слова в строке
            for word in line.split():
                #Если слово уже есть в списке, пропускаем его
                if word in words:
                    continue
                #Иначе добавляем его в список
                else:
                    words.append(word)
        #Открываем файл для записи
        with open('result.txt', 'w') as res:
            #Записываем слова в файл
            res.write('\n'.join(words))



btn1 = Button(root, text="join All", bg="white", command=button_clicked1)
btn2 = Button(root, text="Find IP", bg="white", command=button_clicked2)
btn3 = Button(root, text="Del Doubles", bg="white", command=button_clicked3)



btn1.pack(fill=X, padx=10, pady=10)
btn2.pack(fill=X, padx=10, pady=10)
btn3.pack(fill=X, padx=10, pady=10)




root.mainloop()
