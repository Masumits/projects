import json
from flask import Flaks
app = Flask(__name__)

@app.route('/')

def j():
    d = {'pain':'an unpleasant physical feeling caused by an illness or injury',
         'stress': 'feelings of worry caused by difficult situations such as problems at work'}
    f = open ('C:\\Users\\North Star\\Desktop\\data.json', 'w')
    json.dump(d, f, ensure.ascii =False, indent=2)
    f.close()

def fl(name=None):
    # string = 'ill'( а в коде будет {{some.string}} и она заменится на то, что я ввела), если  some.string|length, то будет 1234)
    return render_template('f.html', #name(в шаблоне)=name(переменная) #somestring= string)

if __name__ == '__main__':
    app.run(debug=True)


#{% for i in d%}
#{% endfor %} для того, чтобы бесконечное кол-во переменных отражать в коде на странице
