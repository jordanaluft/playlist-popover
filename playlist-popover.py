from gi.repository import Gtk
from random import randint


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
    (False, 'Fifth Track', '4:50', True),
    (False, 'Sixth Track', '3:31', True),
    (True, 'Seventh Track', '2:40', False),
    (False, 'Eighth Track', '3:45', False),
    (False, 'Ninth Track', '4:00', False),
    (False, 'Tenth Track', '2:50', False),
    (False, 'Eleventh Track', '3:44', False)
]


class App:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('playlist-popover.ui')

        self.window = self.builder.get_object('window')
        self.window.show_all()
        self.window.connect('delete-event', Gtk.main_quit)

        self.button = self.builder.get_object('nowplaying_button')
        self.button.connect('clicked', self.on_clicked_button)

        self.popover = self.builder.get_object('popover')
        self.popover.set_relative_to(self.button)

        self.track_list = self.builder.get_object('track_list')
        self.__populate_playlist()

        self.stack = self.builder.get_object('stack3')

        self.button.connect('clicked', self.on_clicked_stack)

        self.box2 = self.builder.get_object('box2')
        self.box1 = self.builder.get_object('box1')
        self.box_content = self.builder.get_object('box_content')

    def __populate_playlist(self):
        for playing, track, time, played in TRACKS_FIXTURE:
            row = Gtk.ListBoxRow()
            box_track = Gtk.Box()
            row.add(box_track)

            track_label = Gtk.Label()
            time_label = Gtk.Label()

            if played:
                padding = 16
                track_label.set_markup('<span color="grey">{}</span>'.format(track))
                time_label.set_markup('<span color="grey">{}</span>'.format(time))
            elif playing:
                padding = 0
                image = Gtk.Image.new_from_icon_name('media-playback-start', 1)
                box_track.pack_start(image, False, False, 0)
                track_label.set_label(track)
                time_label.set_label(time)
            else:
                padding = 16
                track_label.set_label(track)
                time_label.set_label(time)

            box_track.pack_start(track_label, False, False, padding)
            box_track.reorder_child(track_label, 1)
            box_track.pack_end(time_label, False, False, 20)
            box_track.reorder_child(time_label, 2)

            self.track_list.add(row)
            self.track_list.show_all()

    def on_clicked_button(self, button):
        if self.popover.get_visible():
            self.popover.hide()
        else:
            self.popover.show()

    def start(self):
        Gtk.main()

    def on_clicked_stack(self, button):
        value = randint(0, 2)
        if value == 0:
            self.stack.set_visible_child(self.box2)
        if value == 1:
            self.stack.set_visible_child(self.box1)
        if value == 2:
            self.stack.set_visible_child(self.box_content)


def main():
    app = App()
    app.start()


if __name__ == '__main__':
    main()
