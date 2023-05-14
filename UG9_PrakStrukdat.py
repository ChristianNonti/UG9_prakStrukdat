class Node:
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority
        self._next = None


class PriorityQueueUnsorted:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def add(self, data, priority):
        new_node = Node(data, priority)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node
        self._size += 1

    def remove(self):
        if not self.is_empty():
            if self._size == 1:
                removed_node = self._head
                self._head = None
                self._tail = None
            else:
                min_priority = self.peek()[1]  # Get the highest priority
                prev = None
                current = self._head
                while current is not None:
                    if current._priority == min_priority:
                        if current == self._head:
                            self._head = current._next
                        elif current == self._tail:
                            self._tail = prev
                            prev._next = None
                        else:
                            prev._next = current._next
                        removed_node = current
                        current = current._next
                        del removed_node
                        self._size -= 1
                    else:
                        prev = current
                        current = current._next

    def peek(self):
        if not self.is_empty():
            highest_priority = self._head._priority
            highest_data = self._head._data
            current = self._head._next
            while current is not None:
                if current._priority < highest_priority:
                    highest_priority = current._priority
                    highest_data = current._data
                current = current._next
            return (highest_data, highest_priority)
        else:
            return None

    def print_all(self):
        if not self.is_empty():
            current = self._head
            while current is not None:
                print(current._data, current._priority)
                current = current._next
        else:
            print("Queue is empty")

    def ubahBersama(self, prio, namaBaru):
        if not self.is_empty():
            current = self._head
            while current is not None:
                if current._priority == prio:
                    current._data = namaBaru
                current = current._next

    def removePrioSekaligus(self):
        if not self.is_empty():
            highest_priority = self.peek()[1]
            while self.peek()[1] == highest_priority:
                self.remove()

    def fungsiTambahan(self):
        pass


# Contoh penggunaan
myQueue = PriorityQueueUnsorted()
myQueue.add("Dedi", 4)
myQueue.add("Sindu", 2)
myQueue.add("Haniif", 5)
myQueue.add("Farel", 2)
myQueue.add("Beatrix", 3)
myQueue.add("Shalom", 3)
myQueue.add("Harris", 2)
myQueue.print_all()

myQueue.ubahBersama(2, "Mahasiswa A")
myQueue.print_all()

myQueue.removePrioSekaligus()
myQueue.print_all()

