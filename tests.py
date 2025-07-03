import os
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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

if __name__ == "__main__":
    run_tests()
