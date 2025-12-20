class ListWorker:
    def __init__(self):
        self.lst = [5, 1, 9]
        print("Старт:", self.lst)

    def check_methods(self):
        self.lst.append(10)
        print("Append 10:", self.lst)

        self.lst.extend([2, 3])
        print("Extend [2, 3]:", self.lst)

        self.lst.insert(0, 77)
        print("Insert 77 (на 0):", self.lst)

        if 1 in self.lst:
            self.lst.remove(1)
            print("Remove 1:", self.lst)

        self.lst.reverse()
        print("Reverse:", self.lst)

        self.lst.sort()
        print("Sort:", self.lst)

        copy_lst = self.lst.copy()
        print("Copy:", copy_lst)

        self.lst.clear()
        print("Clear:", self.lst)

if __name__ == "__main__":
    w = ListWorker()
    w.check_methods()