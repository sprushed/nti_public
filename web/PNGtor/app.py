from flask import Flask
from flask import render_template, abort, flash, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
import os
import uuid
import io
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg
from PIL import Image
import base64

app = Flask(__name__)
app.config['TMP_FOLDER'] = "/tmp"
app.config['MAX_FILE_SIZE'] = 1024*1024*16 # 16 mb


def convertSVG(path):
    try:
        with io.BytesIO() as output:
            drawing = svg2rlg(path)
            image = renderPM.drawToPIL(drawing)
            image.save(output, format="PNG")
            return base64.b64encode(output.getvalue()).decode()
    except Exception as e:
        return (-1, e)

def convertAny(path):
    try:
        with io.BytesIO() as output:
            image = Image.open(path)
            image.save(output, format="PNG")
            return base64.b64encode(output.getvalue()).decode()
    except Exception as e:
        return (-1, e)

def convertToPNG(path):
    ext = path.split(".")[-1].lower()
    if ext == "svg":
        return convertSVG(path)

    if ext == "bmp" or ext == "jpeg" or ext == "jpg" or ext == "jpeg" or ext == "gif":
        return convertAny(path)

    return (-1, "unknown file type. Currently supported: png, jpg, jpeg, bmp, svg, gif")

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/logo.png')
def send_logo():
    return send_file('logo.png')

@app.route("/", methods=["GET", "POST"])
def upload():
    errors = []
    if request.method == "POST" and not 'file' in request.files or request.method == "POST" and request.files['file'].filename == '':
        errors.append("Error: file not provided")

    if request.method == "POST" and len(errors) == 0:
        file = request.files['file']
        ext = secure_filename(file.filename).split(".")[-1]
        name = str(uuid.uuid4()) + "." + ext
        tmp_path = os.path.join(app.config['TMP_FOLDER'], name)

        # check file size
        file.save(tmp_path)
        size = os.stat(tmp_path).st_size
        if size > app.config['MAX_FILE_SIZE']:
            os.remove(tmp_path)
            errors.append("Error: file too large")
            return render_template("file_upload.html", errors=errors)

        pngImage = convertToPNG(tmp_path)
        os.remove(tmp_path)
        if pngImage[0] == -1:
            errors.append(pngImage[1])
            return render_template("file_upload.html", errors=errors)
        else:
            return render_template("file_upload.html", png=pngImage)

    return render_template("file_upload.html", errors=errors)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
