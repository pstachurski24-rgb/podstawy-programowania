facebook = True
twitter = False
instagram = True

accounts = int(facebook) + int(twitter) + int(instagram)

if accounts >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")