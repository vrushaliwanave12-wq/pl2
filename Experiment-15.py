class Stack:
  def __init__(self):
    self.stack = []
  def push(self, item):
    self.stack.append(item)
    print(f"Pushed {item} onto the stack.")

  def safe_pop(self):
    if not self.stack:
      print("Stack is empty, nothing to pop.")
      return None
    return self.stack.pop()
  
  def display(self):
    print("Current stack:", self.stack)

if __name__ == "__main__":
  my_stack = Stack()
  my_stack.safe_pop() 
  my_stack.push(10)
  my_stack.push(20)
  my_stack.display()
  print("Popped item:", my_stack.safe_pop())
  my_stack.display(