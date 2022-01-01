from requests import get
from bs4 import BeautifulSoup as bs

html = get("https://en.wikipedia.org/wiki/X86_instruction_listings").text
soup = bs(html, "html.parser")
instructions = []

tables = soup.find_all("table")
for e in tables:

    h = e.find("thead")
    if type(h) == None:
        h = 1
    else:
        h = 0

    table = e.find("tbody").find_all("tr")
    for i in range(h, len(table)):
        td = table[i].find_all("td")
        if len(td) != 0:
            try:
                instructions.append(td[0].text)
            except:
                print("fail")

with open("ins.txt", 'w+') as f:
    for i in instructions:
        f.write(i.replace('\n', '').split(' ')[0] + '\n')

print("[")
for e in range(256):
    if (e > 47 and e < 58) or (e > 64 and e < 94 and e != 92) or (e > 96 and e < 123) or (e == 95):
        print("\"" + chr(e) + "\"" + ",")
print("]")
