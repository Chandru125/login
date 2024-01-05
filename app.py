from flask import Flask,render_template,url_for,request,redirect,flash
import sqlite3
app=Flask(__name__)
app.secret_key="123"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        try:
            name=request.form['name']
            password=request.form['password']
            email=request.form['email']
            con=sqlite3.connect("data.db")
                
            con.execute("create table if not exists stud (pid integer primary key,Name text,password text,email text )")
            cur=con.cursor()
            cur.execute(''' insert into stud (Name,password,email)values(?,?,?)''',
                            (name,password,email))
            con.commit()
            flash("Data inserted successfully","success")

        except:
            flash("Data Not inserted ","danger")

        finally:
            return redirect(url_for('home'))
            con.close()
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)