# 3-6: TV volume within 0..10
from tv import TV

tv = TV()
tv.turn_on()
tv.show_status()
for _ in range(12):
    tv.volume_up()
tv.show_status()
for _ in range(15):
    tv.volume_down()
tv.show_status()
