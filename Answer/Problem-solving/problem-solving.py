import threading
import time

people = [
   {"first_name": "John", "last_name": "Black", "age": 30},
   {"first_name": "Michael", "last_name": "Johnsson", "age": 13},
   {"first_name": "Mery", "last_name": "Hunter", "age": 60},
   {"first_name": "Chris", "last_name": "Williams", "age": 45},
]

class Person:
   people_count = 0
   
   def __init__(self, first_name, last_name, age): 
       self.first_name = first_name
       self.last_name = last_name
       self.age == age  # ERROR: Using comparison operator (==) instead of assignment operator (=)
       self.id = self.increase_count()

   # This method should not be modified.
   def introduce(self):
       time.sleep(1)
       print(f"Hello, my first name is {self.first_name} and I am {self.age} years old.")

   def increase_count():  # ERROR: Missing 'self' or 'cls' parameter, should be a class method
       Person.people_count += 1
       return Person.people_count

def main():
   threads = []
   for p in people:
       x = Person(p["first_name"], p["age"], p["last_name"])  # ERROR: Incorrect parameter order - should be first_name, last_name, age
       threads.append(threading.Thread(target=x.introduce))
       
   for thread in threads:
       thread.start()
   
   print(f"Number of people created: {Person.people_count}")  # ERROR: Printing count before threads complete
   return

if __name__ == "main":  # ERROR: Incorrect format - should be "__main__" (with double underscores)
   main()