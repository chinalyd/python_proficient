import fileinput
def demo_fileinput():
    with fileinput.input(['123.txt', '456.txt']) as lines:
        for line in lines:
            print('Sum No.%d line, '%fileinput.lineno(), 'File %s No.%d line:'%(fileinput.filename(), fileinput.filelineno()))
            print(line.strip())
if __name__ == '__main__':
    demo_fileinput()
