# World population by hemisphere

total = 8000000000
north = 7200000000

south = total - north

north_percent = north / total * 100
south_percent = south / total * 100

print("World population:", total)
print("Northern Hemisphere:", north)
print("Northern Hemisphere in %:", north_percent)
print("Southern Hemisphere:", south)
print("Southern Hemisphere in %:", south_percent)