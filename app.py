from flask import Flask, jsonify, request
import platform
import socket

app = Flask(__name__)

@app.route('/api/quote', methods=['GET'])
def get_quote():
    hostname = socket.gethostname()
    ip = request.remote_addr

    data = {
        "hardwareArchitecture": platform.machine(),
        "operatingSystem": platform.system(),
        "ipAddress": f"{hostname}/{ip}",
        "quote": "In Python, simplicity is powerful."
    }

    return jsonify(data)

if __name__ == '__main__':
    print("Starting Python version of quote-service on port 8080")
    app.run(host='0.0.0.0', port=8080)