import turtle
import random

cizim_tahtasi=turtle.Screen()
cizim_tahtasi.bgcolor("light green")
cizim_tahtasi.title("Catch The Turtle")

FONT=("verdana",18,"normal")
skor=0
game_over=False

# skor turtle
score_turtle=turtle.Turtle()

#GeriSayım turtle
geriSayim_turtle=turtle.Turtle()

grid_boyutu=10 #ekran büyürse yada  oyun zorluğu için bu değer değiştirebilinir.
turtle_listesi=[]


'''turtle_olustur(20,10)
turtle_olustur(-0,10)
turtle_olustur(-20,10)
turtle_olustur(-40,10)'''


'''for i in range(-20,20,+10):
    for j in range(20,-20,-10):
        turtle_olustur(i,j)
bunun diğer bir hali aşağıda yapabilirsin
'''
x_koordinatlari=[-20, -10, 0, 10, 20]
y_koordinatlari=[20, 10, 0, -10]

def skoruAyarlaTurtle():

    score_turtle.hideturtle()
    score_turtle.color("dark blue")

    yukseklik=cizim_tahtasi.window_height()/2  # (0,0) posizyonu ekranın yarısında başlar

    #print(yukseklik)
    y_koordinati=yukseklik*0.9
    #print(y_koordinati)
    score_turtle.penup()

    score_turtle.setposition(0,y_koordinati)
    score_turtle.write(arg="Score : 0",move=False,align="center",font=FONT)


def turtle_olustur(x,y):
    t=turtle.Turtle()

    def turtlea_tikla(x, y):
        global skor
        skor += 1
        score_turtle.clear()  # önceki skor bilgisini sildik
        score_turtle.write(f"Score : {skor}", move=False, align="center", font=FONT)
        # print(x,y)
    t.onclick(turtlea_tikla)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x*grid_boyutu,y*grid_boyutu)
    turtle_listesi.append(t) #olusturulan turtleları tek tek listeye aldık


def tumKaplumbagalari_olustur():
    for i in x_koordinatlari:
        for j in y_koordinatlari:
            turtle_olustur(i,j)

def turtlelari_gizle():
    for t in turtle_listesi:
        t.speed("slowest")
        t.hideturtle() #olusturulan turtleları tek tek gizledik


def rastgele_turtle_goster():
    if not game_over: #oyun devam ediyorsa bunları yap game over true olursa burası çalışmamalı
        random.choice(turtle_listesi).showturtle()
        turtlelari_gizle()
        if True:  # start again in the future if still needed
            cizim_tahtasi.ontimer(rastgele_turtle_goster, 500)  # her 0.5 saniyede tekrar eder. recursive fonks oluşturduk fonks içinde çonksyion çağırdık



def countdown(time):
    global game_over
    geriSayim_turtle.hideturtle()
    geriSayim_turtle.color("dark blue")

    yukseklik=cizim_tahtasi.window_height()/2  # (0,0) posizyonu ekranın yarısında başlar

    #print(yukseklik)
    y_koordinati=yukseklik*0.9
    #print(y_koordinati)
    geriSayim_turtle.penup()

    geriSayim_turtle.setposition(0,y_koordinati-30)


    geriSayim_turtle.clear()
    #print(time)

    if time > 0:
        geriSayim_turtle.clear()

        geriSayim_turtle.write(arg=f"Süre : {time}",move=False, align='center', font=FONT)
        cizim_tahtasi.ontimer(lambda: countdown(time - 1), 1000)

    else:
        game_over=True
        geriSayim_turtle.clear()
        turtlelari_gizle()
        geriSayim_turtle.write("GAME OVER ! ", align='center', font=FONT)


def oyunu_baslat():
    global game_over
    game_over=False
    turtle.tracer(0) #takip etme olayı turtle'ları tek tek oluşumları beklemeye gerek yok bitince direk göster izleyici görevi budur
    skoruAyarlaTurtle()
    tumKaplumbagalari_olustur()
    turtle.speed("slow")
    turtle.hideturtle()
    turtlelari_gizle()

    rastgele_turtle_goster()

    cizim_tahtasi.ontimer(lambda : countdown(10),10)
    turtle.tracer(1)

oyunu_baslat()
turtle.mainloop() #oyunu sürekli takip eder tıklama tapılmış mı edilmiş mi, eğer time modülünde time.sleep() kullnılırsa diğer tarafları bloklar durdurur.




