#Câu 1
from random import randrange
print("Chương trình xử lý List")
n=int(input("Nhập số phần tử"))
lst=[0]*n
for i in range(n):
 lst[i]=randrange(-100,100)
print("List ngẫu nhiên là:")
print(lst)
print("Mời bạn thêm số mới:")
value=int(input())
lst.append(value)
print(lst)
print("bạn muốn đếm số nào:")
k=int(input())
dem=lst.count(k)
print(k,"xuất hiện ",dem,"trong list")
def CheckPrime(n):
    d=0
    for i in range(1,n+1):
         if n%i ==0:
             d+=1
    return d==2
demnt=0
tongnt=0
for x in lst:
    if CheckPrime(x):
        demnt+=1
        tongnt+=x
print("Có ",demnt,"số nguyên tố trong list")
print("Tổng=",tongnt)
lst.sort()
print("List sau khi sort:")
print(lst)
lst.clear()
print("List sau khi xóa:")
print(lst)


#Câu 2
from random import randrange
lst=[]
print("Nhập số phần tử:")
n=int(input())
for i in range(n):
    lst.append(randrange(0,100))
print("List sau khi tạo ngẫu nhiên là:")
print(lst)
x=int(input("Mời bạn chèn thêm số mới"))
lst.append(x)
print("List sau khi chèn:")
print(lst)
k=int(input("Mời nhập số để xóa"))
while lst.count(k)>0:
    lst.remove(k)
print("List sau khi xóa:")
print(lst)
def CheckDoiXung(lst):
    for i in range(len(lst)):
        if lst[i]!=lst[len(lst)-i-1]:
            return False
    return True
kt=CheckDoiXung(lst)
if kt==True:
 print("List đối xứng")
else:
 print("List không đối xứng")

 #Câu 3
 from random import randrange
def TaoMaTran(m,n):
    D=[]
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(randrange(100))
        D.append(row)
    return D
def XuatMaTran(D):
 for row in D:
    for element in row:
        print(element,end='\t')
    print()
def LayDong(r):
 R=D[r]
 return R
def XuatList1Chieu(R):
    for element in R:
        print(element,end='\t')
def LayCot(c):
 C=[]
 for i in range(len(D)):
   C.append(D[i][c])
 return C
def MAX(D):
 max=D[0][0]
 for i in range(len(D)):
    for j in range(len(D[i])):
        if(max<D[i][j]):
            max=D[i][j]
    return max
print("Nhập số dòng:")
m=int(input())
print("Nhập số cột:")
n=int(input())
D=TaoMaTran(m,n)
XuatMaTran(D)
print("Mời bạn nhập dòng muốn xuất:")
r=int(input())
XuatList1Chieu(LayDong(r))
print("Mời bạn nhập cột muốn xuất:")
c=int(input())
XuatList1Chieu(LayCot(c))
max=MAX(D)
print("Số lớn nhất trong ma trận=",max)

#Câu 4
#(a) lst[0] Phần tử ở vị trí 0 là 3 => Kết quả: 3
#(b) lst[3]  Phần tử ở vị trí 3 là 5 => Kết quả: 5
#(c) lst[x]  x = 2 → lst[2] = 1 => Kết quả: 1
#(d) lst[-x]  x = 2 → lst[-2] nghĩa là phần tử thứ 2 từ cuối, lst[-2] = 5 => Kết quả: 5
#(e) lst[x + 1]  x + 1 = 3 → lst[3] = 5 =>  Kết quả: 5
#(f) lst[x] + 1  lst[x] = 1 → 1 + 1 = 2 => Kết quả: 2
#(g) lst[lst[x]]  lst[x] = 1 → lst[1] = 0 => Kết quả: 0
#(h) lst[lst[lst[x]]] , lst[x] = 1,  lst[lst[x]] = lst[1] = 0, 
#lst[lst[lst[x]]] = lst[0] = 3 => Kết quả: 3

