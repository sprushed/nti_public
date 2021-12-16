import os
from flask import Flask, request, jsonify
from Crypto.Util.number import long_to_bytes as l2b

p = 4448969339709658119179471114552306735281280715433700946537751326892671370479981086570264860309709374064610452775364704769491886019025297462118854820567577380305344793475944962067098115169814970386897388031412241543528697225380492092387463389834623325921506754370752015400820839404177216655896503541578602116341
a = int(os.urandom(128).hex(), base=16)
g = 2
A = pow(g, a, p)
pub = {"p": p, "A": A, "g": g}

app = Flask(__name__)


@app.route('/get_key', methods=['GET'])
def get_key():
    return jsonify(pub)


@app.route("/send_flag", methods=['POST'])
def send_flag():
    content = request.json
    if "c1" not in content.keys() or "c2" not in content.keys():
        return jsonify({"status": "error, malformed input"})

    c1 = content["c1"]
    c2 = content["c2"]

    x = pow(pow(c1, a, p), -1, p)
    print("Decrypted data:", l2b(x*c2%p))

    return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run('0.0.0.0', 8887)
