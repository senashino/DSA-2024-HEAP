# ใบงานการทดลอง: โครงสร้างข้อมูล Heap

## วัตถุประสงค์การเรียนรู้
1. อธิบายหลักการทำงานของโครงสร้างข้อมูลแบบ Heap ได้
2. เขียนโปรแกรมเพื่อสร้างและจัดการ Heap ได้
3. ประยุกต์ใช้ Heap ในการแก้ปัญหาได้

## ทฤษฎีที่เกี่ยวข้อง
Heap เป็นโครงสร้างข้อมูลแบบต้นไม้แบบทวิภาค (Binary Tree) ที่มีคุณสมบัติพิเศษดังนี้:
- เป็นต้นไม้ที่สมบูรณ์ (Complete Binary Tree)
- ทุกโหนดพ่อแม่ต้องมีค่ามากกว่าหรือเท่ากับโหนดลูกทั้งสอง (กรณี Max Heap)
- หรือทุกโหนดพ่อแม่ต้องมีค่าน้อยกว่าหรือเท่ากับโหนดลูกทั้งสอง (กรณี Min Heap)

## ตัวอย่างการเขียนโปรแกรม

### การสร้าง Max Heap
```python
class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) // 2
        
    def left_child(self, i):
        return 2 * i + 1
        
    def right_child(self, i):
        return 2 * i + 2
        
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
        
    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
```

### การลบค่าสูงสุด
```python
def extract_max(self):
    if len(self.heap) == 0:
        return None
    
    max_val = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.heap.pop()
    
    if len(self.heap) > 0:
        self._sift_down(0)
    
    return max_val

def _sift_down(self, i):
    max_index = i
    left = self.left_child(i)
    right = self.right_child(i)
    
    if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
        max_index = left
    
    if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
        max_index = right
        
    if i != max_index:
        self.swap(i, max_index)
        self._sift_down(max_index)
```

## แบบฝึกหัด

### แบบฝึกหัดที่ 1: การแทรกค่า
จงเขียนโปรแกรมเพื่อแทรกค่าต่อไปนี้ลงใน Max Heap ที่ว่างเปล่า: 5, 3, 8, 1, 2, 7, 6, 4
พร้อมแสดงค่า Max Heap ที่ได้หลังจากเพิ่มข้อมูลครบแล้ว
```python
code python
```

[Capture รูปส่งตรงนี้]
![alt text](image.png)


### แบบฝึกหัดที่ 2: การลบค่า
จากข้อ 1 จงเขียนลำดับการลบค่าสูงสุดออกจาก Heap จำนวน 3 ครั้ง แสดงข้อมูล Heap หลังจากลบแต่ละครั้ง

```python
code python

```
[Capture รูปส่งตรงนี้]
![alt text](image-1.png)


### แบบฝึกหัดที่ 3: การเขียนโปรแกรม
จงเขียนฟังก์ชัน `is_max_heap(arr)` ที่รับ array เข้ามาและตรวจสอบว่าป็น Max Heap หรือไม่ 

```python
code python
```
[Capture รูปส่งตรงนี้]
![alt text](image-2.png)

## การประยุกต์ใช้งานจริง

### 1. ระบบจัดการคิวผู้ป่วยฉุกเฉิน (Emergency Room Triage)
```python
class Patient:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority  # ระดับความรุนแรง 1-5 (1 = ฉุกเฉินมาก)
    
    def __lt__(self, other):
        return self.priority < other.priority

class ERQueue:
    def __init__(self):
        self.queue = []  # Min Heap เพื่อให้ผู้ป่วยที่มี priority ต่ำ (อาการหนัก) ได้รับการรักษาก่อน
    
    def add_patient(self, patient):
        heapq.heappush(self.queue, patient)
    
    def treat_next_patient(self):
        if self.queue:
            return heapq.heappop(self.queue)
        return None

# ตัวอย่างการใช้งาน
er = ERQueue()
er.add_patient(Patient("คนไข้ A", 1))  # หัวใจวาย
er.add_patient(Patient("คนไข้ B", 3))  # ปวดท้อง
er.add_patient(Patient("คนไข้ C", 2))  # กระดูกหัก
```

[Capture รูปผลการทดลองส่งตรงนี้]

