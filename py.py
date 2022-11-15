import lxml.html

html_tovara = """
      <ul class="list-unstyled" id="product_options">\r\n                                                                <li><strong>Артикул:</strong> <span itemprop="sku">L03196</span></li>\r\n                                                                                            <li><strong>Материал:</strong> Стекло, Металл </li>\r\n                                                    <li><strong>Стиль:</strong> Современный, Лофт </li>\r\n                                                    <li><strong>Цоколь:</strong> LED </li>\r\n                                                    <li><strong>Место использования:</strong> кухня, кабинет, гостиная, бар, кафе, ресторан </li>\r\n                                                                                        <li><strong>Производитель:</strong> Loft4You (Китай)</li>\r\n                                                        </ul>
      """
tree = lxml.html.document_fromstring(html_tovara.text)
html_tovara = tree.xpath('//li')

list = []
for line in html_tovara.split("\n"):
    if not line.strip():
            continue
    list.append(line.lstrip())

print(list)