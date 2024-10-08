from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_socketio import SocketIO, emit

port = 5000;
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
image_directory = 'C:/Your/Absolute/Directory/Here'

data = {
    "match":{
        "p1Score":0,
        "p2Score":0,
        "firstTo":2

    },
    "players":[
        {
            "username":"",
            "pfp":"/static/placeholder.png",
            "rank":"",
            "country":"",
            "flag_img":"/static/placeholder.png",
            "since":"",
            "stats":[
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0,0,0],
                [0,0,0]
            ],
            "rival":""
        },
        {
            "username":"",
            "pfp":"/static/placeholder.png",
            "rank":"",
            "country":"",
            "flag_img":"/static/placeholder.png",
            "since":"",
            "stats":[
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0,0,0],
                [0,0,0]
            ],
            "rival":""
        }
    ]
}
@app.route('/update_data', methods=['POST'])
def updateData():
    data = request.json
    socketio.emit('playerUpdate', data)
    return jsonify({"message": "Data updated successfully"})

@app.route('/update_scores', methods =['POST'])
def resetScores():
    data = request.json
    socketio.emit("updateScores", data)
    return jsonify({"message": "Reset scores"})

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hide', methods = ['POST'])
def hide():
    socketio.emit("hide")
    return jsonify({"message":"Hidden items"})

@app.route('/show', methods = ['POST'])
def show():
    socketio.emit("show")
    return jsonify({"message":"Showed items"})

@app.route('/clear', methods = ['POST'])
def clear():
    socketio.emit("clear")
    return jsonify({"message":"Cleared Screen"})

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(image_directory, filename)

if __name__ == '__main__':
    socketio.run(app, port=port, allow_unsafe_werkzeug=True)
