from gi.repository import Gtk


TRACKS_FIXTURE = [
    (False, 'First Track', '2:23', True),
    (False, 'Second Track', '2:00', True),
    (False, 'Third Track', '3:42', True),
    (False, 'Fourth Track', '2:00', True),
    (False, 'Fifth Track', '4:50', True),
    (False, 'Sixth Track', '3:31', True),
    (True, 'Seventh Track', '2:40', False),
    (False, 'Eighth Track', '3:45', False),
    (False, 'Ninth Track', '4:00', False),
    (False, 'Tenth Track', '2:50', False),
    (False, 'Eleventh Track', '3:44', False),
]


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

        self.track_list = self.builder_popover.get_object('track_list')
        self.__populate_playlist()

    def __populate_playlist(self):
        for playing, track, time, played in TRACKS_FIXTURE:
            row = Gtk.ListBoxRow()
            label = Gtk.Label()
            text = '   {track:50}{time}'.format(
                track=track,
                time=time,
            )

            if played:
                label.set_markup('<span color="grey">{}</span>'.format(text))
            elif playing:
                label.set_label('P' + text[2:])
            else:
                label.set_label(text)

            label.set_xalign(0)
            row.add(label)
            self.track_list.add(row)
            self.track_list.show_all()

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
