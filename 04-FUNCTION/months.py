
def month(n):
    names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    if 1 <= n <= 12:
        return names[n - 1]

    return "Invalid month"
