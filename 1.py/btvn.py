#bai1btvn
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

#btvn2# a. Tổng tam giác trên (chéo phụ)
def tong_cheo_phu_tren(a):
    n = len(a)
    tong = 0
    for i in range(n):
        for j in range(n):
            if i + j <= n - 1:
                tong += a[i][j]
    return tong

# b. Đổi số âm -> trị tuyệt đối
def doi_am(a):
    return [[abs(x) for x in row] for row in a]

# c. Thay số chẵn = x
def thay_chan(a, x):
    return [[x if val % 2 == 0 else val for val in row] for row in a]

# d. Kiểm tra toàn chẵn
def toan_chan(a):
    return all(val % 2 == 0 for row in a for val in row)

# e. Kiểm tra đối xứng
def doi_xung(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False
    return True

#btvn3

data = {
    "lop1": {"ten": "An", "diem": 8},
    "lop2": {"ten": "Binh", "diem": 7},
    "lop3": {"ten": "Chi", "diem": 9}
}

#btvn4
with open("data.txt", "w") as f:
    f.write("Hello Python")
with open("data.txt", "r") as f:
    print(f.read())

