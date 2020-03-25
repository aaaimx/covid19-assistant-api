from flask import Flask, request, abort
from utils.diagnosis import get_diagnosis
app = Flask(__name__)

@app.route('/diagnosis', methods = ['POST'])
def diagnosis():
    diagnosis = 0
    try:
        values = request.json['values']
        if(len(values) == 11):
            print(values)
            # diagnosis = get_diagnosis(values)
        else: 
            raise Exception("A list of 11 values is expected")

    except NameError:
        return "Property values not found in request", 404
    except TypeError:
        return "Values should be a list", 400
    except Exception:
        return Exception, 400 
    else: 
        return { "diagnosis": diagnosis }, 200


@app.errorhandler(404)
def page_not_found(error):
    return 'Not found', 404

if __name__ == "__main__":
    app.run(port = 3000, debug = True)
