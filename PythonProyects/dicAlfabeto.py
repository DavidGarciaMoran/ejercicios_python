
def createDic(vocales, num_):
    d = dict(zip(vocales, num_))
    return d


vocales = ['a','b','c','d','e','f','g','h','i','j']
num_ = [1,2,3,4,5,6,7,8,9,10]
dic = createDic(vocales, num_)
print(dic)