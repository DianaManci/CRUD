from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import bcrypt
import re
import os
import sys

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto a una clave secreta más segura

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Carpeta para subir fotos de perfil

# Inicializar MySQL
mysql = MySQL(app)

#ruta login 
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            sql = 'SELECT * FROM usuarios WHERE nombre = %s'
            cursor.execute(sql, (username,))
            account = cursor.fetchone()

            if account:
                hash_almacenado = account['clave'].encode('utf-8')
                if bcrypt.checkpw(password.encode('utf-8'), hash_almacenado):
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['nombre']
                    flash('Logged in successfully!', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Incorrect username/password!', 'error')
            else:
                flash('Incorrect username/password!', 'error')
        except Exception as e:
            flash(f'Error connecting to the database: {e}', 'error')
    
    return render_template('login.html')


#ruta home
@app.route('/home')
def home():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuarios WHERE id = %s', (session['id'],))
        account = cursor.fetchone()

        # Si la cuenta existe y tiene foto, configurar la URL de la foto
        foto_url = url_for('static', filename='uploads/' + account['foto']) if account['foto'] else url_for('static', filename='default.png')

        return render_template('home.html', account=account, foto_url=foto_url)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'foto' in request.files:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')  # Corregido para coincidir con el formulario
        foto = request.files.get('foto')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuarios WHERE nombre = %s', (username,))
        account = cursor.fetchone()
            
        if account:
            flash('ESTA CUENTA YA EXISTE', 'error')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('EMAIL INCORRECTO!', 'error')
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('CARACTERES INVALIDOS', 'error')
        else:
            try:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                foto_filename = os.path.join(app.config['UPLOAD_FOLDER'], foto.filename)
                foto.save(foto_filename)
                cursor.execute('INSERT INTO usuarios (nombre, clave, correo, foto) VALUES (%s, %s, %s, %s)', (username, hashed_password.decode('utf-8'), email, foto_filename))
                mysql.connection.commit()
                flash('SE HA REGISTRADO CORRECTAMENTE', 'success')
                return redirect(url_for('login'))
            except Exception as e:
                flash(f'Error al registrar la cuenta: {e}', 'error')
    else:
        flash('DIGITE INFORMACION EN EL CAMPO REQUERIDO', 'error')
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
