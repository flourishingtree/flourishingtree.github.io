from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ranking')
def ranking():
    datalist = []
    con = sqlite3.connect("dataMax_2020.db")
    cur = con.cursor()
    sql = "select * from dataMax"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template('ranking.html',datalist=datalist)

@app.route('/wordcloud')
def wordcloud():
    return render_template('wordcloud.html')

@app.route('/data1')
def data1():
    return render_template('data1.html')

@app.route('/data2_2020')
def data2_2020():
    return render_template('data2_2020.html')


@app.route('/data2_2019')
def data2_2019():
    return render_template('data2_2019.html')

if __name__ == '__main__':
    app.run()
