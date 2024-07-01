# from flask import Flask, render_template
# from datetime import datetime
#
# app = Flask(__name__)
#
# @app.route('/')
# def main():
#     now = datetime.now() # Получаем текущее время
#     current_time = now.strftime("%H:%M:%S") # Форматируем время
#     return render_template('index.html', current_time=current_time)
#     #return render_template('index.html')
#
# @app.route('/aboutus/')
# def aboutus():
#     return render_template('aboutus.html')
#
# @app.route('/contacts/')
# def contacts():
#     return render_template('contacts.html')
#
#
# @app.route('/blog/')
# def blog():
#     return render_template('blog.html')
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     app.run()
#


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)