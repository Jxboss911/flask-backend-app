from flask import Flask, request

# Initialize Flask app
app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '''
        <h1>Welcome to the Flask Backend App!</h1>
        
        <a href="/add?a=2&b=3">Try adding 2 and 3</a><br>
        
        <a href="/subtract?a=5&b=2">Try subtracting 5 and 2</a>
    '''

# Addittion route
@app.route('/add')
def add():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        result = a + b
        return f"<h1>{a} + {b} = {result}</h1>"
    except ValueError:
        return "<h1>Invalid input, please provide two integers.</h1>"

# Subtraction route
@app.route('/subtract')
def subtract():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        result = a - b
        return f"<h1>{a} - {b} = {result}</h1>"
    except ValueError:
        return "<h1>Invalid input, please provide two integers.</h1>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
