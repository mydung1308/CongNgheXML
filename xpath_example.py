from lxml import etree

# Đọc file XML
tree = etree.parse("sv.xml")

# ===== Ví dụ các câu XPath =====

# 1. Lấy tất cả sinh viên
students = tree.xpath("/school/student")
print("Tổng số sinh viên:", len(students))

# 2. Liệt kê tên tất cả sinh viên
names = tree.xpath("/school/student/name/text()")
print("Tên sinh viên:", names)


# 3. Lấy tất cả id của sinh viên
ids = tree.xpath("/school/student/id/text()")
print("Tất cả ID sinh viên:", ids)

# 4. Lấy ngày sinh SV01
birth_sv01 = tree.xpath("/school/student[id='SV01']/date/text()")
print("Ngày sinh SV01:", birth_sv01)

# 5. Lấy các khóa học
courses = tree.xpath("/school/enrollment/course/text()")
print("Các khóa học:", courses)

# 6. Lấy toàn bộ thông tin của sinh viên đầu tiên
first_student = tree.xpath("/school/student[1]")
print("Thông tin sinh viên đầu tiên:")
print(etree.tostring(first_student[0], pretty_print=True, encoding="unicode"))


# 7. Lấy mã sinh viên sinh viên học môn Vatly203 -------
names_vatly = tree.xpath("/school/enrollment[course='Vatly203']/studentRef")
print("Sinh viên học Vatly203:", names_vatly)


# 8. Lấy tên sinh viên học môn "Toan101"
name_toan = tree.xpath("/school/student[id=/school/enrollment[course='Toan101']/studentRef]/name/text()")
print("Sinh viên học Toan101:", name_toan)


# 9. Lấy tên sinh viên học môn "Vatly203"
name_vatly = tree.xpath("/school/student[id=/school/enrollment[course='Vatly203']/studentRef]/name/text()")
print("Sinh viên học Vatly203:", name_vatly)

# 10. Lấy ngày sinh của sinh viên có id="SV01"
birth_sv01 = tree.xpath("/school/student[id='SV01']/date/text()")
print("Ngày sinh của SV01:", birth_sv01)

# 11. Lấy tên và ngày sinh sinh viên sinh năm 1997
info_1997 = tree.xpath("/school/student[starts-with(date, '1997')]/name/text()") + \
            tree.xpath("/school/student[starts-with(date, '1997')]/date/text()")
print("Sinh viên sinh năm 1997:", info_1997)

# 12. Lấy tên của các sinh viên có ngày sinh trước năm 1998
name_before_1998 = tree.xpath("/school/student[number(substring(date,1,4)) < 1998]/name/text()")
print("Sinh viên sinh trước năm 1998:", name_before_1998)

# 13. Đếm tổng số sinh viên
count_students = tree.xpath("count(/school/student)")
print("Tổng số sinh viên:", int(count_students))

from lxml import etree

# Đọc file XML
tree = etree.parse("sv.xml")

# ===== CÁC TRUY VẤN XPATH =====

# 1. Lấy tất cả id của sinh viên
ids = tree.xpath("/school/student/id/text()")
print("Tất cả ID sinh viên:", ids)

# 2. Lấy các khóa học
courses = tree.xpath("/school/enrollment/course/text()")
print("Các khóa học:", courses)

# 3. Lấy toàn bộ thông tin của sinh viên đầu tiên
first_student = tree.xpath("/school/student[1]")
print("Thông tin sinh viên đầu tiên:")
print(etree.tostring(first_student[0], pretty_print=True, encoding="unicode"))

# 4. Lấy tên sinh viên học môn "Toan101"
name_toan = tree.xpath("/school/student[id=/school/enrollment[course='Toan101']/studentRef]/name/text()")
print("Sinh viên học Toan101:", name_toan)

# 5. Lấy tên sinh viên học môn "Vatly203"
name_vatly = tree.xpath("/school/student[id=/school/enrollment[course='Vatly203']/studentRef]/name/text()")
print("Sinh viên học Vatly203:", name_vatly)

# 6. Lấy ngày sinh của sinh viên có id="SV01"
birth_sv01 = tree.xpath("/school/student[id='SV01']/date/text()")
print("Ngày sinh của SV01:", birth_sv01)

# 7. Lấy tên của các sinh viên có ngày sinh trước năm 1998
name_before_1998 = tree.xpath("/school/student[number(substring(date,1,4)) < 1998]/name/text()")
print("Sinh viên sinh trước năm 1998:", name_before_1998)



# ===== Thêm 2 sinh viên mới =====
root = tree.getroot()

# Sinh viên 4
new_stu1 = etree.SubElement(root, "student")
etree.SubElement(new_stu1, "id").text = "SV04"
etree.SubElement(new_stu1, "name").text = "Trần Văn Nam"
etree.SubElement(new_stu1, "date").text = "1999-05-10"

# Sinh viên 5
new_stu2 = etree.SubElement(root, "student")
etree.SubElement(new_stu2, "id").text = "SV05"
etree.SubElement(new_stu2, "name").text = "Trần Thị Hoa"
etree.SubElement(new_stu2, "date").text = "2000-02-15"

# Lưu lại file (ghi đè)
tree.write("sv.xml", pretty_print=True, encoding="utf-8")

# 8. Lấy tất cả sinh viên chưa đăng ký môn nào
students_no_course = tree.xpath("/school/student[not(id=/school/enrollment/studentRef)]/name/text()")
print("Sinh viên chưa đăng ký môn nào:", students_no_course)

# 9. Lấy phần tử <date> anh em ngay sau <name> của SV01
date_after_name = tree.xpath("/school/student[id='SV01']/name/following-sibling::date[1]/text()")
print("Phần tử <date> ngay sau <name> của SV01:", date_after_name)

# 10. Lấy phần tử <id> anh em ngay trước <name> của SV02
id_before_name = tree.xpath("/school/student[id='SV02']/name/preceding-sibling::id[1]/text()")
print("Phần tử <id> ngay trước <name> của SV02:", id_before_name)

# 11. Lấy toàn bộ node <course> trong cùng enrollment với studentRef='SV03'
course_sv03 = tree.xpath("/school/enrollment[studentRef='SV03']/course/text()")
print("Môn học của SV03:", course_sv03)

# 12. Lấy sinh viên có họ là “Trần”
name_tran = tree.xpath("/school/student[starts-with(name, 'Trần')]/name/text()")
print("Sinh viên họ Trần:", name_tran)

# 13. Lấy năm sinh của sinh viên SV01
year_sv01 = tree.xpath("substring(/school/student[id='SV01']/date, 1, 4)")
print("Năm sinh SV01:", year_sv01)

