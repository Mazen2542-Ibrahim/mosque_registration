from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import Database
import tkintermapview

db = Database('mosques.db')


class Mosques:
    def __init__(self):
        self.root = Tk()
        self.root.title('  Mosques Management System')
        self.width, self.height = 1100, 450
        self.s_width = (self.root.winfo_screenwidth() // 2) - (self.width // 2)
        self.s_height = (self.root.winfo_screenheight() // 2) - (self.height // 2)
        self.root.geometry(f'{self.width}x{self.height}+{self.s_width}+{self.s_height}')
        # self.root.resizable(False, False)
        self.root.iconbitmap('images/mosque.ico')
        self.window_counter = 0
        self.search_frame()
        self.entry_frame()
        self.buttons_frame()
        self.table_frame()
        self.display_all()

    def search_frame(self):
        search_frame = Frame(self.root, bg='gray')
        search_frame.pack(anchor=NW, padx=5, pady=5, fill=BOTH)
        self.e_search = StringVar()
        Button(search_frame, text='Search by name', relief=FLAT, font=('Helvetica', 13, 'bold'),
               command=self.search_by_name).grid(row=0, column=0, padx=10, pady=5)
        search_entry = Entry(search_frame, textvariable=self.e_search, relief=FLAT,
                             font=('Helvetica', 12, 'bold')).grid(row=0, column=1, padx=(0, 5), pady=5)
        Label(search_frame, text='Mosques Management System', font=('Helvetica', 16, 'bold'), bg='gray').grid(row=0,
                                                                                                              column=2,
                                                                                                              padx=200,
                                                                                                              pady=5)

    def entry_frame(self):
        self.e_id = StringVar()
        self.e_name = StringVar()
        self.e_type = StringVar()
        self.e_address = StringVar()
        self.e_coordinates = StringVar()
        self.e_imam_name = StringVar()

        # Label(self.root, image='images/m.png', width=66, height=10, bg='gray').place(x=627, y=53)

        options = ['  صغير  ', '  جامع  ']
        self.e_type.set(options[0])

        entry_frame = Frame(self.root, bg='gray')
        entry_frame.pack(anchor=NW, padx=5, pady=(0, 5))

        Label(entry_frame, text='ID', font=('Helvetica', 12, 'bold'), bg='gray').grid(row=0, column=0, padx=(5, 10),
                                                                                      pady=5)
        id_entry = Entry(entry_frame, textvariable=self.e_id, relief=FLAT, font=('Helvetica', 12, 'bold'),
                         state=DISABLED).grid(row=0, column=1, padx=(0, 5), pady=5)

        Label(entry_frame, text='Name', font=('Helvetica', 12, 'bold'), bg='gray').grid(row=0, column=2, padx=(20, 10),
                                                                                        pady=5)
        name_entry = Entry(entry_frame, textvariable=self.e_name, relief=FLAT, font=('Helvetica', 12, 'bold')).grid(
            row=0, column=3, padx=(0, 5), pady=5)

        Label(entry_frame, text='Type', font=('Helvetica', 12, 'bold'), bg='gray').grid(row=1, column=0, padx=(10, 10),
                                                                                        pady=5)
        OptionMenu(entry_frame, self.e_type, *options).grid(row=1, column=1, padx=(0, 5), pady=5)

        Label(entry_frame, text='Address', font=('Helvetica', 12, 'bold'), bg='gray').grid(row=1, column=2,
                                                                                           padx=(5, 10), pady=5)
        address_entry = Entry(entry_frame, textvariable=self.e_address, relief=FLAT,
                              font=('Helvetica', 12, 'bold')).grid(row=1, column=3, padx=(0, 5), pady=5)

        Label(entry_frame, text='Imam name', font=('Helvetica', 12, 'bold'), bg='gray').grid(row=2, column=0,
                                                                                             padx=(20, 10), pady=5)
        imam_name_entry = Entry(entry_frame, textvariable=self.e_imam_name, relief=FLAT,
                                font=('Helvetica', 12, 'bold')).grid(row=2, column=1, padx=(0, 5), pady=5)

        Label(entry_frame, text='Coordinates', font=('Helvetica', 12, 'bold'), bg='gray').grid(row=2, column=2,
                                                                                               padx=(5, 10), pady=5)
        coordinates_entry = Entry(entry_frame, textvariable=self.e_coordinates, relief=FLAT,
                                  font=('Helvetica', 12, 'bold')).grid(row=2, column=3, padx=(0, 5), pady=5)

    def buttons_frame(self):
        buttons_frame = Frame(self.root, bg='gray')
        buttons_frame.pack(anchor=NW, padx=5)

        disp_all = Button(buttons_frame, text='Display All', relief=FLAT, font=('Helvetica', 13, 'bold'),
                          command=self.display_all)
        disp_all.grid(row=0, column=0, padx=10, pady=5)
        add = Button(buttons_frame, text='Add Entry', relief=FLAT, font=('Helvetica', 13, 'bold'),
                     command=self.add_entry)
        add.grid(row=0, column=1, padx=(0, 10), pady=5)
        update = Button(buttons_frame, text='Update Entry', relief=FLAT, font=('Helvetica', 13, 'bold'),
                        command=self.update_entry)
        update.grid(row=0, column=2, padx=(0, 10), pady=5)
        delete = Button(buttons_frame, text='Delete Entry', relief=FLAT, font=('Helvetica', 13, 'bold'),
                        command=self.delete_entry)
        delete.grid(row=0, column=3, padx=(0, 10), pady=5)
        on_map = Button(buttons_frame, text='Display on map', relief=FLAT, font=('Helvetica', 13, 'bold'),
                        command=self.display_no_map)
        on_map.grid(row=0, column=4, padx=(0, 10), pady=5)

    def table_frame(self):
        self.table_frame = Frame(self.root, bg='gray')
        self.table_frame.pack(anchor=NW, padx=5, pady=5, fill=BOTH, expand=True)
        scrollbar = Scrollbar(self.table_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.table = ttk.Treeview(self.table_frame, yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.table.yview)
        self.table['columns'] = ('ID', 'Type', 'Name', 'Address', 'Coordinate', 'Imam name')
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('ID', anchor=CENTER, width=12)
        self.table.column('Type', anchor=W, width=120)
        self.table.column('Name', anchor=W, width=120)
        self.table.column('Address', anchor=W, width=120)
        self.table.column('Coordinate', anchor=W, width=160)
        self.table.column('Imam name', anchor=W, width=120)

        self.table.heading('#0', text='')
        self.table.heading('ID', text='ID', anchor=CENTER)
        self.table.heading('Type', text='Type', anchor=W)
        self.table.heading('Name', text='Name', anchor=W)
        self.table.heading('Address', text='Address', anchor=W)
        self.table.heading('Coordinate', text='Coordinate', anchor=W)
        self.table.heading('Imam name', text='Imam name', anchor=W)
        self.table.pack(expand=True, fill=BOTH, padx=5, pady=5)

        # bind list select
        self.table.bind('<<TreeviewSelect>>', self.select_item)

    def add_entry(self):
        if self.e_name.get() == '' or self.e_type.get() == '' or self.e_address.get() == '' or self.e_coordinates.get() == '' or self.e_imam_name.get() == '':
            messagebox.showerror('Required Fields', 'Please include all fields')
            return
        db.insert(self.e_name.get(), self.e_type.get(), self.e_address.get(), self.e_coordinates.get(),
                  self.e_imam_name.get())
        self.table.delete(*self.table.get_children())
        self.table.insert('', END, values=(
            self.e_name.get(), self.e_type.get(), self.e_address.get(), self.e_coordinates.get(),
            self.e_imam_name.get()))
        self.clear_entry()
        self.display_all()

    def update_entry(self):
        if self.e_name.get() == '' or self.e_type.get() == '' or self.e_address.get() == '' or self.e_coordinates.get() == '' or self.e_imam_name.get() == '':
            messagebox.showerror('Error', 'Please selected a recored', parent=self.root)
            return
        else:
            db.update(self.row[0], self.e_name.get(), self.e_type.get(), self.e_address.get(),
                      self.e_coordinates.get(), self.e_imam_name.get())
            self.display_all()

    def select_item(self, event):
        self.clear_entry()
        selected = self.table.selection()
        contents = self.table.item(selected)
        self.row = contents['values']
        self.e_id.set(self.row[0])
        self.e_type.set(self.row[1])
        self.e_name.set(self.row[2])
        self.e_address.set(self.row[3])
        self.e_coordinates.set(self.row[4])
        self.e_imam_name.set(self.row[5])



    def delete_entry(self):
        if self.e_name.get() == '' or self.e_type.get() == '' or self.e_address.get() == '' or self.e_coordinates.get() == '' or self.e_imam_name.get() == '':
            messagebox.showerror('Error', 'Please selected a recored', parent=self.root)
            return
        else:
            self.clear_entry()
            db.delete(self.row[0])
            self.display_all()

    def display_all(self):
        self.table.delete(*self.table.get_children())
        records = db.display()
        for i, row in enumerate(records, start=1):
            self.table.insert('', END, values=(row[0], row[2], row[1], row[3], row[4], row[5]))

    def search_by_name(self):
        search_v = self.e_search.get()
        self.table.delete(*self.table.get_children())
        records = db.search(search_v)
        for i, row in enumerate(records, start=1):
            self.table.insert('', END, values=(row[0], row[2], row[1], row[3], row[4], row[5]))
        self.clear_entry()

    def display_no_map(self):
        if self.e_name.get() == '' or self.e_type.get() == '' or self.e_address.get() == '' or self.e_coordinates.get() == '' or self.e_imam_name.get() == '':
            messagebox.showerror('Error', 'Please selected a recored', parent=self.root)
            return
        else:
            if self.window_counter < 1:
                self.window_counter += 1
                self.map_win = Toplevel()
                self.map_win.title('Map')
                self.map_win.iconbitmap('images/map.ico')
                self.map_win.geometry('500x500')
                map_label = Label(self.map_win)
                map_label.pack(expand=True, fill=BOTH, pady=(30, 5), padx=5)

                map = tkintermapview.TkinterMapView(map_label, corner_radius=0)
                map.pack(expand=True, fill=BOTH)
                map.set_position(26.3592, 43.9818)
                map.set_zoom(11)
                coordinates = self.e_coordinates.get().split(',')
                map.set_marker(float(coordinates[0]), float(coordinates[1]), text=self.e_name.get())
                self.map_win.protocol('WM_DELETE_WINDOW', self.closed_window)
            else:
                messagebox.showerror('Error', 'Please close map window', parent=self.map_win)

    def clear_entry(self):
        self.e_id.set('')
        self.e_name.set('')
        self.e_type.set('')
        self.e_address.set('')
        self.e_coordinates.set('')
        self.e_imam_name.set('')
        self.e_search.set('')

    def closed_window(self):
        self.map_win.destroy()
        self.window_counter = 0

    def run(self):
        self.root.mainloop()


Mosques().run()
