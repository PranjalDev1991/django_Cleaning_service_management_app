print("Stmt1")
try:
    x=int(input("Enter the num1"))
    y=int(input("Enter the num2"))
    print(x/y)
    try:
        print("This is inner block")
    except:
        print("Inner block executed")
except ZeroDivisionError as  msg:
    print("Omg its ",msg)
except ValueError:
    print("Its a value error")
else:
    print("Code excecuted")
finally:
    print("stmt3")