### 2. ระบบแนะนำสินค้าขายดี (Top K Items)
```python
class ProductRanking:
    def __init__(self, k):
        self.k = k
        self.products = []  # Min Heap เก็บ k สินค้าขายดีที่สุด
    
    def update_sales(self, product_id, sales):
        if len(self.products) < self.k:
            heapq.heappush(self.products, (sales, product_id))
        else:
            if sales > self.products[0][0]:
                heapq.heapreplace(self.products, (sales, product_id))
    
    def get_top_k(self):
        return sorted(self.products, reverse=True)

# ตัวอย่างการใช้งาน
ranking = ProductRanking(3)  # เก็บ 3 อันดับสินค้าขายดี
ranking.update_sales("สินค้า A", 100)
ranking.update_sales("สินค้า B", 150)
ranking.update_sales("สินค้า C", 80)
ranking.update_sales("สินค้า D", 200)
```
[Capture รูปผลการทดลองส่งตรงนี้]

### 3. ตัวอย่างระบบคิวธนาคาร แบบมีระดับความสำคัญ โดยใช้ heapq
```python 
import heapq
from datetime import datetime
import time

class BankCustomer:
    def __init__(self, name, service_type, is_premium=False):
        self.name = name
        self.service_type = service_type
        self.is_premium = is_premium
        self.arrival_time = datetime.now()
        
        # กำหนดลำดับความสำคัญตาม service_type และสถานะลูกค้า
        self.priority = self._calculate_priority()
        
    def _calculate_priority(self):
        # ลำดับความสำคัญ (ยิ่งน้อยยิ่งสำคัญ)
        priority = {
            'ฝาก-ถอน': 3,
            'ชำระค่าบริการ': 2,
            'เปิดบัญชี': 1,
            'สินเชื่อ': 0
        }
        
        # ลูกค้า Premium จะได้ priority สูงกว่าปกติ 1 ระดับ
        base_priority = priority.get(self.service_type, 4)
        if self.is_premium:
            base_priority -= 0.5
            
        return base_priority
        
    def __lt__(self, other):
        # เปรียบเทียบลำดับความสำคัญ
        if self.priority == other.priority:
            # ถ้าความสำคัญเท่ากัน ใช้เวลามาก่อน-หลัง
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority
        
class BankQueue:
    def __init__(self):
        self.queue = []  # heap queue
        self.waiting_count = 0
        
    def add_customer(self, customer):
        heapq.heappush(self.queue, customer)
        self.waiting_count += 1
        print(f"ลูกค้า: {customer.name}")
        print(f"บริการ: {customer.service_type}")
        print(f"สถานะ: {'Premium' if customer.is_premium else 'ทั่วไป'}")
        print(f"จำนวนคิวรอ: {self.waiting_count}")
        print("-" * 30)
        
    def serve_next_customer(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return None
            
        customer = heapq.heappop(self.queue)
        self.waiting_count -= 1
        
        wait_time = datetime.now() - customer.arrival_time
        print(f"\nเรียกลูกค้า: {customer.name}")
        print(f"บริการ: {customer.service_type}")
        print(f"เวลารอ: {wait_time.seconds} วินาที")
        print(f"จำนวนคิวรอ: {self.waiting_count}")
        print("-" * 30)
        
        return customer
        
    def display_queue(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return
            
        print("\nรายการคิวที่รอ:")
        # สร้าง copy ของคิวเพื่อไม่ให้กระทบคิวจริง
        temp_queue = self.queue.copy()
        position = 1
        
        while temp_queue:
            customer = heapq.heappop(temp_queue)
            print(f"{position}. {customer.name} - {customer.service_type}")
            position += 1
        print("-" * 30)

# ตัวอย่างการใช้งาน
def demo_bank_queue():
    bank = BankQueue()
    
    # เพิ่มลูกค้าเข้าคิว
    customers = [
        BankCustomer("คุณแดง", "ฝาก-ถอน"),
        BankCustomer("คุณขาว", "สินเชื่อ", is_premium=True),
        BankCustomer("คุณเขียว", "ชำระค่าบริการ"),
        BankCustomer("คุณม่วง", "เปิดบัญชี"),
        BankCustomer("คุณฟ้า", "สินเชื่อ")
    ]
    
    for customer in customers:
        bank.add_customer(customer)
        time.sleep(1)  # จำลองการมาถึงต่างเวลากัน
        
    print("\nแสดงลำดับคิว:")
    bank.display_queue()
    
    # จำลองการเรียกลูกค้าเข้ารับบริการ
    print("\nเริ่มเรียกลูกค้า:")
    for _ in range(len(customers)):
        bank.serve_next_customer()
        time.sleep(1)

if __name__ == "__main__":
    demo_bank_queue()
```
### ทำการปรับปรุงโปรแกรม โดยให้ทำการกดเลือกธุรกรรม แล้วจะมีเลขคิวในแต่ละช่วงของการทำธุรกรรม แทนชื่อของลูกค้า และมีการเรียกคิวตามระดับความสำคัญและเวลาที่มาก่อนหลังของลูกค้า

```python
code python
```
[Capture รูปส่งตรงนี้]
![alt text](image-3.png)