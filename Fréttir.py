from flask import Flask
from flask import render_template

app = Flask(__name__)

frettalisti = [
{
            "id": 0,
            "flokkur": "lifstill",
            "hofundur": "Lightning Mcqueen",
            "fyrirsogn": "How to run faster by changing the way you poop",
            "meginmal": "Ever wondered why you can’t meet your fitness goals? Behavioural scientist Emily Balcetis turned to elite runners to find the answer. She proposes a strategy that consists of changing your poop focus.",
            "mynd": "hlaup.jpg",
        },
        {
            "id": 1,
            "flokkur": "Lifstill",
            "hofundur": "Steve Hellington",
            "fyrirsogn": "The therapy used by Stalin and still popular in Russia",
            "meginmal": "Leech therapy is an ancient and controversial cure that has become an alternative choice of therapy for Russia’s health-conscious, environmentally aware younger generation.We visit one of Russia’s premiere hirudotherapy clinics to observe the leeches and take a look at the world's largest leech farm, to see how these fascinating creatures are reared.",
            "mynd": "mynd1.jpg",
        },
        {
            "id": 2,
            "flokkur": "Dyralif",
            "hofundur": "Steve Wellington",
            "fyrirsogn": "The psychedelic power of the Sonoran Desert toad",
            "meginmal": "In Mexico City, some young people take part in psychedelic rituals, as they believe it helps them spiritually and to ease daily stresses. Arturo, a 'shaman', hosts ceremonies in the city's urban mesh, where participants can get an intimately guided dose of Bufo Alvarius, also known as the Sonoran Desert toad.The toad contains the psychoactive alkaloid 5-MeO-DMT and is regarded as the 'God molecule'.",
            "mynd": "mynd2.jpg",
        },
        {
            "id": 3,
            "flokkur": "Utlond",
            "hofundur": "Jakob Reiss",
            "fyrirsogn": "Texans can now openly carry guns in public without a permit or training. Police say the new law makes it harder to do their jobs",
            "meginmal": "A new pro-gun law in Texas that went into effect Wednesday allows most Texans who legally own a firearm to carry it openly in public without obtaining a permit or training, a measure that experts say will make it more challenging for law enforcement to protect the public from gun violence.",
            "mynd": "mynd3.jpg",
        },
        {
            "id": 4,
            "flokkur": "Dyralif",
            "hofundur": "Steinunn Helga",
            "fyrirsogn": "Comedy Wildlife Photography Awards 2021 finalists revealed",
            "meginmal": "A seal that appears to be giggling, a baboon that looks like it's singing and a very angry starling - this year's finalists show animals in comedy moments snapped by photographers from around the world.",
            "mynd": "mynd4.jpg",
        },
        {
            "id": 5,
            "flokkur": "Utlond",
            "hofundur": "Eren Yaeger",
            "fyrirsogn": "Canada federal election: How much trouble is Trudeau in?",
            "meginmal": "Canada's Justin Trudeau called a snap election in mid-August hoping an early campaign could net his Liberals a majority government. But with their lead in the poll vanishing at the campaign's halfway point, is one still within reach?",
            "mynd": "mynd5.jpg",
        }
]

@app.route("/")
def index():
    return render_template('index.html', fl = frettalisti)

@app.route('/frett/<int:id>')
def frett(id):
    frett = frettalisti[id]
    return "Frétt nr. %s" %id

if __name__ == "__main__":
    app.run(debug=True)
