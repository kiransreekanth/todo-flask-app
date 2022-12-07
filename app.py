from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/add', methods=['GET', 'POST'])
def add():
    name = request.form.get('title')
    new_todo = Todo(title=name, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/')
def index():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template("index.html", todo_list=todo_list)


if __name__ == '__main__':
    app.run()
