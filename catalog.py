from lxml import etree

# Đường dẫn file
xml_file = "catalog.xml"
xsd_file = "catalog.xsd"

# Nạp file XML và XSD
xml_doc = etree.parse(xml_file)
xsd_doc = etree.parse(xsd_file)

# Tạo đối tượng schema
schema = etree.XMLSchema(xsd_doc)

# Kiểm tra hợp lệ
if schema.validate(xml_doc):
    print("✅ XML hợp lệ với XSD.")
else:
    print("❌ XML KHÔNG hợp lệ!")
    print(schema.error_log)
