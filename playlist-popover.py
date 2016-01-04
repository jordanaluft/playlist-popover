from gi.repository import Gtk

class App:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('playlist-popover.ui')

        self.window = self.builder.get_object('window')
        self.window.show_all()
        self.window.connect('delete-event', Gtk.main_quit)

        self.button = self.builder.get_object('button')
        self.button.connect('clicked', self.on_clicked_button)

        self.builder_popover = Gtk.Builder()
        self.builder_popover.add_from_file('popover.ui')

        self.popover = self.builder_popover.get_object('popover')
        self.popover.set_relative_to(self.button)

    def on_clicked_button(self, button):
        if self.popover.get_visible():
            self.popover.hide()
        else:
            self.popover.show()

    def start(self):
        Gtk.main()


def main():
    app = App()
    app.start()


if __name__ == '__main__':
    main()
