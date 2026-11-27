from collections import deque
waiting = deque()
next_ticket = 1
while True:
    print('1. New customer   2. Serve next   0. Quit')
    command = input('Choose: ').strip()
    if command == '1':
        waiting.append(next_ticket)
        print('Ticket number:',next_ticket)
        next_ticket += 1
    elif command == '2':
        if waiting: print('Serving ticket:',waiting.popleft())
        else: print('No customers waiting')
    elif command == '0': break
    else: print('Invalid option')
