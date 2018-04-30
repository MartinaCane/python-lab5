from flask import Flask, render_template, request
import Database

app = Flask(__name__)


@app.route('/')
def index():
    task_list = Database.read_from_db()
    print(task_list)

    return render_template('index.html', tasks=task_list)


@app.route('/insert_page', methods=["POST"])
def insertTask():
    new=request.form['new_task']
    Database.insert_new_task(new)
    return render_template("index.html", tasks=Database.read_from_db())


if __name__ == '__main__':
    app.run()
