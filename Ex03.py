def is_max_heap(arr):
    n = len(arr)
    # ตรวจสอบสำหรับทุก node ที่มีลูก
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        # ถ้ามีลูกด้านซ้าย ให้ตรวจสอบเงื่อนไข
        if left < n and arr[i] < arr[left]:
            return False
        # ถ้ามีลูกด้านขวา ให้ตรวจสอบเงื่อนไข
        if right < n and arr[i] < arr[right]:
            return False
    return True

if __name__ == '__main__':
    arr = [8, 4, 7, 3, 2, 5, 6, 1]

print("arr1 เป็น Max Heap หรือไม่?", is_max_heap(arr))  

