class tree:

    def __init__(self, data, parent = None):
        self.node =  data
        self.left = None
        self.right = None
        self.counter = 1
        self.parent = parent

    def add(self, obj):
        if obj > self.node:
            if not self.right:
                self.right = tree(obj, self.node)
                self.counter += 1
            else:
                self.right.add(obj)
                self.counter += 1
        elif obj < self.node:
            if not self.left:
                self.left = tree(obj, self.node)
                self.counter += 1
            else:
                self.left.add(obj)
                self.counter += 1

    def delete(self, value):
        if value == self.node:
            if self.left != None:
                self.node = self.left.highest()
                self.left.delete(self.node)
                self.counter -= 1
            elif self.right != None:
                self.value = self.right.lowest()
                self.right.delete(self.node)
                self.counter -= 1
            else:
                return None
        else:
            if value < self.node and self.left != None:
                self.left = self.left.delete(value)
                self.counter -= 1
            if value > self.node and self.right != None:
                self.right = self.right.delete(value)
                self.counter -= 1
            return self

    def highest(self):
        if self.right != None:
            return self.right.highest()
        else:
            return self.node
    
    def lowest(self):
        if self.left != None:
            return self.left.lowest()
        else:
            return self.node

    def search(self, value):
        if value == self.node:
            return self
        elif value < self.node:
            if self.left == None:
                return False
            else:
                return self.left.search(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.search(value)

    def data_print(self):
        d = []
        if self.left:
            d.extend(self.left.data_print())
        d.append(self.node)
        if self.right:
            d.extend(self.right.data_print())
        return d

    

        
