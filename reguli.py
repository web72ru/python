
import re

s = 'auuthor=Пушкин А.С.; title = Евгений; price =<img alt="sdugsdg" src="ssdgdgsg>" >'

итог = re.findall(r'(<.*?)(:?.|\n)*?(>)(.*?)(<\/.*?>)+', s)

print(итог)