import pandas as pd

# CSV dosyasını okuyun
df = pd.read_csv("imdb.csv")

# 1- Dosyada hakkındaki bilgiler.
result = df
result = df.columns
result = len(df.columns)
result = df.info

# 2- İlk 5 kaydı gösterin
result = df.head()

# 3- İlk 10 kaydı gösterin
result = df.head(10)

# 4- Son 5 kaydı gösterin
result = df.tail()

# 5- Son 10 kaydı gösterin
result = df.tail(10)

# 6- Sadece Movie_Title kolonunu alın.
result = df["Name"]

# 7- Sadece Movie_Title kolonunu içeren ilk 5 kaydı alın.
result = df["Name"][:5]

# 8- Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın.
result = df[["Name", "Duration"]][:5]
result = df[["Name", "Duration"]].head()

# 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın.
result = df[["Name", "Duration"]].tail(7)

# 10- Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alın.
result = df[["Name", "Duration"]][6:11]
result = df[5:10][["Name", "Duration"]]
result = df[5:20][["Name", "Duration"]].head()

# 11- Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 
#     ve üstünde olan kayıtlardan ilk 50 tanesini alınız.
# Önce "Rate" sütununu sayısal bir türe (float) dönüştürün
df["Rate"] = pd.to_numeric(df["Rate"], errors="coerce")
result = df[df["Rate"] >= 8.0][["Name", "Rate"]].head(50)

# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.
# Şu kodu kullanabilirsiniz:
result = df[(df["Date"] >= 2014) & (df["Date"] <= 2015)]["Name"]

# 13- Değerlendirme sayısı (Num_Reviews) 100.000'den büyük ya da imdb puanı
#     8 ile 9 arasında olan filmleri listeleyiniz.

# 13- Değerlendirme sayısı (Num_Reviews) 100.000'den büyük ya da imdb puanı
# 8 ile 9 arasında olan filmleri listeleyiniz.

# "Votes" sütununu sayısal bir türe (integer) dönüştürün
df["Votes"] = pd.to_numeric(df["Votes"], errors="coerce")

result = df[(df["Votes"] > 100000) | ((df["Rate"] >= 8) & (df["Rate"] <= 9))]["Name"]
print(result)
