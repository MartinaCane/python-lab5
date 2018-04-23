from flask import Flask, render_template
import Database

app = Flask(__name__)


@app.route('/')
def index():
    task_list = Database.read_from_db()
    print(task_list)

    return render_template('index.html', tasks=task_list)

@app.route('/insert_page', methods=["POST"])
def insertTask():



if __name__ == '__main__':
    app.run()
