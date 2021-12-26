from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from io import BytesIO
from PIL import Image
from detect import detect
import base64
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
with open('secret/password') as key:
    app.config['MYSQL_PASSWORD'] = key.read().strip()
app.config['MYSQL_DB'] = 'objdetapp'

mysql = MySQL(app)
cors = CORS(app)


@app.route('/upload', methods=['POST'])
def upload_image():
    # add visit count
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO visits VALUES ()')
    mysql.connection.commit()
    cursor.close()

    # process image
    file = request.files['image']
    orig_image = Image.open(file.stream)
    orig_image = orig_image.convert('RGB')
    new_image = detect(orig_image, min_score=0.2, max_overlap=0.5, top_k=200)
    img_io = BytesIO()
    new_image.save(img_io, 'JPEG')
    image_base64 = base64.b64encode(img_io.getvalue())

    return u'data:image/jpeg;base64,'+image_base64.decode('utf-8')


@app.route('/visits')
def get_visits():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM visits')
    visits = cursor.fetchone()
    return jsonify({'visits': visits[0]})


@app.route('/rating', methods=['POST', 'GET'])
def get_rating():
    if request.method == 'POST':
        score = request.json['score']

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO ratings (score) VALUES (%s)', (str(score)))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'score': score})

    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT AVG(score) FROM ratings')
        score = cursor.fetchone()
        return jsonify({'score': float(score[0])})
