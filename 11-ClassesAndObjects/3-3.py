# 3-3: Change TV channel to 5
from tv import TV

tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.turn_off()
tv.show_status()
