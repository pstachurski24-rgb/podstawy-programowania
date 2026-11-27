# 3-4: Set and list available channels
from tv import TV

tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.show_channels()
tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
tv.show_channels()
tv.show_status()
tv.turn_off()
