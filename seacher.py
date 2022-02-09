import requests
from bs4 import BeautifulSoup
import time
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

while True:
    abc = ["https://cracked.io/Forum-C-C-VB-NET?page=1","https://cracked.io/Forum-Upgraded-Tools?page=1","https://cracked.io/Forum-Buyers-bay?page=1"]
    for ii in abc:
        url = ii
        y = requests.get(url)
        s = BeautifulSoup(y.content, "lxml")
        b = s.find_all("tr", attrs = {"class":"inline_row forum2"})

        with open('TestFile.txt', 'w' , encoding="utf8") as f:
            for i in b:
                q = f"{i.a.text}\n"
                f.write(q)

        def stringss(qw, ert):
            num = 0
            results = []
            with open(qw, 'r', encoding='utf8') as l:
                for line in l:
                    num += 1
                    for search in ert:
                        if search in line:
                            results.append((search, num, line.rstrip()))
            return results

        with open('Finish.txt', 'w', encoding="utf8") as file:
            file.write(ii)
            matched_lines = stringss('TestFile.txt', ['c++', 'tool', 'tools', 'Yahoo', 'buy', 'for', 'Remote Administration Tool', 'RAT', 'Hidden Rootkit','$'])
            xy = ('\n\nTotal Matched lines : ' + str(len(matched_lines)))
            file.write(xy)
            for elem in matched_lines:
                xz = (('\n-'*1)+'\nWord = ' + str(elem[0]) + '\nLine Number = ' + str(elem[1]) + '\nLine = ' + str(elem[2]))
                file.write(xz)

        with open("Finish.txt", encoding="utf8") as file:
            mesa = file.read()
            urll = "https://api.telegram.org/bot"+ parser.get('conf','token') +"/sendMessage"
            dataa = {"chat_id":parser.get('conf','id'), "text":mesa}
            a = requests.post(urll, dataa).json

    time.sleep(3600)


