from gi.repository import Gtk

class App:
    
    def __init__(self):
        self.window = Gtk.Window()
        self.window.show_all()
        self.window.connect("delete-event", Gtk.main_quit)
        
        

    def start(self):
        Gtk.main()
    
   


def main():
    app = App()
    app.start()


if __name__ == '__main__':
    main()

