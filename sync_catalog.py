from lxml import etree
import sqlite3

# -------------------------------
# 1️⃣ Kiểm tra hợp lệ XML với XSD
# -------------------------------
xml_file = "catalog.xml"
xsd_file = "catalog.xsd"

xml_doc = etree.parse(xml_file)
xsd_doc = etree.parse(xsd_file)
schema = etree.XMLSchema(xsd_doc)

if not schema.validate(xml_doc):
    print("❌ XML KHÔNG hợp lệ!")
    print(schema.error_log)
    exit()

print("✅ XML hợp lệ với XSD, bắt đầu đồng bộ dữ liệu...")

# -------------------------------
# 2️⃣ Kết nối SQLite và tạo bảng
# -------------------------------
conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    currency TEXT NOT NULL,
    stock INTEGER NOT NULL,
    category_id TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES Categories(id)
)
""")
conn.commit()

# -------------------------------
# 3️⃣ Xử lý namespace và đọc XML
# -------------------------------
root = xml_doc.getroot()

# Khai báo namespace dictionary (đặt alias là “ns”)
ns = {"ns": "http://www.w3schools.com"}

# Đọc categories
for cat in root.findall(".//ns:category", ns):
    cat_id = cat.get("id")
    cat_name = cat.text.strip() if cat.text else ""

    cursor.execute("""
        INSERT INTO Categories (id, name)
        VALUES (?, ?)
        ON CONFLICT(id) DO UPDATE SET
            name = excluded.name
    """, (cat_id, cat_name))

# Đọc products
for prod in root.findall(".//ns:product", ns):
    prod_id = prod.get("id")
    category_ref = prod.get("categoryRef")
    name = prod.findtext("ns:name", default="", namespaces=ns).strip()
    price_elem = prod.find("ns:price", ns)
    price = float(price_elem.text.strip()) if price_elem is not None else 0
    currency = price_elem.get("currency") if price_elem is not None else ""
    stock_text = prod.findtext("ns:stock", default="0", namespaces=ns)
    stock = int(stock_text.strip())

    cursor.execute("""
        INSERT INTO Products (id, name, price, currency, stock, category_id)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            name = excluded.name,
            price = excluded.price,
            currency = excluded.currency,
            stock = excluded.stock,
            category_id = excluded.category_id
    """, (prod_id, name, price, currency, stock, category_ref))

conn.commit()
conn.close()

print("✅ Đồng bộ dữ liệu thành công vào database 'shop.db'")
