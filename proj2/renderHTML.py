from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def account():
    list=[
('static/triangle.png'),('static/heart.png') ]

    if request.method == 'POST':
        print (request.form)
        name = request.form['name']
        city = request.form['city']
        return redirect(url_for('first'))
   # "Hello %s" %name +"\n" + "in %s" %city + render_template ('base.html')
    


    else:
        page ='''
        <html><body>
        <form action="" method="post" name="form">
             <label for="name">Please, write your name:</label>
             <input type="text" name="name" id="name"/>
           
             <label for="city">What is the name of your city?:</label>
             <input type="text" name="city" id="city"/>
             <input type="submit" name="submit" id="submit"/>
        </form>
        </body></html>'''
        
        return page, 200

@app.route("/first",methods=['POST','GET'])
def first():
    return "Hello"

    if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)
