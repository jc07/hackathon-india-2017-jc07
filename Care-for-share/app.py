from flask import Flask, render_template , request


app = Flask(__name__)
   

@app.route("/")
def main():
    return render_template('home.html')


@app.route("/morty")
def morty():
    return render_template('index.html')


@app.route("/rick")
def rick():
    return render_template('index1.html')

@app.route('/showNotify')
def showSignUp():
    return render_template('signup.html')

@app.route('/showRains')
def showRains():
    return render_template('rains.html')


@app.route('/showTra')
def showTra():
    return render_template('jam.html')



@app.route('/inform' , methods=['POST'])
def inform():

    _time=request.form['inputtime']
    _area=request.form['inputarea']
    file =open("/home/johnny/Desktop/check.txt","w")
    print _time , _area
    file.write(_time+"\n")
    file.write(_area+"\n")
    return render_template('thanks.html')

@app.route('/showMyacc')
def showMyacc():
    return render_template('me.html')


if __name__ == "__main__":
    app.run()