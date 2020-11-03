from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)


@app.route("/",methods=['POST','GET'])
def account():
    if request.method == 'POST':
        print (request.form)
        name = request.form['name']
        city = request.form['city']
        return "Hello %s" %name + render_template('welcome.html')
    else:
        page ='''
        <html>
        <head>
            <link href="/static/css/cssWelcome.css" rel="stylesheet"/>
            <link href="https://fonts.googleapis.com/css2?family=Leckerli+One&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Itim&display=swap" rel="stylesheet">
            <style>
            body{
            background-color:#A2B6E4;
padding-left: 20%;
padding-right:20%;
            }
            .welcomeTitle{
                 height:300px;
                 position:relative;
                 }
            .title{
            color:#3354A0;
            font-size:2em;
            font-color:37559C;
            font-family:'Leckerli One', cursive;
            text-align:center;
            width:100%;
            position:absolute;
                top:30%;
                 }
                 label{
font-family:'Itim',cursive;
font-size: 30px;
                }
                #submit{
font-family:'Itim',cursive;

                 }
            </style>
        </head>
        <body>
            <div class="container-fluid welcomeTitle" >
                <div class="row title">
                <h2 class="title">Welcome to Shappy!</h2>
                </div>
            </div
            <div class="container">
                <div class="row">
                <form action="" method="post" name="form">
                <label for="name">What is your name?</label>
                <input type="text" name="name" id="name"/>
                </div>
                <div>
                <label for="city">What is the name of your city?</label>
                <input type="text" name="city" id="city"/>
                </div>
                <br>
                <div>
                <input type="submit" name="submit" id="submit"/>
                </form>
                </div>
            </div>
        </body>
        </html>'''

        return page,200
    

@app.route("/fstScreen", methods=['POST','GET'])
def firstScreen():
    return render_template('screen1.html')


@app.route("/scndScreen",methods=['POST','GET'])
def secondScreen():
    return render_template('screen2.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
