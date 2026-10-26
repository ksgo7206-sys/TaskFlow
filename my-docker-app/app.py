from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = [" Docker", " website"]

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task", "").strip()
    if task:
        tasks.append(task)
    return redirect("/")

@app.route("/delete/<int:number>", methods=["POST"])
def delete(number):
    if 0 <= number < len(tasks):
        tasks.pop(number)
    return redirect("/")

app.run(host="0.0.0.0", port=5000)