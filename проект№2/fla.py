from flask import Flask
from flask import render_template, request, redirect, url_for
import json 

app = Flask(__name__)
            
@app.route('/')
def glavnaya():
    urls = { 'Главная страница с анкетой': url_for('profile'),
             'Страница статистики': url_for('stats'),
             'Страница с выводом данных': url_for('js'),
             'Страница поиска': url_for ('search'),}
    return render_template('index.html', urls=urls)
    
@app.route('/profile')
def profile():
    if request.args:
        f = open('data.json', 'a', encoding='utf-8')
        s = json.dumps(request.args, f, ensure_ascii =False )
        f.write(s + '\n')
        f.close()
    return render_template('profile.html')

@app.route('/stats')
def stats():
    fi = open ('data.json', 'r', encoding = 'utf-8')
    answers = []
    for m in fi:
        answer = json.loads(m)
        answers.append(answer) #я сделала массив из словарей, нужно их распихать
    return render_template('stat.html', answer=answers)

@app.route('/json')
def js():
    fil = open('data.json', 'r', encoding = 'utf-8')
    return render_template('js.html', answer1=fil)


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/results')
def results():
    file = open('data.json', 'r', encoding='utf-8')
    data = json.load(file)
    language = request.args['language']
    age = request.args['age']
    country = request.args['country']
    results = []
    for answer1 in data:
        for a in answer1:
            if word in a:
                results.append(a)
    if results == []:
        results.append('')
    else:
        for r in results:
            results = str() + r
    return render_template('results.html', results=results, language = language, age = age, country = country)

if __name__ == '__main__':
    app.run(debug=True)
