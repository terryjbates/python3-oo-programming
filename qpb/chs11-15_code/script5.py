import fileinput
def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            print("<start of file %s>" % fileinput.filename())
        print(line, end="")
main()

