
import re

s = 'auuthor=Пушкин А.С.; title = Евгений; price =<img alt="sdugsdg" src="ssdgdgsg>" >'

итог = re.findall(r'(\w+)=|\s=\s|\s=(.*);|\s', s)

print(итог)