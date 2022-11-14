import requests
from lxml import etree
import lxml.html

def poluchit_html(url, params=''):
    r = requests.get(url, params=params)
    return r

url_1_tovara = 'https://loft4you.ru/catalog/hico_round_chandelier_2'

# Получаем хтмл страницы товара
html_1_tovara = poluchit_html(url_1_tovara)

# Делаем из хтмл страницы дерево (tree) всей страницы для парса
derevo_stranicy = lxml.html.document_fromstring(html_1_tovara.text)

# Получаем из дерева искпасом список элементов в виде объектов типа Element
spisok_objectov_Element_h1 = derevo_stranicy.xpath("//h1")

# Вытаскиваем из списка объектов первый объект
h1_object_Element = spisok_objectov_Element_h1[0]

# Обращаемся к атрибутам объекта text и tag
print('Текст:', h1_object_Element.text)
print('Название тэга:', h1_object_Element.tag)

# Делаем из объекта хтмл-текст при помощи функции etree.tostring() из модуля lxml
print('Преобразованный объект в HTML-текст:', etree.tostring(h1_object_Element, pretty_print=True))

