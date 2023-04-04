#day-6 DS
#sorting
'''
def selectionSort(array, size):

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array [min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx],array[step])

data = [20, 12, 10, 15, 2]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending order:')
print(data)
'''
#question-1
'''
class FruitInfo:
    fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.fruit_name_list:
            return FruitInfo.fruit_price_list[FruitInfo.fruit_name_list.index(fruit_name)]
        else:
            return -1


class Purchase:
    counter = 101

    def __init__(self, customer, fruit_name, quantity, is_wholesale):
        self.__purchase_id = "P" + str(Purchase.counter)
        Purchase.counter += 1
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
        self.__is_wholesale = is_wholesale

    def calculate_price(self):
        price = FruitInfo.get_fruit_price(self.__fruit_name)
        if price == -1:
            return -1
        else:
            total_price = price * self.__quantity
            max_price_fruit = max(FruitInfo.fruit_price_list)
            min_price_fruit = min(FruitInfo.fruit_price_list)
            if price == max_price_fruit and self.__quantity > 1:
                total_price *= 0.98
            elif price == min_price_fruit and self.__quantity >= 5:
                total_price *= 0.95
            if self.__is_wholesale:
                total_price *= 0.9
            return total_price

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_fruit_name(self):
        return self.__fruit_name

    def get_quantity(self):
        return self.__quantity

    def get_is_wholesale(self):
        return self.__is_wholesale


class Customer:
    def __init__(self, customer_name, phone_number):
        self.__customer_name = customer_name
        self.__phone_number = phone_number

    def get_customer_name(self):
        return self.__customer_name

    def get_phone_number(self):
        return self.__phone_number
customer = Customer("John", "9876543210")
purchase = Purchase(customer, "Grape", 6, True)
final_price = purchase.calculate_price()
print("Purchase ID:", purchase.get_purchase_id())
print("Customer Name:", purchase.get_customer().get_customer_name())
print("Customer Phone Number:", purchase.get_customer().get_phone_number())
print("Fruit Name:", purchase.get_fruit_name())
print("Quantity:", purchase.get_quantity())
print("Is Wholesale:", purchase.get_is_wholesale())
prclass FruitInfo:
    fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.fruit_name_list:
            return FruitInfo.fruit_price_list[FruitInfo.fruit_name_list.index(fruit_name)]
        else:
            return -1


class Purchase:
    counter = 101

    def _init_(self, customer, fruit_name, quantity, is_wholesale):
        self.__purchase_id = "P" + str(Purchase.counter)
        Purchase.counter += 1
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
        self.__is_wholesale = is_wholesale

    def calculate_price(self):
        price = FruitInfo.get_fruit_price(self.__fruit_name)
        if price == -1:
            return -1
        else:
            total_price = price * self.__quantity
            max_price_fruit = max(FruitInfo.fruit_price_list)
            min_price_fruit = min(FruitInfo.fruit_price_list)
            if price == max_price_fruit and self.__quantity > 1:
                total_price *= 0.98
            elif price == min_price_fruit and self.__quantity >= 5:
                total_price *= 0.95
            if self.__is_wholesale:
                total_price *= 0.9
            return total_price

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_fruit_name(self):
        return self.__fruit_name

    def get_quantity(self):
        return self.__quantity

    def get_is_wholesale(self):
        return self.__is_wholesale


class Customer:
    def _init_(self, customer_name, phone_number):
        self.__customer_name = customer_name
        self.__phone_number = phone_number

    def get_customer_name(self):
        return self.__customer_name

    def get_phone_number(self):
        return self.__phone_number
customer = Customer("John", "9876543210")
purchase = Purchase(customer, "Grape", 6, True)
final_price = purchase.calculate_price()
print("Purchase ID:", purchase.get_purchase_id())
print("Customer Name:", purchase.get_customer().get_customer_name())
print("Customer Phone Number:", purchase.get_customer().get_phone_number())
print("Fruit Name:", purchase.get_fruit_name())
print("Quantity:", purchase.get_quantity())
print("Is Wholesale:", purchase.get_is_wholesale())
print("Final Price:", final_price)int("Final Price:", final_price)
'''
#question
'''
class BakeHouse:
    def __init__(self):
        self.occupied_table_list = []

    def get_occupied_table_list(self):
        return self.occupied_table_list

    def allocate_table(self):
        if not self.occupied_table_list: 
            self.occupied_table_list.append(1) 
        else:
            for i in range(len(self.occupied_table_list)):
                if i == len(self.occupied_table_list) - 1: 
                    self.occupied_table_list.append(self.occupied_table_list[i] + 1) 
                elif self.occupied_table_list[i+1] != self.occupied_table_list[i] + 1: 
                    self.occupied_table_list.insert(i+1, self.occupied_table_list[i] + 1) 
                    break

    def deallocate_table(self, table_number):
        if table_number in self.occupied_table_list:
            self.occupied_table_list.remove(table_number)
class Node:
    def init(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.print_list() 
my_list.reverse()
my_list.print_list()
'''
#question
'''
class ChildrenCamp:
    def __init__(self, child_id, chocolates_received):
        self.child_id = child_id
        self.chocolates_received = chocolates_received

    def calculate_total_chocolates(self):
        return sum(self.chocolates_received)

    def reward_child(self, child_id_rewarded, extra_chocolates):
        if extra_chocolates < 1:
            return "Extra chocolates is less than 1"
        if child_id_rewarded not in self.child_id:
            return "Child id is invalid"
        index = self.child_id.index(child_id_rewarded)
        self.chocolates_received[index] += extra_chocolates
        return self.chocolates_received

child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

camp = ChildrenCamp(child_id, chocolates_received)
print(camp.calculate_total_chocolates()) 

print(camp.reward_child(30, 2)) 
print(camp.calculate_total_chocolates()) 

print(camp.reward_child(60, 2)) 

print(camp.reward_child(40, 0))
'''
#question
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] <=pivot:
            i = i+1
            (array[i], array[j]) = (array[j], array[i])
        (array[i+1],array[high]) = (array[high], array[i+1])
        return i+1
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
data = [8, 7, 6, 1, 0, 9, 2]
print("Unsorted array")
print(data)
size=len(data)
quickSort(data, 0, size - 1)
print("Sorted array in ascending order:")
print(data)
        
































