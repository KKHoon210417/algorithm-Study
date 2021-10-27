class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        self.items[hash(key) % len(self.items)] = value
        return

    def get(self, key):
        result = self.items[hash(key) % len(self.items)]
        return result


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))