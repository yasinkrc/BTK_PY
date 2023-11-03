"""#error handling
try :
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)
except ZeroDivisionError :
    print("Y için sıfır girilemez ")
except ValueError :
    print("x ve y için sayısal değer girmelisiniz .") """
#error handling
""" try :
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)
except (ZeroDivisionError , ValueError , SyntaxError , EOFError , OSError):
    print("Hata ile karşılaştın ! ") """

try :
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)
except (ZeroDivisionError , ValueError , SyntaxError , EOFError , OSError) as e :
    print("Hata ile karşılaştın ! : ",e)




