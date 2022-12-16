import tkinter
from tkinter import ttk
import socket

class Looker(ttk.Frame):
    """The gui functions and dns lookup"""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
    def init_gui(self):
        """Builds gui"""
        self.root.title("DNS Looker")
        self.grid(column=0, row=0, sticky='nsew')
       # self.pack(fill='both', padx=10, pady=5)
        #ttk.Label(self, text='DNS Lookup').pack(pady='5')
     #    ttk.Label(self, text='DNS').pack(side='left', padx=5, pady=5)
        self.dns_addr = ttk.Entry(self, width=20)
        self.dns_addr.pack(side='left', padx=5, pady=5)
        self.dns_addr.grid(column=1, row=2)

        self.dnslkup_button = ttk.Button(self, text='DNS Lookup', command=self.dnslookup)
        self.dnslkup_button.grid(column=0, row=3, columnspan=4)
        self.reslv_frame = ttk.LabelFrame(self, text='Resolver:', height=100)
        self.reslv_frame.grid(column=0, row=4,columnspan=4, sticky='nsew')
        self.reslv_label = ttk.Label(self.reslv_frame, text='')
        self.reslv_label.grid(column=0, row=0)

        ttk.Separator(self, orient='horizontal').grid(column=0, row=1, columnspan=4, sticky='ew')
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.root.option_add('*tearOff', 'FALSE')
        self.menubar = tkinter.Menu(self.root)
        self.menu_file = tkinter.Menu(self.menubar)
       # self.menu_edit = tkinter.Menu(self.menubar)

        self.menu_file = tkinter.Menu(self.menubar)
        self.menu_file.add_command(label='Exit', command=self.on_quit)

        self.menubar.add_cascade(menu=self.menu_file, label='File')
        #self.menubar.add_cascade(menu=self.menu_edit, label='Edit')


        self.root.config(menu=self.menubar)

    def on_quit(self):
        """Exits program"""
        quit()

    def dnslookup(self):
        self.dns_addr = socket.gethostbyname(self.dns_addr.get())
        reslvd = self.dns_addr
        self.reslv_label['text'] = reslvd






if __name__ == '__main__':
    root = tkinter.Tk()
    Looker(root)
    root.mainloop()