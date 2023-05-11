# you may need to install duckdb, flask_sqlalchemy and duckdb_engine


from flask import Flask, render_template, request, redirect, url_for
import uuid
import duckdb
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

conn = duckdb.connect('/flaskdb.db', read_only=False)

app.config['SQLALCHEMY_DATABASE_URI'] = "duckdb:////flaskdb.db"

db = SQLAlchemy(app)

class Task(db.Model):

	__tablename__ = 'tasks'

	uid = db.Column(db.String(50), primary_key=True)
	task = db.Column(db.String(50), nullable=True)

	def __init__(self, uid, task):
		self.uid = uid
		self.task = task

	def __repr__(self):
		return f"{self.id}:{self.task}>"

with app.app_context():
		db.create_all()

@app.route("/")
def index():
#	with app.app_context():
#		db.create_all()
	all_tasks = Task.query.all()
	return render_template("index.html", tasks=all_tasks)


@app.route("/add", methods=["POST"])
def add_task():
	task = request.form.get("task")
	if task:
		new_task = Task(uid=str(uuid.uuid4()), task=task)
		db.session.add(new_task)
		db.session.commit()

	return redirect(url_for("index"))

# Note this won't work without changing Jordan's template
@app.route("/delete/<task_id>", methods=["GET", "POST"])
def delete_task(task_id):
	#global tasks
	#tasks = [task for task in tasks if task["id"] != task_id]
	Task.query.filter_by(uid=task_id).delete()
	db.session.commit()
	return redirect(url_for("index"))


if __name__ == "__main__":
	app.run(debug=True)