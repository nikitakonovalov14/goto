from PIL import Image
import random

text=input("введите расположение файла: ")
text_exit=input("введите место сохранения: ")
print("выберите фильтр:")
print("если хотите пленочный мир нажмите 1")
print("если хотите двуцветный мир нажмите 2")
print("если хотите шумно! нажмите 3")
print("если хотите 4-рматирование нажмите 4")
print("если хотите КЕК нажмите 5")
print("если хотите инверсию нажмите 6")
print("если хотите раздвоение нажмите 7")
print("если хотите необычный фильтр нажмите 8")
n=int(input(":"))


def plenochnyu_mir(text,text_exit):
    img = Image.open(text)
    pixels = img.load()
    k=0
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = pixels[i, j]

            k=r+b+g
            r=g=b=k//3
            pixels[i, j] = (r, g, b)


    img.show()

    # или сохраняем его в файл
    img.save(text_exit)

def two_colors_mir(text,text_exit):
    img = Image.open(text)

    pixels = img.load()
    k=0
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = pixels[i, j]

            k=r+b+g
            if(k//3>128):r=g=b=0
            else:r=g=b=255
            pixels[i, j] = (r, g, b)


    img.show()

    # или сохраняем его в файл
    img.save(text_exit)
    
def shumno(text,text_exit):
        
    n=random.randint(1,200)
    img = Image.open(text)

    pixels = img.load()
    k=0
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = pixels[i, j]
            if(r+n<255):r+=n
            else:r=255
            if(g+n<255):g+=n
            else:g=255
            if(b+n<255):b+=n
            else:b=255
            pixels[i, j] = (r, g, b)

    img.show()


    # или сохраняем его в файл
    img.save(text_exit)

def four_rmatirovanie(text,text_exit):
    img = Image.open(text)

    pixels = img.load()
    k=0
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = pixels[i, j]
            if(j<img.height//2):
                if(i<img.width//2):
                    r+=100
                    b+=100
                else:r+=100
            else:
                if(i<img.width//2):
                    g+=100
                else:b+=100
            
            pixels[i, j] = (r, g, b)


    img.show()

    # или сохраняем его в файл
    img.save(text_exit)

def KEK(text,text_exit):
    img = Image.open(text)

    pixels = img.load()
    k=0
    iw=img.width//2
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = pixels[i, j]
            if(i<iw):pixels[img.width-1-i,j]= (r,g,b)
        
            pixels[i, j] = (r, g, b)


    img.show()

    # или сохраняем его в файл
    img.save(text_exit)
    
def inversia(text,text_exit):
    img = Image.open(text)

    pixels = img.load()
    k=0
    iw=img.width//2
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = pixels[i, j]
            r=255-r
            g=255-g
            b=255-b
        
            pixels[i, j] = (r, g, b)


    img.show()

    # или сохраняем его в файл
    img.save(text_exit)
    
def razdvoenie(text,text_exit):
    img = Image.open(text)

    pixels = img.load()
    k=0
    iw=img.width//2
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = pixels[i, j]
            if(i<iw):pixels[i+iw,j]= (r,g,b)
        
            pixels[i, j] = (r, g, b)


    img.show()

    # или сохраняем его в файл
    img.save(text_exit)
    
def blur(text,text_exit):
    img = Image.open(text)

    pixels = img.load()
    
    k=0
    iw=img.width
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = pixels[i, j]
            
        
            pixels[i, j] = (r, g, b)


    img.show()

    # или сохраняем его в файл
    img.save(text_exit)
def new(text,text_exit):
    from PIL import Image
    import random
    m=20
    img = Image.open(text)
    text.replace(".jpg","")
    text+="-rjgbz.jpg"
    img.save(text)
    imgg = Image.open(text)
    pixels = img.load()
    k=1
    v = imgg.load()
    z=0
    if(img.width<200):
        print ("error")
    h=random.randint(7,10)
    a=random.randint(1,img.width)
    o=a+(img.width/100*h)//1
    n=[a]
    t=[0,]
    rr=[]
    rr+=[100]
    rr+=[50]
    rr+=[0]
    rr+=[0]
    rr+=[0]
    gg=[]
    gg+=[0]
    gg+=[50]
    gg+=[100]
    gg+=[50]
    gg+=[0]
    bb=[]
    bb+=[0]
    bb+=[0]
    bb+=[0]
    bb+=[50]
    bb+=[100]
    for i in range(1,6):
        t+=[img.width//5*i]
    for i in range(1,m+1):
        n+=[a+(o-a)//m*i]
    for i in range(img.width):
        k=0
        
        for j in range(img.height):
            
            
            if(i>a and i<n[19]):
                for l in range(m-1):
                    if(l%2==0):
                        if(i>n[l] and i<n[l+1]):
                            if(j+200<img.height):pixels[i,j]=v[i,j+200]
                            else:
                    
                                pixels[i,j]=v[i,k]
                                k+=1
                    else:
                        if(i>n[l] and i<n[l+1]):
                            if(j+img.height-200<img.height):pixels[i,j]=v[i,j+img.height-200]
                            else:
                    
                                pixels[i,j]=v[i,k]
                                k+=1
                    
                r, g, b = pixels[i, j]
    
                k=r+b+g
                r=g=b=k//3
                if(r>128):r+=30
                else:r-=30
                if(g>128):g+=30
                else:g-=30
                if(b>128):b+=30
                else:b-=30
                pixels[i, j] = (r, g, b)
            else:
                for l in range(4):
                    
                    if(i>t[l] and i<t[l+1]):
                        r, g, b = pixels[i, j]
                        r+=rr[l]
                        g+=gg[l]
                        b+=bb[l]
                        pixels[i, j] = (r, g, b)
    print(i)




    img.save(text_exit)

    
if(n==1): plenochnyu_mir(text,text_exit)
elif(n==2): two_colors_mir(text,text_exit)
elif(n==3): shumno(text,text_exit)
elif(n==4): four_rmatirovanie(text,text_exit)
elif(n==5): KEK(text,text_exit)
elif(n==6): inversia(text,text_exit)
elif(n==7): razdvoenie(text,text_exit)
elif(n==8): new(text,text_exit)
