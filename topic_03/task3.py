class DictWorker:
    def __init__(self):
        self.d = {"name": "Ivan", "group": "KB-241"}
        print("Початковий словник:", self.d)

    def check_methods(self):
        print("Keys:", list(self.d.keys()))

        print("Values:", list(self.d.values()))

        print("Items:", list(self.d.items()))

        self.d.update({"age": 19, "city": "Kyiv"})
        print("Update (додали вік і місто):", self.d)

        if "group" in self.d:
            del self.d["group"]
            print("Del 'group' (видалили групу):", self.d)

        self.d.clear()
        print("Clear (очистили):", self.d)

if __name__ == "__main__":
    worker = DictWorker()
    worker.check_methods()