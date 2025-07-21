from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        return f"Hello, {username}!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
