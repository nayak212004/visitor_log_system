from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'db_password'
app.config['MYSQL_DB'] = 'society_log'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/log', methods=['GET', 'POST'])
def log_visitor():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        flat = request.form['flat']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO visitor_log (name, mobile, flat) VALUES (%s, %s, %s)", (name, mobile, flat))
        mysql.connection.commit()
        cur.close()

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return render_template('success.html', name=name, flat=flat, time=time)
    
    return render_template('log.html')

if __name__ == '__main__':
    app.run(debug=True)



