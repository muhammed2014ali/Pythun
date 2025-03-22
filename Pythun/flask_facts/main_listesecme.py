from flask import Flask
import time
import random
app = Flask(__name__)
facts_list = ["Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
            "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor.",
            "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
            "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir."]
@app.route("/")
def index():
    return f'<h1>MERHABA! Bu sayfada, teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz!</h1>'
@app.route("/rastgele_gercek")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'
app.run(debug=True)
@app.route("/tkm")


def tkm():
 return f'
facts_list =
# Kodunuzu buraya yazınız
SeninPuanin = 0
BilgisayarinPuani = 0
while True:
    sen = input("Birini seçiniz: taş/kağıt/makas")
    if sen == "taş" or sen == "kağıt" or sen == "makas":
        bilgisayar = random.randint(1,3)
        if bilgisayar == 1:
            bilgisayar = "taş"
        elif bilgisayar == 2:
            bilgisayar = "kağıt"
        elif bilgisayar == 3:
            bilgisayar = "makas"
        print("Taş", "Kağıt", "Makas")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        print("Bilgisayarın seçimi:", bilgisayar)
        time.sleep(1)
        if sen == bilgisayar:
            print("berabere")
        if sen == "taş" and bilgisayar == "makas":
            print("sen kazandın")
            SeninPuanin = SeninPuanin + 1
        elif sen == "makas" and bilgisayar == "kağıt":
            print("sen kazandın!")
            SeninPuanin = SeninPuanin + 1
        elif sen == "kağıt" and bilgisayar == "taş":
            print("sen kazandın")
            SeninPuanin = SeninPuanin + 1
        else:
            print("Bilgisayar kazandı")
            BilgisayarinPuani = BilgisayarinPuani + 1
        print("Şu anki puan durumu", "SeninPuanin:",SeninPuanin, "BilgisayarinPuani", BilgisayarinPuani)
    else:
             print("Böyle bir seçenek yok")
             '