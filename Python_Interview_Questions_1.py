{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "40276dc2-ff84-4f3a-9e3b-3f01d77f0f63",
   "metadata": {},
   "source": [
    "Q:1 What is Compiler ?   "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1cc5130-5224-4e1a-87b5-3ab4318431d1",
   "metadata": {},
   "source": [
    "ANS:A compiler converts human-readable code into computer-understandable code at once, before execution."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee7d8789-67b0-4859-94ff-82e2f674eb40",
   "metadata": {},
   "source": [
    "or:\n",
    "A compiler is a computer program that translates source code written in a high-level programming language into machine code, bytecode, or another programming language so that it can be executed by a computer.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27e418fa-3bb8-4300-820a-82966f5569e4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "67ac6ac3-c860-4e33-b6b4-fa892312bb7d",
   "metadata": {},
   "source": [
    "Q:2 What is Python? What are its key features?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d84c3dca-8837-403b-9f8a-265c4154d7d7",
   "metadata": {},
   "source": [
    "Python is a high-level, interpreted, general-purpose programming language. It was created by Guido van Rossum and released in 1991. Python is known for its simplicity, readability, and versatility, making it popular among beginners and professionals alike."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ceddde2f-e9fd-430f-bd91-669dd2bab7b4",
   "metadata": {},
   "source": [
    "✅ 1. Easy to Learn and Use\n",
    "Python has a simple and clean syntax, similar to English.\n",
    "\n",
    "\n",
    "✅ 2. Interpreted Language\n",
    "Python executes code line by line using an interpreter.\n",
    "\n",
    "No need to compile before running.\n",
    "\n",
    "✅ 3. High-Level Language\n",
    "You don't need to manage memory or hardware directly.\n",
    "It abstracts complex details like memory management, so you can focus on logic.\n",
    "\n",
    "Easy for beginners and professionals.\n",
    "\n",
    "✅ 4. Dynamically Typed\n",
    "No need to declare data types.\n",
    "\n",
    "\n",
    "✅ 5. Object-Oriented\n",
    "Supports classes and objects.\n",
    "\n",
    "\n",
    "✅ 6. Large Standard Library\n",
    "Comes with built-in modules for math, file handling, web, etc.\n",
    "\n",
    "✅ 7. Platform Independent\n",
    "Write code once, run it anywhere (Windows, Mac, Linux).\n",
    "\n",
    "✅ 8. Open Source\n",
    "Free to use and distribute. Huge community support.\n",
    "\n",
    "✅ 9. Extensive Libraries and Frameworks\n",
    "For web: Django, Flask\n",
    "\n",
    "For data: NumPy, Pandas\n",
    "\n",
    "For ML: TensorFlow, Scikit-learn\n",
    "\n",
    "✅ 10. Portable and Embeddable\n",
    "Python code can be integrated with other languages like C or C++."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4c8452b-2aae-4d2a-9bcf-cb734a5b4942",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "9e9c6978-3e8e-45d2-a50c-267513901926",
   "metadata": {},
   "source": [
    "Q:3 What are Python’s data types?\n",
    "\n",
    "int, float, str, bool, list, tuple, set, dict, etc.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dcbb15b4-44ae-454f-8d6c-9b23c5727648",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "51e839ed-29f4-49bd-bf61-346de209a94c",
   "metadata": {},
   "source": [
    "Q:4 What is the difference between list and tuple?\n",
    "\n",
    "\n",
    "🔹 List:\n",
    "List is mutable – you can add, remove, or change elements.\n",
    "\n",
    "Defined using square brackets [].\n",
    "\n",
    "Example: fruits = [\"apple\", \"banana\", \"mango\"]\n",
    "\n",
    "Lists have more built-in methods like append(), pop(), etc.\n",
    "\n",
    "Slower in performance compared to tuples.\n",
    "\n",
    "Preferred when the data needs to change.\n",
    "\n",
    "🔸 Tuple:\n",
    "Tuple is immutable – you cannot modify elements after creation.\n",
    "\n",
    "Defined using round brackets ().\n",
    "\n",
    "Example: colors = (\"red\", \"green\", \"blue\")\n",
    "\n",
    "Tuples have fewer methods.\n",
    "\n",
    "Faster and more memory-efficient.\n",
    "\n",
    "Preferred when the data should stay constant.\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\"\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fcb011d8-8c0b-44fc-8225-06cdda1aaed1",
   "metadata": {},
   "source": [
    "\n",
    "Answer:\n",
    "\n",
    "\"In Python, both lists and tuples are used to store collections of items. However, the main difference lies in their mutability. A list is mutable, meaning we can modify it after creation—such as adding, removing, or updating elements. Lists are defined using square brackets, for example: my_list = [1, 2, 3].\n",
    "\n",
    "On the other hand, a tuple is immutable, which means once it's created, its elements cannot be changed. Tuples are defined using parentheses, like my_tuple = (1, 2, 3).\n",
    "\n",
    "Due to immutability, tuples are generally faster and more memory-efficient, and they are preferred when we want to ensure that the data remains constant throughout the program."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "028d3544-6472-4eec-b292-7b8c16a964f8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "038de195-e432-4866-b288-3a797c241524",
   "metadata": {},
   "source": [
    "Q:5 How is Python an interpreted language?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "54799b3e-ace1-40b5-8c4e-948f64c32873",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid character '✅' (U+2705) (143989127.py, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[32], line 4\u001b[1;36m\u001b[0m\n\u001b[1;33m    ✅ Explanation:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid character '✅' (U+2705)\n"
     ]
    }
   ],
   "source": [
    "Python is called an interpreted language because its code is executed line by line by an interpreter rather than being \n",
    "compiled into machine code all at once (like in C or C++).\n",
    "\n",
    "✅ Explanation:\n",
    "When you run a Python program:\n",
    "\n",
    "Source Code (.py) → is fed to the Python interpreter\n",
    "\n",
    "Interpreter converts it into bytecode\n",
    "\n",
    "Bytecode is then executed by the Python Virtual Machine (PVM) line-by-line\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f951c2e0-5bc4-4095-ac50-c7b0076d4c2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your Python Code (.py)\n",
    "#         ↓\n",
    "#   Python Interpreter\n",
    "#         # ↓\n",
    "#      Bytecode (.pyc)\n",
    "#         ↓\n",
    "# Python Virtual Machine (PVM)\n",
    "#         ↓\n",
    "#   Output (line-by-line execution)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6683d4aa-5046-4730-aff7-ebbf7d8b78af",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "ac7ca863-4105-447f-8981-cfcd3ca2c924",
   "metadata": {},
   "source": [
    "Q:6 What are Python functions? How do you define them?\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d5028956-d53f-49cb-86cd-2c7bfbef1765",
   "metadata": {},
   "source": [
    "In Python, a function is a block of reusable code that performs a specific task. Functions help organize code, reduce repetition, and make programs easier to understand and maintain.\n",
    "\n",
    "🔧 Types of Functions in Python:\n",
    "\n",
    "Built-in Functions → Provided by Python (e.g., print(), len(), type())\n",
    "\n",
    "User-defined Functions → Created by the programmer using def keyword\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "cf546673-c088-4761-9fdb-8efcefd3947b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Built-in functions are pre-defined functions provided by Python — you can use them directly without writing any extra code or importing modules."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d4ae693-3d58-4e8b-abff-9748da12ce0e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "558de059-a28f-42bf-b5e6-2444b112a5a4",
   "metadata": {},
   "source": [
    "Q:7 What is the difference between is and ==?\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "544433db-4ae5-4a6e-8a6b-3ce77bc1e906",
   "metadata": {},
   "source": [
    " == (Double Equals) – Equality Operator\n",
    "\n",
    "\n",
    "== checks if the values of two variables are equal, regardless of whether they are stored at the same memory location"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "09d27080-a73d-4b92-9d99-84e0117805ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a = [1, 2, 3]\n",
    "b = [1, 2, 3]\n",
    "print(a == b)   # Output: True (values are same)\n",
    " # Even though a and b are different objects, their values are the same, so == returns True."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fcbf4caf-2bed-40ba-a2b6-8d34ebe73bf8",
   "metadata": {},
   "source": [
    " is – Identity Operator\n",
    "is checks whether two variables point to the same object in memory.\n",
    "\n",
    "It checks the identity, not just the content."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "3fbb4210-8795-48ae-97c3-c3618309e73f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "a = [1, 2, 3]\n",
    "b = [1, 2, 3]\n",
    "print(a is b)   # Output: False (different memory locations)\n",
    "# Although a and b have the same value, they are two different objects in memory, so a is b returns False."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "98e1471c-dfb2-4a5a-857e-7112f5b26b74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "\n",
    "x = 10\n",
    "y = 10\n",
    "print(x is y)   # Output: True (Python reuses small integers)\n",
    "# In this case, Python may point x and y to the same object in memory due to object caching for small integers and strings."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21bc4eed-2ed2-407c-a6bf-08831011c484",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "8464f3a2-ac7c-4ba0-b037-653a170cd1a0",
   "metadata": {},
   "source": [
    "Q:8 Explain the use of *args and **kwargs."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a41d3c02-d1b6-424f-9011-85b703cfb580",
   "metadata": {},
   "source": [
    "🔹 *args → Non-keyword variable-length arguments\n",
    "\n",
    "Accepts any number of positional arguments (like a tuple).\n",
    "\n",
    "Use when you want to pass multiple values without naming them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "05a8bf46-d9cd-4c0f-9f50-0f5eb8e7cba9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "def add(*args):\n",
    "    total = 0\n",
    "    for num in args:\n",
    "        total += num\n",
    "    return total\n",
    "\n",
    "print(add(1, 2, 3, 4))   # Output: 10\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6c89ffd-1264-456f-8459-23f6ca1b0da3",
   "metadata": {},
   "source": [
    "🔸 **kwargs → Keyword variable-length arguments\n",
    "\n",
    "Accepts any number of named arguments (like a dictionary).\n",
    "\n",
    "Use when you want to pass multiple key-value pairs."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "100ef836-0d87-4fb2-80d2-638d51364273",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name = Rahul\n",
      "age = 25\n",
      "country = India\n"
     ]
    }
   ],
   "source": [
    "def greet(**kwargs):\n",
    "    for key, value in kwargs.items():\n",
    "        print(f\"{key} = {value}\")\n",
    "\n",
    "greet(name=\"Rahul\", age=25, country=\"India\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "08c53ca0-b3b3-4497-ad83-41e8bafeaa5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Args: (1, 2, 3)\n",
      "Kwargs: {'name': 'Rahul', 'age': 20}\n"
     ]
    }
   ],
   "source": [
    "#  use both together\n",
    "\n",
    "def demo(*args, **kwargs):\n",
    "    print(\"Args:\", args)\n",
    "    print(\"Kwargs:\", kwargs)\n",
    "\n",
    "demo(1, 2, 3, name=\"Rahul\", age=20)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f7c52ce-aba8-4d62-a008-97f57c2db3a1",
   "metadata": {},
   "source": [
    "| Syntax     | Type            | Accepts                   | Stored As  |\n",
    "| ---------- | --------------- | ------------------------- | ---------- |\n",
    "| `*args`    | Positional args | Variable-length arguments | Tuple      |\n",
    "| `**kwargs` | Keyword args    | Variable-length key-value | Dictionary |\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b23b9d0-69ae-406c-8816-fc602a9ff41c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "42528270-b8a9-4ae5-b40a-9b7598dc0e4b",
   "metadata": {},
   "source": [
    "Q:9 What are Python modules and packages?\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "694e8ef9-204e-405d-a3f8-11245f1925e2",
   "metadata": {},
   "source": [
    "A module in Python is simply a file containing Python code — functions, classes, variables — that you can reuse in other programs using the import keyword.\n",
    "\n",
    "➤ In simple words:\n",
    "\n",
    "A module helps you organize your code and reuse functionality without rewriting it again and again."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca4fe92b-20d8-4894-b719-9fb0d6624bd3",
   "metadata": {},
   "source": [
    "✅ Types of Modules in Python\n",
    "1. Built-in Modules\n",
    "\n",
    "Provided by Python by default.\n",
    "\n",
    "Examples: math, os, random, datetime\n",
    "\n",
    "2. User-Defined Modules\n",
    "\n",
    "You can create your own module by saving functions or classes in a .py file.\n",
    "Example: my_module.py\n",
    "\n",
    "3. External Modules\n",
    "\n",
    "Not part of Python by default.\n",
    "\n",
    "Must be installed using pip (Python package manager).\n",
    "\n",
    "Examples: numpy, pandas, flask\n",
    "    \n",
    "    !pip instal numpy\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c9bf272-f96c-4367-a41f-e38861ab6118",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "4f52e0d8-60f8-4511-98e8-f7f51ed0fc48",
   "metadata": {},
   "source": [
    "🎯 Why Use Modules?\n",
    "\n",
    "✅ Code Reusability\n",
    "\n",
    "✅ Organized Code Structure\n",
    "\n",
    "✅ Avoid Code Duplication\n",
    "\n",
    "✅ Access to Powerful Libraries\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4439956-1af8-4512-8054-92fc92ad0d50",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "92410310-3bad-4820-a6c6-df06b605db5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.141592653589793\n"
     ]
    }
   ],
   "source": [
    "# import the whole module\n",
    "import math\n",
    "print(math.pi)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "34c7e1b0-a9b2-40ff-aa46-4bd72e7cffa0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.0\n"
     ]
    }
   ],
   "source": [
    "# import spesic function / class\n",
    "from math import sqrt\n",
    "print(sqrt(16))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "e48cd541-9929-46ad-a1ec-7e91d7b41efa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import with alias\n",
    "\n",
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "98a81021-41ab-466e-9635-b67e3f66925e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import everything ( not recommended)\n",
    "\n",
    "from math import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c7205af-9950-488d-8514-fa45e27fdcbb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "8b13e7b1-8df1-4b88-b5c5-e2c43db8a562",
   "metadata": {},
   "source": [
    "A package in Python is a collection of related modules organized in a folder (directory) that contains a special file named __init__.py.\n",
    "It helps you organize your code into multiple files for better structure and reusability.\n",
    "\n",
    "🧾 In Simple Words:\n",
    "    \n",
    "A package = folder that contains multiple Python files (modules) + __init__.py."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "e796a5cc-3ff1-4b60-b666-98a6ba0d9332",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid character '←' (U+2190) (2879328097.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[130], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    my_package/              ← This is the package\u001b[0m\n\u001b[1;37m                             ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid character '←' (U+2190)\n"
     ]
    }
   ],
   "source": [
    "my_package/              ← This is the package\n",
    "│\n",
    "├── __init__.py          ← Marks this folder as a Python package\n",
    "├── file1.py             ← Module 1\n",
    "├── file2.py             ← Module 2\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "08570a21-a4de-4f59-a14f-602a8045e6ac",
   "metadata": {},
   "source": [
    "\n",
    "🧠 Why Use Packages?\n",
    "\n",
    "\n",
    "✅ To organize code in large projects\n",
    "\n",
    "✅ To reuse code across multiple files\n",
    "\n",
    "✅ To avoid name conflicts using namespaces\n",
    "\n",
    "✅ Makes code clean, readable, and maintainable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d9de6a6-1922-4c5e-9496-b9f01a8accfe",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "112487c1-3102-458e-b26a-1ea9bfeff0b7",
   "metadata": {},
   "source": [
    "Q:10 What is the difference between local and global variables?\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51a2505b-299c-40a0-95c4-197596d1c4c1",
   "metadata": {},
   "source": [
    "🔹 Local Variable:\n",
    "\n",
    "Declared inside a function.\n",
    "\n",
    "Can be accessed only within that function.\n",
    "\n",
    "Created when the function is called, and destroyed when it ends.\n",
    "\n",
    "\n",
    "🔸 Global Variable:\n",
    "\n",
    "Declared outside all functions.\n",
    "\n",
    "Can be accessed anywhere in the program (inside and outside functions).\n",
    "\n",
    "Exists as long as the program runs.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef4074f0-b689-4920-9f1d-75c6c1f29485",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "727a451d-3ea5-4082-a015-aba15d8f5bcc",
   "metadata": {},
   "source": [
    "Q:11 What is a lambda function?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "06fb8722-c52d-4dd5-8395-d448b0fc1094",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
