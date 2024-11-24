lst_ID = []


def DataInit():
    try:
        buf = open('buffer.txt', 'w')
    except:
        print("Error of initiation")
    else:
        buf.close()


def DataReading(filename):
    file = open(filename, 'r', encoding='utf-8')
    #проходит по каждой строке и записывает ее в файл 'buffer.txt'.
    file_buf = open('buffer.txt', 'a', encoding='utf-8')
    #разделяет строку на строки, и [:-1] используется для исключения последней
    #пустой строки(если она есть).
    onstring = file.read().split("\n")[:-1]
    global lst_ID
    #cчитывание содержимого файла одной строкой
    for item in onstring:
        file_buf.write(item)
        file_buf.write("\n")
    file_buf.close()
    file.close()


def DataSave(filename):
    file = open(filename, 'a', encoding='utf-8')
    file_buf = open('buffer.txt', 'r', encoding='utf-8')
    #считывает содержимое файла 'buffer.txt' как одну строку
    #разделяет строку на строки, и исключает последнюю пустую строку (если она есть)
    onstring = file_buf.read().split("\n")[:-1]
    #проходит по каждой строке и записывает ее в указанный файл.
    for item in onstring:
        file.write(item)
        file.write("\n")

    file_buf.close()
    file.close()


def DataChange(n, id, author, title, publisher, price):
    import shutil
    shutil.copyfile('buffer.txt', 'buffer_.txt')
    file_buf = open('buffer.txt', 'w', encoding='utf-8')
    file_buf_copy = open('buffer_.txt', 'r', encoding='utf-8')
    onstring = file_buf_copy.read().split("\n")[:-1]
    count = 1
    for item in onstring:
        if count != int(n):
            file_buf.write(item)
            file_buf.write("\n")
            count += 1
        else:
            new_string = str(id), author, title, publisher, str(price)
            file_buf.write(','.join(new_string))
            file_buf.write("\n")
            count += 1

    file_buf.close()
    file_buf_copy.close()
    import os
    os.remove("buffer_.txt")


def MultipleDelete(lst_for_id):
    import shutil
    shutil.copyfile('buffer.txt', 'buffer_.txt')
    file_buf = open('buffer.txt', 'w', encoding='utf-8')
    file_buf_copy = open('buffer_.txt', 'r', encoding='utf-8')
    onstring = file_buf_copy.read().split("\n")[:-1]
    global lst_ID
    for element in lst_for_id:
        lst_ID.remove(int(element))
    lll = []
    for i in lst_for_id:
        for item in onstring:
            if item.split(',')[0] != i and int(item.split(',')[0]) in lst_ID:
                if int(item.split(',')[0]) not in lll:
                    lll.append(int(item.split(',')[0]))
                    file_buf.write(item)
                    file_buf.write("\n")
            else:
                continue

    file_buf.close()
    file_buf_copy.close()
    import os
    os.remove("buffer_.txt")


def DataDelete(n):
    import shutil
    shutil.copyfile('buffer.txt', 'buffer_.txt')
    file_buf = open('buffer.txt', 'w', encoding='utf-8')
    file_buf_copy = open('buffer_.txt', 'r', encoding='utf-8')
    onstring = file_buf_copy.read().split("\n")[:-1]
    count = 1
    for item in onstring:
        if count != int(n):
            file_buf.write(item)
            file_buf.write("\n")
            count += 1
        else:
            count += 1
    file_buf.close()
    file_buf_copy.close()
    import os
    os.remove("buffer_.txt")


def DataAdd(id, author, title, publisher, price):
    file = open('buffer.txt', 'a', encoding='utf-8')
    # проверка на правильность открытия
    new_string = id, author, title, publisher, price
    file.write(','.join(new_string))
    file.write("\n")


def DataClean():
    file = open('buffer.txt', 'w', encoding='utf-8')
    file.write('')
    file.close()


def DataBaseDestroy():
    import os
    os.remove("buffer.txt")


def DataSearch(request, request_name):
    lst = []
    if request == 'ID':
        lst = Search(request_name, 0)
    if request == 'Автор':
        lst = Search(request_name, 1)
    if request == 'Название':
        lst = Search(request_name, 2)
    if request == 'Издатель':
        lst = Search(request_name, 3)
    if request == 'Цена':
        lst = Search(request_name, 4)
    return lst


def Search(request_name, i=0):
    flag = False
    file_buf = open('buffer.txt', 'r', encoding='utf-8')
    onstring = file_buf.read().split("\n")[:-1]
    lst = []
    for item in onstring:
        request = item.split(",")[i]
        if request != str(request_name):
            continue
        else:
            lst.append(item)
            flag = True
    file_buf.close()
    return lst


def DataCreateBackup(n):
    import zipfile
    zname = r'C:\Backup\'', n, '.zip'
    newzip = zipfile.ZipFile(''.join(zname), 'w')
    newzip.write(r'buffer.txt')
    newzip.close()


def DataRestoreBackup(n):
    import zipfile
    import os
    archive = r'C:\Backup\''+ n + '.zip'
    with zipfile.ZipFile(archive, 'r') as zip_file:
        zip_file.extract('buffer.txt', 'C:\\Backup')
    os.chdir('C:\\Backup')
    os.rename('buffer.txt', n)
    os.chdir('C:\\Users\\Arina\\PycharmProjects\\pythonProject5')
    DataReading('C:\\Backup\\' + n)
    os.remove('C:\\Backup\\' + n)