#Câu 5
#(a) lst => [20, 1, -34, 40, -8, 60, 1, 3]
#(b) lst[0:3] Lấy phần tử từ chỉ số 0 đến 2 (3 không lấy) => [20, 1, -34]
#(c) lst[4:8] Lấy phần tử từ chỉ số 4 đến 7 => [-8, 60, 1, 3]
#(d) lst[4:33] Bắt đầu từ chỉ số 4 đến 33 (nhưng danh sách chỉ có 8 phần tử → tự cắt đến hết) => [-8, 60, 1, 3]
#(e) lst[-5:-3] Danh sách: [20, 1, -34, 40, -8, 60, 1, 3], Chỉ số âm tương ứng: => [-8→-4], [60→-3], [1→-2], [3→-1]
#lst[-5:-3] = phần tử ở chỉ số -5 đến -4 (2 phần tử): =>  [40, -8]
#(f) lst[-22:3] Âm quá giới hạn → bắt đầu từ đầu danh sách đến phần tử có chỉ số 2 => [20, 1, -34]
#(g) lst[4:] Bắt đầu từ chỉ số 4 đến hết danh sách => [-8, 60, 1, 3]
#(h) lst[:] Sao chép toàn bộ danh sách => [20, 1, -34, 40, -8, 60, 1, 3]
#(i) lst[:4] Lấy phần tử từ đầu đến chỉ số 3 =>[20, 1, -34, 40]
#(j) lst[1:5] Lấy phần tử từ chỉ số 1 đến 4 => [1, -34, 40, -8]
#(k) -34 in lst: -34 có trong danh sách => True
#(l) -34 not in lst: -34 có trong danh sách → mệnh đề sai => False
#(m) len(lst) Số phần tử trong danh sách: 8

#Câu 6
import random

N = int(input("Nhập số lượng phần tử N: "))
lst = random.sample(range(1, 100), N)  
print("Danh sách ngẫu nhiên không trùng là:", lst)

#Câu 7
n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    if i > 0 and x <= lst[-1]:
        print("Sai thứ tự tăng dần, nhập lại từ đầu!")
        lst = []
        break
    lst.append(x)

if len(lst) == n:
    print("Dãy số hợp lệ:", lst)

#Câu 8
n = int(input("Nhập số lượng phần tử: "))
M = []

for i in range(n):
    x = float(input(f"Nhập M[{i}]: "))
    M.append(x)

M.sort(reverse=True)

print("Dãy sau khi sắp xếp giảm dần:", M)

#Câu 9

def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

le = [x for x in M if x % 2 != 0]
print("Các số lẻ:", le, "→ Tổng cộng có", len(le), "số lẻ")

chan = [x for x in M if x % 2 == 0]
print("Các số chẵn:", chan, "→ Tổng cộng có", len(chan), "số chẵn")

nguyento = [x for x in M if la_nguyen_to(x)]
print("Các số nguyên tố:", nguyento)

khong_nguyento = [x for x in M if not la_nguyen_to(x)]
print("Các số không phải nguyên tố:", khong_nguyento)


#Câu 10

def nhap_ma_tran(ten):
    n = int(input(f"Nhập số hàng của ma trận {ten}: "))
    m = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử của ma trận {ten}:")
    mat = []
    for i in range(n):
        hang = list(map(float, input(f"Hàng {i+1}: ").split()))
        mat.append(hang)
    return mat

def cong_ma_tran(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def chuyen_vi(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


print("Nhập ma trận A:")
A = nhap_ma_tran("A")

print("Nhập ma trận B:")
B = nhap_ma_tran("B")

if len(A) == len(B) and len(A[0]) == len(B[0]):
    C = cong_ma_tran(A, B)
    print("Tổng ma trận A + B là:")
    for hang in C:
        print(hang)
else:
    print("Hai ma trận không cùng kích thước, không thể cộng!")

print("Ma trận chuyển vị của A:")
for hang in chuyen_vi(A):
    print(hang)

print("Ma trận chuyển vị của B:")
for hang in chuyen_vi(B):
    print(hang)
