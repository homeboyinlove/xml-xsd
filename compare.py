from lxml import etree

# Загрузка XML-документа
xml_file = 'menu.xml'
xml_doc = etree.parse(xml_file)

# Загрузка XSD-схемы как байтовый поток
xsd_file = 'menu.xsd'
with open(xsd_file, 'rb') as schema_file:  # Открываем файл в бинарном режиме
    schema_root = etree.XML(schema_file.read())

schema = etree.XMLSchema(schema_root)


is_valid = schema.validate(xml_doc)

# Результат
if is_valid:
    print("XML соответствует XSD-схеме")
else:
    print("XML не соответствует XSD-схеме")
    log = schema.error_log
    for error in log:
        print(error.message)
