from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/api/v1/bmi', methods=['POST'])
def bmi():
    height = float (request.form.get('height'))
    weight = float (request.form.get('weight'))
    BMI = weight / (height/100)**2
    msg = "BMI Kamu adalah " + str(BMI)
    if BMI <= 18.4:
        ket = "Kamu Kurus."
    elif BMI <= 25:
        ket = "Kamu Normal."
    elif BMI <= 40:
        ket = "Kamu Berlebih."
    else:
        ket = "Kamu Dangerous."
    data = {'result': 'true', 'msg': msg, 'ket': ket}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=False, port=4000) 