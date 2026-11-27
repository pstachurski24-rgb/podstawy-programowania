history = []
current = None
while True:
    print('1. Visit page  2. Back  0. Quit')
    command = input('Choose: ').strip()
    if command == '0': break
    if command == '1':
        address = input('Website: ').strip()
        if address:
            if current is not None: history.append(current)
            current = address
            print('Now visiting:', current)
    elif command == '2':
        if history:
            current = history.pop()
            print('Back to:', current)
        else: print('No previous page')
    else: print('Invalid choice')
