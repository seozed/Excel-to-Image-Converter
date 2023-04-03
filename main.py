from flask import Flask, request, send_file
from excel2img import export_img
import tempfile

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(request.files['file'].read())
        img = export_img(temp_file.name, 'output.png')
    return send_file('output.png', mimetype='image/png', as_attachment=True)

if __name__ == '__main__':
    app.run()
