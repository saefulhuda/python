import time

start = time.time()
data = [56, 8, 88, 1, 4, 3, 17, 20, 3, 87]

# Bubble Sort
    # Bandingkan nilai data ke-1 dan data ke-2
    # Jika data ke-1 lebih besar dari data ke-2 maka tukar posisinya
    # Kemudian data yg lebih besar tadi dibandingkan dengan data ke-3
    # Lakukan langkah nomer 2 hingga selesai.
def bubble_sort(alist):
	print('Bubble Sort Start at:', start)
	print('Keadaan awal:', alist)
	lenlist = len(alist)
	for i in range(0, lenlist - 1):
		print('Langkah ke-%d: ' % (i+1), end = '')
		for j in range(lenlist - 1, i, -1):
			if alist[j] < alist[j-1]:
				temp 		= alist[j]
				alist[j] 	= alist[j-1]
				alist[j-1] 	= temp
		print(alist)
	# print(alist)

# Insertion Sort
    # Bandingkan data ke-2 dengan data ke-1, jika data ke-2 lebih kecil maka tukar posisinya, jika tidak biarkan aja.
    # Data ke-3 dibandingkan dengan data ke-1 dan ke-2, jika data ke-3 lebih kecil kemudian tukar lagi posisinya.
    # Data ke-4 dibandingkan dengan data ke-3, ke-2, dan ke-1, jika data ke-4 lebih kecil dari ketiganya maka letakkan data ke-4 ke posisi paling depan. Begitu seterusnya sampai tidak ada lagi data yang bisa dipindahkan.
def insertion_sort(alist):
	print('Insertion Sort Start at:', start)
	print('Keadaan awal:', alist)
	lenlist = len(alist)
	for i in range(1, lenlist):
		currentvalue = alist[i]
		print('Meyisipkan nilai %d: \t' % currentvalue, end = '')
		position = i
		while position > 0 and alist[position - 1] > currentvalue:
			alist[position] = alist[position - 1]
			position -= 1
		alist[position] = currentvalue
		print(alist)


# Insertion Sort
    # Cari data terkecil dalam interval  j= 0 sampai dengan j= N-1
    # Jika pada posisi  pos ditemukan data yang terkecil, tukarkan data diposisi  pos dengan data di posisi  i jika k.
    # Ulangi langkah 1 dan 2 dengan j= j+isampai dengan j= N-1, dan seterusnya sampai  j = N
def selection_sort(alist):
	print('Selection Sort Start at:', start)
	print('Keadaan awal:', alist)
	# Traverse through all array elements 
	for i in range(len(alist)): 
	# Find the minimum element in remaining 
	# unsorted array 
		min_idx = i 
		for j in range(i+1, len(alist)): 
			if alist[min_idx] > alist[j]:
				min_idx = j

		# Swap the found minimum element with 
		# the first element		 
		alist[i], alist[min_idx] = alist[min_idx], alist[i]

# Quick Sort
    # Ambil sebuah elemen, yang disebut dengan pivot, pada sebuah daftar.
    # Urutkan kembali sebuah list sehingga elemen dengan nilai yang kecil dari pivot berada sebelum pivot, sedangkan seluruh element yang memiliki nilai yang lebih besar dari pivot berada setelahnya (nilai yang sama dapat berada pada pivot setelahnya). Setelah pemisahan, pivot berada pada posisi akhirnya. Operasi ini disebut Partition.
    # Sub list kemudian disortir secara recursif dari elemen yang lebih kecil dan sub list dari elemen yang lebih besar.
# Python program for implementation of quick_sort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 


def partition(arr, low, high): 
	i = (low-1)		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low, high): 

		# If current element is smaller than or 
		# equal to pivot 
		if arr[j] <= pivot: 

			# increment index of smaller element 
			i = i+1
			arr[i], arr[j] = arr[j], arr[i] 

	arr[i+1], arr[high] = arr[high], arr[i+1] 
	return (i+1) 

# The main function that implements quick_sort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 


def quick_sort(arr, low, high): 
	if len(arr) == 1: 
		return arr 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr, low, high) 

		# Separately sort elements before 
		# partition and after partition 
		quick_sort(arr, low, pi-1) 
		quick_sort(arr, pi+1, high) 


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quick_sort(arr, 0, n-1) 
print("Sorted array is:") 
for i in range(n): 
	print("%d" % arr[i]), 

# This code is contributed by Mohit Kumra 
#This code in improved by https://github.com/anushkrishnav 



# Start bubble sort process
# bubble_sort(data)
# Start insertion sort process
# insertion_sort(data)
# Start selection sort process
# selection_sort(data)
# Start quick sort process
lenlist = len(data)
# quick_sort(data, 0, lenlist - 1)

print('Hasil akhir:', data)
print('Jumlah data:', len(data))
end = time.time()
print('End at:', end)
print('Waktu eksekusi:', (end - start))