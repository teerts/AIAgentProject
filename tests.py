import os
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def run_tests():
    print("Result for current directory:")
    result = get_files_info("calculator", ".")
    print(result)
    print()

    print("Result for 'pkg' directory:")
    result = get_files_info("calculator", "pkg")
    print(result)
    print()

    print("Result for '/bin' directory:")
    result = get_files_info("calculator", "/bin")
    print(f"    {result}")
    print()

    print("Result for '../' directory:")
    result = get_files_info("calculator", "../")
    print(f"    {result}")
    print()

    print("Result for 'calculator/main.py' file:")
    result = get_file_content("calculator", "main.py")
    print(f"    {result}")
    print("Result for 'calculator/pkg/calculator.py' file:")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"    {result}")
    print("Result for 'calculator/bin/cat' file:")
    result = get_file_content("calculator", "/bin/cat") 
    print(f"    {result}")

    print("Result for writing to lorem.txt file:")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"    {result}")
    print("Result for writing to pkg/morelorem.txt file:")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"    {result}")
    print("Result for writing to /tmp/temp.txt file:")
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"    {result}")

    print("Running a Python file:")
    result = run_python_file("calculator", "main.py")
    print(f"    {result}")
    print("Running a Python file:")
    result = run_python_file("calculator", "nonexistent.py")
    print(f"    {result}")
    print("Running a Python file:")
    result = run_python_file("calculator", "../main.py")
    print(f"    {result}")


if __name__ == "__main__":
    run_tests()
