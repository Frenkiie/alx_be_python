# main.py

from fns_and_dsa.arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("أدخل الرقم الأول: "))
    num2 = float(input("أدخل الرقم الثاني: "))
    operation = input("أدخل العملية (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"النتيجة: {result}")

if __name__ == "__main__":
    main()
