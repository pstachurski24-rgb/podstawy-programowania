
polish_license_plates = [
    "KR5233F", "PO6987E", "KR16179", "BI7192L",
    "KK12255", "WA7930T", "SK6922I", "KK61108",
    "KR90538", "BI8052Q", "KK54985", "LU4864U"
]

counter = 1

for plate in polish_license_plates:
    if plate.startswith(("KR", "KK")):
        print(counter, plate)
        counter += 1
