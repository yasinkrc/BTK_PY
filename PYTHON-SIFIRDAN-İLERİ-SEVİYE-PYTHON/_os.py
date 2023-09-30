import os 
import datetime
#os modülü genelikle işletim sistemi hakkında bize bilgiler sunar 

result=dir(os)
result=os.name # 'nt' demek Microsoft demek  işetim sistemi 

""" Dizi değiştirme """
# os.chdir('C:\\') #konum değiştirir 
# os.chdir('../../..') #kaç tane kullanırsan o kadar geri gider

"""Klasör oluşturma """
# os.mkdir("newdirectory") #aynı dizin içerisinde yeni bir klasör oluşturur
# os.makedirs('newdirectory/yeniklasör') #iç içe dizi oluşturur
# os.rename("newdirectory","yeniklasörX") #klasörün adını değiştiriyor
# os.rmdir("newdirectory")  #altdizinleri yoksa tek de bunu kullan 
# os.removedirs("yeniklasörX\yeniklasör") #altdizinleri varsa 



""" Listeleme   """
# result=os.listdir() # o dizi içinde ne varsa listeler
# result=os.listdir("C://")  #özel bir konumun içinde listeleme yapar 
#peki bunları nasıl temizleriz ? 

# for dosya in os.listdir():
    
#     if dosya.endswith('py'):
#         print(dosya)


""" Etkin dizi öğrenme """
# result=os.getcwd() #C:\Users\ismai\OneDrive\Masaüstü\yasin_pc\sıfırdan_python\PYTHON-SIFIRDAN-İLERİ-SEVİYE-PYTHON

result=os.stat('date.py')
""" os.stat_result(st_mode=33206, st_ino=4785074604248122, st_dev=537704065, 
st_nlink=1, st_uid=0, st_gid=0, st_size=2038, st_atime=1695927775,  
st_mtime=1695926158, st_ctime=1695922086)"""
# result=result.st_size/1024 #dosyanın kaç mb olduğunu hesaplıyor 
# result=datetime.datetime.fromtimestamp(result.st_ctime )#dosyanın oluşturma zamanını paylaşıyor 
# result=datetime.datetime.fromtimestamp(result.st_mtime) #son değiştirilme tarihi 
# result=datetime.datetime.fromtimestamp(result.st_atime) #son erişilme tarihi

# os.system("notepad.exe") #bir uygulmayı çalıştırma 


""" PATH İŞLEMLERİ """ 


#result=os.path.abspath("_os.py") #bize bir dosyanın tam konumunu verir bu yüzden önemli
# result=os.path.dirname('C:/Users/ismai/OneDrive/Masaüstü/yasin_pc/sıfırdan_python/PYTHON-SIFIRDAN-İLERİ-SEVİYE-PYTHON/_os.py')
#yukarıdaki bize dosyanın dizini verir ama dikkat et değiştirmen gerek \ with / 
# result=os.path.dirname(os.path.abspath('_os.py')) sadece osya ismi biliyoruz var say
# result=os.path.exists('_os.py') #dizinde olup olmadığını söyler TRUE-FALSE
# result=os.path.exists("C:/Users/ismai/OneDrive/Masaüstü/yasin_pc/sıfırdan_python/PYTHON-SIFIRDAN-İLERİ-SEVİYE-PYTHON/_os.py")
# result=os.path.exists("C:/Users/ismai/OneDrive/Masaüstü/yasin_pc/sıfırdan_python/PYTHON-SIFIRDAN-İLERİ-SEVİYE-PYTHON") #klasör sorgulama 

# result=os.path.isdir("C:/Users/ismai/OneDrive/Masaüstü/yasin_pc/sıfırdan_python/PYTHON-SIFIRDAN-İLERİ-SEVİYE-PYTHON") #bir klasör mü ? 
# result=os.path.isfile("C:/Users/ismai/OneDrive/Masaüstü/yasin_pc/sıfırdan_python/PYTHON-SIFIRDAN-İLERİ-SEVİYE-PYTHON/_os.py") #bir dosya mı ?
# result=os.path.join('C://','deneme','deneme1') #kafana göre birleştir  C://deneme\deneme1
# result=os.path.split("C://deneme")  #('C://', 'deneme')
# result=os.path.splitext("_os.py") #dosyanın ismi ve uzantısını ayırır
# result=result[0]
# result=result[1]
print(result)