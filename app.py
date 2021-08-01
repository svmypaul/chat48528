from flask import Flask, render_template,request
import pickle
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('intro.html')



@app.route('/enter',methods = ['POST', 'GET'])
def data():
    if request.method == 'POST':
      name = request.form['input']
      if name=='svsree':
          dat = []
          with open('text', 'rb') as fr:
              try:
                  while True:
                      dat.append(pickle.load(fr))
              except EOFError:
                  pass
          return render_template('index.html',dat=dat,name=name)
      elif name=='svmy':
           dat = []
           with open('text', 'rb') as fr:
              try:
                  while True:
                      dat.append(pickle.load(fr))
              except EOFError:
                  pass
           return render_template('index.html',dat=dat,name=name)
      else:
          return render_template('intro.html')


@app.route('/chat/<name>',methods = ['POST', 'GET'])
def chat(name):
    if request.method == 'POST':
        text= request.form['text']
        if text=='':
            print("no input")
            dat = []
            with open('text', 'rb') as fr:
                try:
                    while True:
                        dat.append(pickle.load(fr))
                except EOFError:
                    pass
            return render_template('index.html',dat=dat,name=name)
        else:
            dat = []
            with open('text', 'rb') as fr:
                try:
                    while True:
                        dat.append(pickle.load(fr))
                except EOFError:
                    pass
            file = open("text",'wb')
            time=datetime.today().strftime("%H:%M %p")
            dbf=str(text)+'     ' + str(time)
            dict={name : dbf}
            
            for item in dat:  
                pickle.dump(item,file)
            pickle.dump(dict,file)
            file.close()
            return render_template('index.html',text=text,dat=dat,name=name)

@app.route('/clear',methods = ['POST', 'GET'])
def clear():
    if request.method == 'POST':
        item=[]
        file = open("text",'wb')
        pickle.dump(item,file)
        return render_template('intro.html')

if __name__ == "__main__":  
    app.run(debug=True)