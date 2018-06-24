from flask import Flask,request,g,current_app,render_template
from flask import url_for, redirect,Response
import time,json
app = Flask(__name__)
time = time.time()

with app.app_context():
    # within this block, current_app points to app.
    #time = time.time()
    print current_app.name

@app.route('/')
def hello_world():
    #g.time = time.time()
    #print g.time
    #hello()
    #return "helloworld"
    #return redirect(url_for('hello',ag="testa",bg="testb"))
    return render_template("index.html")

@app.route('/testarg',methods=['GET','POST'])
def hello():
    ag = request.args.get("ag")
    bg = request.args.get("bg")
    print time
    #ag = "ag"
    #bg = "bg"
    print ag
    print bg
    return 'Hello World!'

@app.route('/search',methods=["GET","POST"])
def search():
    search = ["ab","cd","ef","gh","ij","kl"]
    return render_template("search.html",**locals())
@app.route('/liandong',methods=["GET","POST"])
def liandong():
    data = request.form.get('se_program')
    print data
    print request.form
    PlatFormList = []
    if data == "ab":
        PlatFormList = ["1","2"]
    elif data == "cd":
        PlatFormList = ["3","4","5"]
    elif data == "ef":
        PlatFormList = ["6","7","8"]
    else:
        print "no data"
    print type(PlatFormList)
    platform = json.dumps(PlatFormList)
    print type(platform)
    # platform=set(platform)
    print platform
    #return Response(json.dumps(platform), mimetype='application/json')
    return platform
    #return render_template("search.html",platform)
@app.route('/liandong1',methods=["GET","POST"])
def liandong1():
    data = request.form.get('se_platform')
    print data
    print request.form
    PlatFormList = []
    if data == "1":
        PlatFormList = ["1","2"]
    elif data == "2":
        PlatFormList = ["3","4","5"]
    elif data == "3":
        PlatFormList = ["6","7","8"]
    else:
        print "no data"
    print type(PlatFormList)
    platform = json.dumps(PlatFormList)
    print type(platform)
    # platform=set(platform)
    print platform
    #return Response(json.dumps(platform), mimetype='application/json')
    return platform
    #return render_template("search.html",platform)


if __name__ == '__main__':
    app.run()
