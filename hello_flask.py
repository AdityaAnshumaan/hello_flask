import flask

# Create the application.
app = flask.Flask(__name__)

@app.route('/') #mapping the / value to a specific function
def index():
    return flask.render_template('index copy.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
