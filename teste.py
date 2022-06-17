import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from bd import consultar


def agenda ():
    root = tk.Tk()
    root.title('Treeview demo')
    root.geometry('620x200')

    contatos = consultar(True)


    # define columns
    columns = ('first_name', 'last_name', 'email')

    tree = ttk.Treeview(root, columns=columns, show='headings')

    # define headings
    tree.heading('first_name', text='ID')
    tree.heading('last_name', text='Nome')
    tree.heading('email', text='Telefone')

    # generate sample data
    contacts = contatos



    # add data to the treeview
    for contact in contacts:
        tree.insert('', tk.END, values=contact)


    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))


    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

    # add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    # run the app
    root.mainloop()
