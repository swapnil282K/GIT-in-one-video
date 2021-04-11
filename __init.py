from flask import flask
app=flask(__name__)

@app.route('/')
def hello_word():
    return 'Hello World'

if __name__=="__main__"
    app.run(debug=True)