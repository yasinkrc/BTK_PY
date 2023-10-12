import pandas as pd 

df=pd.read_csv("dataset\\youtube-ing.csv")

# 1- İlk 10 kaydı getiriniz.
result=df.head(10)
# 2- İkinci 5 kaydı getiriniz.
result=df[5:10].head()
# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
for i in  df.columns :
    pass
result=len(df.columns)
    
# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
# df=df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1,inplace=True)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)
result=df
# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result=df["likes"].mean()
result=df["dislikes"].mean()
# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result=df.head(50)[["title","likes","dislikes"]]
# 7- En çok görüntülenen video hangisidir ?
# result=df[df["views"].max()]["title"] ---> hatalı
result=df[df["views"]==df["views"].max()][["title","views"]]
result=df[df["views"]==df["views"].max()][["title","views"]].iloc[0]
# 8- En düşük görüntülenen video hangisidir?
result=df[df["views"]==df["views"].min()][["title","views"]].iloc[0]
# 9- En fazla görüntülenen ilk 10 video hangisidir ?

result=df.sort_values("views",ascending=False).head(10)[["title","views"]]
result=df.sort_values("views",ascending=False).head(10)

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.

# Convert the "likes" column to a numeric data type (assuming it's currently stored as strings)
df['likes'] = pd.to_numeric(df['likes'], errors='coerce')  # 'coerce' option handles any non-numeric values by converting them to NaN

# Group by "category_id," calculate the mean of "likes," and sort the result
result = df.groupby("category_id")["likes"].mean().sort_values()

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız
result = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]

# 12- Her kategoride kaç video vardır ?
result=df["category_id"].value_counts()
# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
# result=df["title"]
# df["newcolon"]
# for i in df["title"]:
#     df["newcolon"]=len(i)  

# result=df[["title","newcolon"]]

""" 
Yukarıdaki koda hata var o hatayı düzeltmek için aağıdaki koda bak 
"""
df["title_len"]=df["title"].apply(len)

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
# df["tag_count"]=df["tags"].apply(lambda x : len(x.split('|')))

def tagcount(tag):
    return len(tag.split('|'))
df["tag_count"]=df["tags"].apply(tagcount).head(50)
# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)

# likesList=list(df["likes"])
# dislikesList=list(df["dislikes"])
# # print(likesList,dislikesList)

def likedislikeoranhesapla(dataset):
    likesList=list(dataset["likes"])
    dislikesList=list(dataset["dislikes"])
    
    liste=list(zip(likesList,dislikesList))
    
    oranListesi=[]
    
    for like , dislike in liste :
        
        if (like+dislike)==0:
            oranListesi.append(0)
        else :
            oranListesi.append(like/(like+dislike))    
    return oranListesi

df["beğeni_orani"]=likedislikeoranhesapla(df)
print(df.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]])