#Câu 1
import math
try:
    r=float(input("Mời bạn nhập bán kính hình tròn:"))
    cv=2*math.pi*r
    dt=r**2
    print("Chu vi =",cv)
    print("Diện tích=",dt)
except:
    print("Lỗi rồi!")

#câu 2
t=int(input("Nhập số giây:"))
hour=(t//3600)%24
minute=(t%3600)//60
second=(t%3600)%60
print(hour,":",minute,":",second)

#Câu 3
print("Chương trình tính điểm trung bình")
toan,ly,hoa=eval(input("Nhập điểm toán,lý,hóa:"))
print("Điểm toán=",toan)
print("Điểm lý=",ly)
print("Điểm hóa=",hoa)
dtb=(toan+ly+hoa)/3
print("Điểm trung bình=",dtb)
print("Điểm làm tròn=",round(dtb,2))

#Câu 4
#Có 8 kiểu dữ liệu cơ bản 
#Kiểu số 
#Kiểu chuỗi 
#Kiểu logic 
#Kiểu dãy
#Kiểu ánh xạ
#Kiểu tập hợp
#Kiểu nhị phân
#Kiểu none '''

#Câu 5
#Các loại ghi cú trong python
#Ghi chú 1 dòng #
#Ghi chú nhiều dòng dùng #, """...""" hoặc '''...'''

#Câu 6
#Ý nghĩa toán tử
#/: Chia thực
#//: Chia lấy phần nguyên
#%: Chia lấy phần dư
#**: Luỹ thừa
#and: Toán tử logic and
#or: Toán tử logic or
#is: So sánh đối tượng


#Câu 7
#Một số cách nhập từ bàn phím
#Nhập chuỗi (string)
#Nhập số nguyên (int)
#Nhập số thực (float)
#Nhập nhiều giá trị trên 1 dòng (slit)
#Nhập danh sách nhiều phần từ
#Nhập theo từng dòng nhiều dòng
#Đọc nhiều dòng đến khi người đọc kết thúc (EOF)

#Câu 8
#Các loại lỗi trong python
#Lỗi cú pháp
#Lỗi thời gian chạy
#Lỗi logic

#Cách bắt lỗi
#-Cú pháp cơ bản 
#try:
    # Khối có thể gây lỗi
#    ...
#except LỗiCụThể:
    # Cách xử lý khi có lỗi xảy ra
#    ...
#-Bắt nhiều loại lỗi
#try:
#    ...
#except (TypeError, ValueError):
#    print("Có lỗi kiểu dữ liệu hoặc giá trị không hợp lệ!")
#-Bắt lỗi không xác định
#try:
#    ...
#except Exception as e:
#    print("Đã xảy ra lỗi:", e)



#Câu 9
#| STT | Biểu thức                   | Kết quả               | Giải thích ngắn gọn                             |
#| --- | --------------------------- | --------------------- | ----------------------------------------------- |
#| a   | `i1 + (i2 * i3)`            | `-13`                 | 2 + (5 × -3) = 2 - 15                           |
#| b   | `i1 * (i2 + i3)`            | `4`                   | 2 × (5 + (-3)) = 2 × 2                          |
#| c   | `i1 / (i2 + i3)`            | `1.0`                 | 2 / (5 - 3) = 2 / 2                             |
#| d   | `i1 // (i2 + i3)`           | `1`                   | 2 // 2 = 1                                      |
#| e   | `i1 / i2 + i3`              | `-2.6`                | 2/5 + (-3) = 0.4 - 3                            |
#| f   | `i1 // i2 + i3`             | `-3`                  | 2 // 5 = 0; 0 + (-3) = -3                       |
#| g   | `3 + 4 + 5 / 3`             | `8.666666666666666`   | 5/3 = 1.666...; 3 + 4 + 1.666...                |
#| h   | `3 + 4 + 5 // 3`            | `8`                   | 5 // 3 = 1; 3 + 4 + 1                           |
#| i   | `(3 + 4 + 5) / 3`           | `4.0`                 | 12 / 3 = 4.0                                    |
#| j   | `(3 + 4 + 5) // 3`          | `4`                   | 12 // 3 = 4                                     |
#| k   | `d1 + (d2 * d3)`            | `-0.5`                | 2.0 + (5.0 × -0.5) = 2.0 - 2.5                  |
#| l   | `d1 + d2 * d3`              | `-0.5`                | Nhân trước: 5.0 × -0.5 = -2.5; 2.0 - 2.5        |
#| m   | `d1 / d2 - d3`              | `0.9`                 | 2.0 / 5.0 = 0.4; 0.4 - (-0.5) = 0.9             |
#| n   | `d1 / (d2 - d3)`            | `0.36363636363636365` | 2.0 / (5.5) ≈ 0.3636...                         |
#| o   | `d1 + d2 + d3 / 3`          | `6.833333333333333`   | -0.5 / 3 ≈ -0.166...; 2.0 + 5.0 - 0.166...      |
#| p   | `(d1 + d2 + d3) / 3`        | `2.1666666666666665`  | (2.0 + 5.0 - 0.5) / 3 = 6.5 / 3                 |
#| q   | `d1 + d2 + (d3 / 3)`        | `6.833333333333333`   | -0.5 / 3 = -0.166...; 2.0 + 5.0 - 0.166...      |
#| r   | `3 * (d1 + d2) * (d1 - d3)` | `52.5`                | 3 × (2 + 5) × (2 - (-0.5)) = 3 × 7 × 2.5 = 52.5 |

 
#Câu 10
#| STT | Lệnh gốc                                                  | Viết ngắn gọn                       |
#| --- | --------------------------------------------------------- | ----------------------------------- |
#| (a) | `x = x + 1`                                               | `x += 1`                            |
#| (b) | `x = x / 2`                                               | `x /= 2`                            |
#| (c) | `x = x - 1`                                               | `x -= 1`                            |
#| (d) | `x = x + y`                                               | `x += y`                            |
#| (e) | `x = x - (y + 7)`                                         | `x -= (y + 7)`                      |
#| (f) | `x = 2 * x`                                               | `x *= 2`                            |
#| (g) | `number_of_closed_cases = number_of_closed_cases + 2*ncc` | `number_of_closed_cases += 2 * ncc` |

