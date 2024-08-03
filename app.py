from flask import Flask, render_template, request, jsonify
import datetime as dt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    birthdate_str = request.form['birthdate']
    birthdate = dt.datetime.strptime(birthdate_str, '%Y-%m-%d').date()
    hari_ini = dt.date.today()

    umur = hari_ini.year - birthdate.year - ((hari_ini.month, hari_ini.day) < (birthdate.month, birthdate.day))
    ulang_tahun = umur + 1

    tahun_berikutnya = hari_ini.year
    if (hari_ini.month, hari_ini.day) >= (birthdate.month, birthdate.day):
        tahun_berikutnya += 1

    tanggal_ulang_tahun_berikutnya = dt.date(tahun_berikutnya, birthdate.month, birthdate.day)
    sisa_hari = (tanggal_ulang_tahun_berikutnya - hari_ini).days

    result = {
        'umur': umur,
        'ulang_tahun': ulang_tahun,
        'sisa_hari': sisa_hari
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
