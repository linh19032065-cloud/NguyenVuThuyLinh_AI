
#bai1
a=float (input("nhap a:"))
b=float (input("nhap b:"))
c = float(input("nhap c: "))
d = float(input("nhap d: "))
tong=a+b
hieu=a-b
tich=a*b
thuong=a/b
print("tong la:",tong)
print("hieu la:",hieu)
print("tich la:",tich)
print("thuong la:",thuong)

#bai2
x="hello world"
print(x[2:5])

#bai3
x=" hello world "
x=x.strip()
print(x.upper())
print(x.lower())
x=x.replace("H","J")

#bai4
if(a>b): print("hello world")

#bai5
if a==b:
  print("yes")
else:
  print("no")

#bai6
if a==b:
  print(1)
elif a>b:
  print(2)
else:
  print(3)

#bai7
if a == b and b == d:
    print("Hello World!")

#bai8
if a == b or c == d:
    print("Hello World!")

#bai9
print("Yes") if a > b else print("No")

#bai10
a=float(input("nhap a:"))
b=float(input("nhap b:"))
print("A") if a > b else print("=") if a == b else print("B")

#bai11
n = int(input("Nhap n: "))
a = []

for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)

b = [x for x in a if x % 2 == 0]

print("Mang a:", a)
print("Mang b (chan):", b)

#bai12
tong = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
print("Tổng:", tong)

#bài13
a=[3, 9, 1, 4]
b=[2, 7, 4, 3, 2, 8]
c=[]
min_len=min(len(a),len(b))
for i in range(min_len):
  c.append(a[i]+b[i])
if len(a)>len(b):
  c.extend(a[min_len:])
else:
  c.extend(b[min_len:])
print(c)

#bai14a
def tao_mang(m, n):
    return [[random.randint(1, 50) for _ in range(n)] for _ in range(m)]

def xuat_dong(a, m):
  print("dong", m, ":",a[m])

def dong_max_duoi_45(a):
    max_sum = -1
    index = -1
    for i in range(len(a)):
        s = sum(a[i])
        if s < 45 and s > max_sum:
            max_sum = s
            index = i
    return index, max_sum

def dong_max_tren_45(a):
    max_sum = -1
    index = -1
    for i, row in enumerate(a):
        s = sum(row)
        if s > 45 and s > max_sum:
            max_sum = s
            index = i
    return index, max_sum

def cot_tich_nho_nhat(a):
    m, n = len(a), len(a[0])
    min_prod = float('inf')
    index = -1
    for j in range(n):
        prod = 1
        for i in range(m):
            prod *= a[i][j]
        if prod < min_prod:
            min_prod = prod
            index = j
    return index, min_prod

def xuat_chan_le(a):
    print("Phần tử dòng chẵn, cột lẻ:")
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i % 2 == 0 and j % 2 == 1:
                print(a[i][j], end=" ")
        print()

def tbc_chan_dong_le(a):
    tong = dem = 0
    for i in range(len(a)):
        if i % 2 == 1:
            for x in a[i]:
                if x % 2 == 0:
                    tong += x
                    dem += 1
    return tong / dem if dem != 0 else 0

def tbc_bien(a):
    m, n = len(a), len(a[0])
    tong = dem = 0
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                tong += a[i][j]
                dem += 1
    return tong / dem

def tbc_tich_trong(a):
    m, n = len(a), len(a[0])
    tong = dem = 0
    for i in range(1, m-1):
        for j in range(1, n-1):
            tong += a[i][j]
            dem += 1
    return tong / dem if dem != 0 else 0

#bai15
import random
class SinhVien:
    def __init__(self, ma, ten, namsinh, diem):
        self.ma = ma
        self.ten = ten
        self.namsinh = namsinh
        self.diem = diem

    # c. Đủ điều kiện lên lớp
    def dem_len_lop(ds):
        return sum(1 for sv in ds if sv.diem >= 5)

    # d. SV đủ 20 tuổi
    def sv_20_tuoi(ds, nam_hien_tai):
        return [sv for sv in ds if nam_hien_tai - sv.namsinh >= 20]

    # e. Đếm hệ DH
    def dem_he_dh(ds):
        return sum(1 for sv in ds if sv.ma[2:4] == "DH")

    # f. Tên "Lan"
    def dem_ten_lan(ds):
        return sum(1 for sv in ds if "Lan" in sv.ten)

    # g. Họ "Phan"
    def dem_ho_phan(ds):
        return sum(1 for sv in ds if sv.ten.startswith("Phan"))


# Test
ds = [
    SinhVien("02DH0001", "Phan Lan", 2003, 6.5),
    SinhVien("01CD0002", "Nguyen Lan", 2005, 4.0),
    SinhVien("02DH0003", "Phan An", 2002, 7.0)
]

print("Đủ lên lớp:", SinhVien.dem_len_lop(ds))
print("Hệ DH:", SinhVien.dem_he_dh(ds))
print("Tên Lan:", SinhVien.dem_ten_lan(ds))
print("Họ Phan:", SinhVien.dem_ho_phan(ds))
nam_hien_tai = 2024
sv_20 = SinhVien.sv_20_tuoi(ds, nam_hien_tai)
print("SV đủ 20 tuổi:", [sv.ten for sv in sv_20])
