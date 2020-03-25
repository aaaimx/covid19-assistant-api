from flask import Flask, request

app = Flask(__name__)

@app.route('/diagnosis', methods = ['POST'])
def diagnosis():
    if('values' in request.json and type(request.json['values']) == list):
        print(request.json['values'])
    return 'Hola'


@app.errorhandler(404)
def page_not_found(error):
    return 'error', 404

if __name__ == "__main__":
    app.run(port = 3000, debug = True)
