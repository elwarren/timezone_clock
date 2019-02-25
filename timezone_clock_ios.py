import datetime
import pytz
from scene import *

frame_interval = 30


def get_tz_text(timezones=(("Etc/UTC", "UTC"))):
    clock_text = ''
    for tz in timezones:
        clock_text = clock_text + "{} {}\n".format(datetime.datetime.now().astimezone(pytz.timezone(tz[0])).strftime("%H:%M:%S.%f")[:-3], tz[1])
    return clock_text


class MyScene (Scene):
    def setup(self):
        self.background_color = 'white'
        self.clock = LabelNode('00:00:00.000', font=('Verdana', 24), color='black')
        self.clock.position = self.size / 2
        self.add_child(self.clock)

    def update(self):
        clock_text = get_tz_text(timezones=(("Europe/Paris", "Amsterdam"),
                                            ("Etc/UTC", "UTC"),
                                            ("America/New_York", "New York"),
                                            ("America/Chicago", "Chicago"),
                                            ("America/Denver", "Denver"),
                                            ("America/Los_Angeles", "San Francisco")))
        self.clock.text = clock_text


if __name__ == "__main__":
    run(MyScene(), PORTRAIT, frame_interval=frame_interval, show_fps=True)
