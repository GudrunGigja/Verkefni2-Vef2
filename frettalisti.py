from flask import Flask
from flask import render_template

app = Flask(__name__)

frettaListi = [
{
            "id": 0,
            "flokkur": "sport",
            "hofundur": "Lightning Mcqueen",
            "fyrirsogn": "Hungary vs England: The journey starts again for Gareth Southgate's side",
            "meginmal": "A small army of Hungarians is said to invade the castle that the queen of England lives in in approx. t-21 minutes. The queen has beefed up her security and sacrificed seven lambs to Geras, the greek god of old age as to lengthen her lifespan even more and give her the physicall strength of ten bulls.",
            "mynd": "mynd2.jpg",
        },
        {
            "id": 1,
            "flokkur": "tolvuleikir",
            "hofundur": "George R.R. Martain",
            "fyrirsogn": "Elden Ring",
            "meginmal": "Elden Ring is an upcoming action role-playing game developed by FromSoftware and published by Bandai Namco Entertainment. The game is a collaborative effort between game director Hidetaka Miyazaki and fantasy novelist George R. R. Martin. It is scheduled to be released for Microsoft Windows, PlayStation 4, PlayStation 5, Xbox One, and Xbox Series X/S on January 21, 2022.",
            "mynd": "mynd1.jpg",
        },
        {
            "id": 2,
            "flokkur": "sport",
            "hofundur": "Mikasa Ackermann",
            "fyrirsogn": " Best vollyball team enters the stage",
            "meginmal": " The story follows Shōyō Hinata, a boy determined to become a great volleyball player despite his small stature. It was serialized in Shueisha Weekly Shōnen Jump from February 2012 to July 2020, with its chapters collected in forty-five tankōbon volumes.",
            "mynd": "mynd5.jpg",
        },
        {
            "id": 3,
            "flokkur": "tolvuleikir",
            "hofundur": "Jakob Reiss",
            "fyrirsogn": "GTA IRL",
            "meginmal": "GTA announces their next game will be only avalable in VR. This has caused teens all over the world to buy VR headgear and are preparing to use the game as an emotional outlet. San diego police officials have a lot to say about this.",
            "mynd": "mynd3.jpg",
        },
        {
            "id": 4,
            "flokkur": "almennt",
            "hofundur": "Steinunn Helga",
            "fyrirsogn": "Hundur verpti eggjum",
            "meginmal": "Hundur verpti eggjum úti á Hvalsfyrði í Saurbæ klukkan 12:30 í gærkvöldi, eigendur segja að þetta atvik spái fyrir næstu stjórnmálaflokka kosningum.",
            "mynd": "mynd4.jpg",
        },
        {
            "id": 5,
            "flokkur": "almennt",
            "hofundur": "Eren Yaeger",
            "fyrirsogn": "Bird watching at its finest",
            "meginmal": "This last december five brothers went on vacation to Paradie island to go bird watching. They Stayed in a cabin in the middle of no where for three years all together totally sustainable. All they did was watch and record birds on their cameras and endless ram. One time one of them even watched a single bird from birth to death in one sitting.",
            "mynd": "mynd0.jpg",
        }
]

@app.route("/")
def index():
    return render_template('index.html', lf = frettaListi)

@app.route('/frett/<int:id>')
def frett(id):
    frett = frettaListi[id]
    return render_template('frett.html', frett=frett)

@app.route('/frettalisti/<flokkur>')
def frettalisti(flokkur):
    return render_template('frettalisti.html', lf = frettaListi, flokkur = flokkur)

if __name__ == "__main__":
    app.run(debug=True)
