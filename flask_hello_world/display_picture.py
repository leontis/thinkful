from flask import Flask

app = Flask(__name__)

""" Fire this up by typing:
python display_picture.py
To view the webpage go to http://0.0.0.0:8080/

"""

@app.route("/hello")
def hello_world():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hello_person(name):
    return "Hello {}!".format(name.title())

@app.route("/see/cat/<name>")
def hello_cat(name):
    html = """
        <h1>
            Hello {} here are two Kittens!
        </h1>
        <p>
            Aren't they cute? 
        </p>
        <img src="http://images.wisegeek.com/young-kittens.jpg">   
    """ 
    return html.format(name.title())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
