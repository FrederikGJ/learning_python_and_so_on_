from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Define a route and a function to handle it
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run()


