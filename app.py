from flask import Flask, render_template, request

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        users.append({'name': name, 'email': email, 'message': message})
        return render_template('result.html', name=name, email=email, message=message)
    return render_template('register.html')

@app.route('/users')
def users_page():
    return render_template('users.html', users=users)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    print("Автор: Шуфлен Назарій")
    app.run(debug=True)

