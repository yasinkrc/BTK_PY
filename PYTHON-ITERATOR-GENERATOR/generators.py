# #Genel anlamda öğrenirsek ; 
# #Bizim için belekte yer etmeyen iterators üretiyor 

# # def cube():
# #     result=[]
    
# #     for i in range(5):
# #         result.append(i**3)
# #     return result


# # print(cube())

# def cube():
    
#     for i in range(4):
#         yield i**3

# generator=cube()
# iterator=iter(generator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator)) ==> bana hata veriyor bu 

# def cube():    
#     for i in range(5):
#         yield i**3 
#           #Buda önemli 
# for i in cube():
#     print(i)

# liste = [i**3 for i in range(5)]

# print(liste)
liste = (i**3 for i in range(5))

print(liste)
print(next(liste))
print(next(liste))
print(next(liste))
print(next(liste))
print(next(liste))