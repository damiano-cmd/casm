from sys import argv

def translate(lines):
    for i in lines:
        i = i.replace('\n', '')
        sections = filter(lambda x: x != '', i.split(" "))
        print(list(sections))

argv.pop(0)
if len(argv) < 1:
    print("No arguments!!!!!")
    exit(1)

with open(argv[0], 'r') as f:
    translate((f.readlines()))