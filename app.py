from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def handle_request():
    data = request.json
    # Process your data here
    return jsonify({'result': 'your result here'})

if __name__ == '__main__':
    app.run(debug=True)
