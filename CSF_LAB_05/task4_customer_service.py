class CustomerService:
    def __init__(self):
        self.queue = []
 
    def add(self, name):
        self.queue.append(name)
 
    def serve(self):
        return self.queue.pop(0) if self.queue else None
 
    def display(self):
        print(f"Waiting: {self.queue}")
 
# Test
cs = CustomerService()
for customer in ["Ugyen", "Sangay", "Kezang"]:
    cs.add(customer)
 
cs.display()
print(f"Serving: {cs.serve()}")
cs.display()
print(f"Serving: {cs.serve()}")
cs.display()