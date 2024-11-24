from tkinter import Frame, Label, Entry, END, Button, Toplevel
from Functions import *

def CreateTable():
    import tkinter
    from tkinter import ttk

    ws = tkinter.Tk()
    ws.title('Книжный магазин')
    ws.geometry('1000x500')

    books_frame = tkinter.Frame(ws)
    books_frame.pack()

    book_store = ttk.Treeview(books_frame)

    book_store.pack()
    #создание таблицы
    book_store['columns'] = ('ID', 'Author', 'Title', 'Publisher', 'Price')

    book_store.column("#0", width=0, stretch=tkinter.NO)
    book_store.column("ID", anchor=tkinter.W, width=80)
    book_store.column("Author", anchor=tkinter.W, width=200)
    book_store.column("Title", anchor=tkinter.W, width=270)
    book_store.column("Publisher", anchor=tkinter.W, width=80)
    book_store.column("Price", anchor=tkinter.W, width=80)

    book_store.heading("#0", text="", anchor=tkinter.W)
    book_store.heading("ID", text="ID", anchor=tkinter.W)
    book_store.heading("Author", text="Автор", anchor=tkinter.W)
    book_store.heading("Title", text="Название", anchor=tkinter.W)
    book_store.heading("Publisher", text="Издатель", anchor=tkinter.W)
    book_store.heading("Price", text="Цена", anchor=tkinter.W)

    #открытие файла
    file_buf = open('buffer.txt', 'r', encoding='utf-8')
    onstring = file_buf.read().split("\n")[:-1]
    lst = []
    for item in onstring:
        tupl = item.split(",")
        lst.append(tupl)

    global i
    i = 0
    for element in lst:
        book_store.insert(parent='', index='end', iid=i, text='',
                       values=element)
        i = i + 1

    book_store.pack()

    frame = Frame(ws)
    frame.pack(pady=20)

    bookid = Label(frame, text="ID")
    bookid.grid(row=0, column=0)

    bookauthor = Label(frame, text="Автор")
    bookauthor.grid(row=0, column=1)

    booktitle = Label(frame, text="Название")
    booktitle.grid(row=0, column=2)

    bookpublisher = Label(frame, text="Издатель")
    bookpublisher.grid(row=0, column=3)

    bookprice = Label(frame, text="Цена")
    bookprice.grid(row=0, column=4)

    # поле ввода
    bookid_entry = Entry(frame)
    bookid_entry.grid(row=1, column=0)

    bookauthor_entry = Entry(frame)
    bookauthor_entry.grid(row=1, column=1)

    booktitle_entry = Entry(frame)
    booktitle_entry.grid(row=1, column=2)

    bookpublisher_entry = Entry(frame)
    bookpublisher_entry.grid(row=1, column=3)

    bookprice_entry = Entry(frame)
    bookprice_entry.grid(row=1, column=4)

    open_name_entry = Entry(ws)
    open_name_entry.place(x=870, y=20)

    #заполнение виджетов ввода
    def select_record():
        #очистить поле ввода
        bookid_entry.delete(0, END)
        bookauthor_entry.delete(0, END)
        booktitle_entry.delete(0, END)
        bookpublisher_entry.delete(0, END)
        bookprice_entry.delete(0, END)

        #текущая (выбранная) запись в виджете
        selected = book_store.focus()
        values = book_store.item(selected, 'values')

        #вывод записи
        bookid_entry.insert(0, values[0])
        bookauthor_entry.insert(0, values[1])
        booktitle_entry.insert(0, values[2])
        bookpublisher_entry.insert(0, values[3])
        bookprice_entry.insert(0, values[4])

    #сохранение
    def update_record():
        selected = book_store.focus()

        #сохранить новые данные
        book_store.item(selected, text="", values=(bookid_entry.get(), bookauthor_entry.get(), booktitle_entry.get(), bookpublisher_entry.get(), bookprice_entry.get()))
        DataChange(selected, bookid_entry.get(), bookauthor_entry.get(), booktitle_entry.get(), bookpublisher_entry.get(), bookprice_entry.get())
        #очистить поля ввода
        bookid_entry.delete(0, END)
        bookauthor_entry.delete(0, END)
        booktitle_entry.delete(0, END)
        bookpublisher_entry.delete(0, END)
        bookprice_entry.delete(0, END)

    #сообщение об ошибке ввода
    def error_message():
        bookid_entry.delete(0, END)
        bookauthor_entry.delete(0, END)
        bookauthor_entry.insert(0, 'ВВЕДИТЕ')
        booktitle_entry.delete(0, END)
        booktitle_entry.insert(0, 'КОРРЕКТНУЮ')
        bookpublisher_entry.delete(0, END)
        bookpublisher_entry.insert(0, 'ЗАПИСЬ')
        bookprice_entry.delete(0, END)

    #внесение новой записи
    def input_record():
        global i
        i += 1
        id = bookid_entry.get()
        price = bookprice_entry.get()
        global lst_ID
        try:
            int_id = int(id)
            int_price = int(price)
        except:
            error_message()
        else:
            if int(id) in lst_ID or bookauthor_entry.get()=='' or booktitle_entry.get()=='' or bookpublisher_entry.get()=='':
                error_message()
            else:
                book_store.insert(parent='', index='end', iid=i, text='',
                       values=(id, bookauthor_entry.get(), booktitle_entry.get(), bookpublisher_entry.get(), bookprice_entry.get()))

                DataAdd(bookid_entry.get(), bookauthor_entry.get(), booktitle_entry.get(), bookpublisher_entry.get(), bookprice_entry.get())
                bookid_entry.delete(0, END)
                bookauthor_entry.delete(0, END)
                booktitle_entry.delete(0, END)
                bookpublisher_entry.delete(0, END)
                bookprice_entry.delete(0, END)

    #удаление записи
    def delete_record():
        selected = book_store.focus()
        book_store.delete(selected)
        DataDelete(selected)
        bookid_entry.delete(0, END)
        bookauthor_entry.delete(0, END)
        booktitle_entry.delete(0, END)
        bookpublisher_entry.delete(0, END)
        bookprice_entry.delete(0, END)

    #открытие базы данных из файла
    def open_database():
        filename = open_name_entry.get()
        try:
            file = open(filename, 'r', encoding='utf-8')
        except:
            open_name_entry.delete(0, END)
            open_name_entry.insert(0, 'Ошибка!')
        else:
            onstring = file.read().split("\n")[:-1]
            lst = []
            global lst_ID
            for item in onstring:
                tupl = item.split(",")
                if int(tupl[0]) not in lst_ID:
                    lst_ID.append(int(tupl[0]))
                    lst.append(tupl)

            global i
            i = 0
            for element in lst:
                book_store.insert(parent='', index='end', iid=i, text='',
                           values=element)
                i = i + 1
            DataReading(filename)

    #сохранение базы данных
    def save_database():
        ws_save = Toplevel()
        ws_save.geometry('500x250')
        message = Label(ws_save, text="Введите имя файла для сохранения: ")
        message.pack()
        save_entry = Entry(ws_save)
        save_entry.pack()

        def save_command():
            filename = save_entry.get()
            if filename == '':
                save_entry.delete(0, END)
                save_entry.insert(0, 'ВВЕДИТЕ ИМЯ ФАЙЛА')
            else:
                DataSave(filename)
                ws_save.destroy()

        readysave_btn = Button(ws_save, text="Сохранить", command=save_command)
        readysave_btn.pack()

    #очистить базу данных
    def clean_database():
        book_store.delete(*book_store.get_children())
        DataClean()

    #создать backup файл
    def create_backup():
        ws_save = Toplevel()
        ws_save.geometry('500x250')
        message = Label(ws_save, text="Введите имя zip-файла для сохранения в папку Backup: ")
        message.pack()
        save_entry = Entry(ws_save)
        save_entry.pack()

        # сохранить файл
        def save_backup():
            filename = save_entry.get()
            if filename == '':
                save_entry.delete(0, END)
                save_entry.insert(0, 'ВВЕДИТЕ ИМЯ ФАЙЛА')
            else:
                DataCreateBackup(filename)
                ws_save.destroy()

        readysave_btn = Button(ws_save, text="Сохранить zip", command=save_backup)
        readysave_btn.pack()

    #восстановить из backup файла
    def restore_backup():
        ws_save = Toplevel()
        ws_save.geometry('500x250')
        message = Label(ws_save, text="Введите имя zip-файла для восстановления: ")
        message.pack()
        save_entry = Entry(ws_save)
        save_entry.pack()

        def take_backup():
            filename = save_entry.get()
            DataRestoreBackup(filename)
            ws_save.destroy()


        readytake_btn = Button(ws_save, text="Восстановаить zip", command=lambda:[take_backup(), refresh()])
        readytake_btn.pack()

    #обновить данные
    def refresh():
        book_store.delete(*book_store.get_children())
        file_buf = open('buffer.txt', 'r', encoding='utf-8')
        onstring = file_buf.read().split("\n")[:-1]
        lst = []
        for item in onstring:
            tupl = item.split(",")
            lst.append(tupl)

        global i
        i = 0
        for element in lst:
            book_store.insert(parent='', index='end', iid=i, text='',
                           values=element)
            i = i + 1

    #поиск данных
    def search_data():
        ws_search = Toplevel()
        ws_search.geometry('800x400')

        frame = Frame(ws_search)
        frame.pack(pady=20)

        section = Label(frame, text="Выберите поле:")
        section.grid(row=0, column=0)

        bookid = Label(frame, text="Запрос")
        bookid.grid(row=0, column=2)

        combo_section = ttk.Combobox(frame,
                                    values=[
                                        "ID",
                                        "Автор",
                                        "Название",
                                        "Издатель",
                                        "Цена"])
        combo_section.grid(column=0, row=1)
        combo_section.current(0)

        bookid_entry = Entry(frame)
        bookid_entry.grid(row=1, column=2)

        lst_for_id = []

        # показать результаты поиска
        def show_results():
            book_store.delete(*book_store.get_children())
            stringg = combo_section.get()
            request_name = bookid_entry.get()
            lst = DataSearch(stringg, request_name)
            lst2 = []
            for item in lst:
                tupl = item.split(",")
                lst_for_id.append(tupl[0])
                lst2.append(tupl)
            global i
            i = 0

            for element in lst2:
                book_store.insert(parent='', index='end', iid=i, text='',
                               values=element)
                i = i + 1

        search_btn = Button(ws_search, text="Поиск", command=show_results)
        search_btn.pack(pady=10)


        books_frame = tkinter.Frame(ws_search)
        books_frame.pack()

        book_store= ttk.Treeview(books_frame)

        book_store.pack()

        book_store['columns'] = ('ID', 'Author', 'Title', 'Publisher', 'Price')

        book_store.column("#0", width=0, stretch=tkinter.NO)
        book_store.column("ID", anchor=tkinter.W, width=80)
        book_store.column("Author", anchor=tkinter.W, width=200)
        book_store.column("Title", anchor=tkinter.W, width=270)
        book_store.column("Publisher", anchor=tkinter.W, width=80)
        book_store.column("Price", anchor=tkinter.W, width=80)

        book_store.heading("#0", text="", anchor=tkinter.W)
        book_store.heading("ID", text="ID", anchor=tkinter.W)
        book_store.heading("Author", text="Автор", anchor=tkinter.W)
        book_store.heading("Title", text="Название", anchor=tkinter.W)
        book_store.heading("Publisher", text="Издатель", anchor=tkinter.W)
        book_store.heading("Price", text="Цена", anchor=tkinter.W)

        # удалить значения строки поиска
        def search_delete():
            if lst_for_id:
                book_store.delete(*book_store.get_children())
                MultipleDelete(lst_for_id)


        del_btn = Button(ws_search, text="Удалить", command=lambda:[search_delete(), refresh()])
        del_btn.pack(pady=10)



    # кнопочки
    Input_button = Button(ws, text="Добавить запись", command=input_record)
    Input_button.pack()

    select_button = Button(ws, text="Выбрать запись", command=select_record)
    select_button.pack(pady=10)

    edit_button = Button(ws, text="Редактировать", command=update_record)
    edit_button.pack(pady=10)

    delete_button = Button(ws, text="Удалить", command=delete_record)
    delete_button.pack(pady=10)

    open_button = Button(ws, text="Открыть", command=open_database)
    open_button.place(x=905, y=45)

    save_button = Button(ws, text="Сохранить", command=save_database)
    save_button.place(x=900, y=80)

    clean_button = Button(ws, text="Очистить", command=clean_database)
    clean_button.place(x=905, y=116)

    backup_button = Button(ws, text=" Создать \n backup ", command=create_backup)
    backup_button.place(x=907, y=157)

    restore_button = Button(ws, text=" Восстановить \n backup ", command=restore_backup)
    restore_button.place(x=890, y=215)

    search_button = Button(ws, text="Поиск", command=search_data)
    search_button.place(x=905, y=270)
    ws.mainloop()