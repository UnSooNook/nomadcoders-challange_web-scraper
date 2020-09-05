from flask import Flask, render_template, request, redirect, send_file

from scrapper import getJobs
from exporter import saveToFile

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
db = {}

app = Flask("DayThirteen")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result")
def result():
    term = request.args.get("term")
    if term:
        term = term.lower()
        existingJobs = db.get(term)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = getJobs(term)
            db[term] = jobs
    else:
        return redirect("/")

    return render_template("result.html", term=term, jobCnt=len(jobs), jobs=jobs)


@app.route("/export")
def export():
    try:
        term = request.args.get("term")
        if not term:
            raise Exception()
        term = term.lower()
        jobs = db.get(term)
        if not jobs:
            raise Exception()
        saveToFile(term, jobs)

        return send_file(f"{term}-jobs.csv", mimetype="text/csv", as_attachment=True, attachment_filename=f"{term}-jobs.csv")
    except:
        return redirect("/")


app.run(host="0.0.0.0")