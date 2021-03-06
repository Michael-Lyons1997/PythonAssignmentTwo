from flask import Flask, request, render_template

app = Flask(__name__)


import DBcm
from appconfig import config

from datetime import date, datetime


@app.route("/")
def index():
    return render_template(
        "homepage.html",
        title="Welcome!",
        heading="This is my homepage, please select the option to use",
    )


@app.route("/showpersonalpage")
def displayPersonal():
    return render_template(
        "personalPage.html", title="Personal Page", heading="This is a page about me",
    )


@app.route("/showCVpage")
def displayCV():
    return render_template("CV.html", title="CV Page", heading="This is my CV",)


@app.route("/showtechnologiespage")
def displayTechnologies():
    return render_template(
        "computingTechnologies.html",
        title="Computing Technology",
        heading="Please fill in this form",
    )


@app.route("/showTechSubpage1")
def displaySub1():
    return render_template(
        "computingTechnologiesSubpageOne.html",
        title="Virtual Reality",
        heading="This is about Virtual Reality",
    )


@app.route("/showTechSubpage2")
def displaySub2():
    return render_template(
        "computingTechnologiesSubpageTwo.html",
        title="Quantum Computing",
        heading="This about Quantum Computing",
    )


@app.route("/showTechSubpage3")
def displaySub3():
    return render_template(
        "computingTechnologiesSubpageThree.html",
        title="Internet of Things",
        heading="This is about the IoT",
    )


@app.route("/showinterestspage")
def displayinterests():
    return render_template(
        "interests.html",
        title="Interests",
        heading="These are my non-computing related interests",
    )


@app.route("/showvisitorspage")
def displayvisitors():
    with DBcm.UseDatabase(config) as db:
        SQL = """
            select email, message, 
            the_date, time_visited 
            from visit order by 
            the_date desc, time_visited desc
        """
        db.execute(SQL)
        data = db.fetchall()
    return render_template(
        "visitorsPage.html",
        title="Visitors",
        heading="These are the most recent visitors",
        theData=data,
    )


@app.route("/processform", methods=["POST"])
def showPersonal():
    theEmail = request.form["email"]
    theMessage = request.form["message"]
    theDate = date.today()
    now = datetime.now()
    theTime = now.strftime("%H:%M:%S")
    with DBcm.UseDatabase(config) as db:
        SQL = """
            insert into visit
            (email, message, the_date, time_visited)
            values
            ( %s, %s, %s, %s )
        """
        db.execute(SQL, (theEmail, theMessage, theDate, theTime,))
    return render_template(
        "homepage.html",
        title="Welcome!",
        heading="This is my homepage, please select the option to use",
    )


if __name__ == "__main__":
    app.run(debug=True)
