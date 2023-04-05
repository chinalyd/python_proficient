def xie():
    print("Wait to receive the processing task...")
    while True:
        data = (yield)
        print('Receive the task: ',data)
def producer():
    c = xie()
    c.__next__()
    for i in range(3):
        print("Send a task...", 'Task %d'%i)
        c.send('Task %d'%i)
if __name__ == '__main__':
    producer()

