#🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨#
# Nama  : Muhammad Irfan Zahran     #
# NIM   : L200210016                #
# Kelas : A                         #
#🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨#

# fungsi menampilkan kemunculan pertama suatu data pada array 
def muncul_pertama(data,x):
  for i in range(len(data)):
    if data[i]==x:
      return i
# membuat data
data= [1, 2, 3, 3, 4, 4, 4, 5]
data2= [1, 1, 2, 3, 5, 8]
# menjalankan fungsi
percobaan1= muncul_pertama(data,4)
percobaan2= muncul_pertama(data2,1)
# mencetak hasil
print("output 1 =>", percobaan1)
print("output 2 =>", percobaan2)


# kode program menampilkan index tertinggi pada mountain array
def mountain_array(arr):
    index_puncak = None
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            index_puncak = i
            break
    return index_puncak

print("=== Mountain Array ===")
# percobaan pertama
arr1= [0,2,4,2,0]
hasil1=mountain_array(arr1)
print("index puncak tertinggi : ", hasil1)
# percobaan ke 2
arr2= [0,5,10,20,10,2,0]
hasil2=mountain_array(arr2)
print("index puncak tertinggi : ", hasil2)




