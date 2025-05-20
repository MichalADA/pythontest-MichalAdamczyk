---

### 1. What is `__main__.py` used for?

__main__.py is used as the entry point for a Python package when it is executed as a script using `python -m package_name`.  
It contains the main logic of the application and is executed by the interpreter when the package is run.


---

### 2. How to prevent Python module code from executing when the module is imported?

You can use:

```python
if __name__ == "__main__":
    # your code here
```

Code inside this block will only run when the file is executed directly, not when imported as a module.

---

### 3. What's the name of the method that represents a class constructor in Python?

The constructor method in Python is called `__init__()`.  
It is automatically invoked when a new object of a class is created.

---

### 4. What options do you have when you need to insert the value of a variable into a string? Name at least three.

Here are three common ways to insert variables into strings:

- **f-strings (Python 3.6+)**:  
  `f"Hello, {name}"`

- **String concatenation**:  
  `"Hello, " + name`

- **%-formatting**:  
  `"Hello, %s" % name`

Other options include `.format()` and `Template` from the `string` module.

---

### 5. How can you truly restrict access to a private method of a class in Python?

Python does not have strict private access modifiers like in other languages.  
However, there are conventions and techniques:

- `_method()` – by convention, intended to be private.
- `__method()` – triggers name mangling (makes it harder to access).
- For stricter access control, you can use:
  - `@property` decorators with custom getters/setters,
  - descriptor protocols,
  - or wrapper classes that expose only specific interfaces.

---


### 6. What Python feature would you use to add functionality to an existing function without modifying its code?

You can use **decorators** to add functionality to an existing function without changing its internal code.  
For example:

```python
@my_decorator
def my_function():
    ...
```

---

### 7. How is @staticmethod different from @classmethod?

The main difference is that a @staticmethod does not take any implicit first argument — it behaves like a regular function that just happens to live inside a class. It cannot access instance (self) or class (cls) data.

On the other hand, a @classmethod receives the class (cls) as its first argument, which allows it to access or modify class-level attributes. It's often used for creating alternative constructors or logic that applies to the class as a whole.

In short:

@staticmethod = no access to class or instance

@classmethod = has access to the class, but not the instance

---


### 8. What is the advantage of using `with` when reading/writing a file in Python?

The `with` statement ensures proper resource management by automatically closing the file, even if an error occurs.  
It uses the **context manager protocol** to handle setup and cleanup cleanly.

Example:

```python
with open("file.txt") as f:
    data = f.read()
```

---