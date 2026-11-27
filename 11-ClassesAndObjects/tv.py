# Full-featured TV object used by tv_show.py
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        if isinstance(new_channel_no, int) and new_channel_no >= 1:
            self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = list(channels_list)

    def show_channels(self):
        print('Channel list:')
        for index, name in enumerate(self.channels, start=1):
            print(f'{index}. {name}')

    def volume_up(self):
        self.volume = min(10, self.volume + 1)

    def volume_down(self):
        self.volume = max(0, self.volume - 1)

    def show_status(self):
        if not self.is_on:
            print('TV is off')
            return
        name = self.channels[self.channel_no-1] if 1 <= self.channel_no <= len(self.channels) else None
        extra = f' ({name})' if name else ''
        print(f'TV is on, channel {self.channel_no}{extra}, volume {self.volume}')
