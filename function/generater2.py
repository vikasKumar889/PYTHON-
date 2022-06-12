def acronym_generator(listofword):
    for word in listofword:
        w1 = word.split()
        acr =""
        for w in w1:
            acr += w[0].upper()
        yield acr

words =  ['Project Manager','Software Engineer','Database Administrator']
for acr in acronym_generator(words):
    print(acr)          
