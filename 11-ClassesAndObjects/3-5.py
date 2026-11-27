# 3-5: Channel numbers and names; minimum seven channels
from tv import TV

tv = TV()
tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery', 'TVP Sport'])
tv.turn_on()
for channel in [4, 1, 7, 10]:
    tv.set_channel(channel)
    tv.show_status()
