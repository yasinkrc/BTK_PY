import pandas as pd 

data =pd.read_csv("nba.csv")

#Eğer baktın elemanlar var  ve sen  bu verileri kullanmak istemiyorsun o  o zaman yapman gereken 
#Bir fonksiyon var 

# data =data.dropna() --> şimdi yazdığın bu kod tamam iyi de ama eğer direk sayfada değişiklik yapmak istersin diye aşağıda 

# data=data.dropna(inplace=True) --> adamda çalıştı ama bende ne yaziki çalışmadı :(
data=data.dropna()

# data["player_name"]=data["player_name"].str.upper()
# data["player_name"]=data["player_name"].str.lower()
# data["index"]=data["player_name"].str.find('a')
# data = data["player_name"].str.contains("Eddie Johnson")
# data=data.college.str.replace(" ","-").str.replace("*","")
data[['FirstName','LastName']] = data['player_name'].loc[data['player_name'].str.split().str.len()==2].str.split(expand=True)
 

print(data.head(10))