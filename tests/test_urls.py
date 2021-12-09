from flask import request


def test_homepage(client):
    """ Test to see of the server is up. """
    assert client.get("/").status_code == 200

def test_personal_page(client):
    """ Test to see of the server is up. """
    assert client.get("/showpersonalpage").status_code == 200

def test_CV_page(client):
    """ Test to see of the server is up. """
    assert client.get("/showCVpage").status_code == 200

def test_tech_page(client):
    """ Test to see of the server is up. """
    assert client.get("/showtechnologiespage").status_code == 200

def test_interests_page(client):
    """ Test to see of the server is up. """
    assert client.get("/showinterestspage").status_code == 200


def test_correct_form(client):
    """ Grab the home page, check for 200 code (all ok), then check to
        see if we have received the correct form and that the response is
        a HTML page.
    """
    response = client.get("/processform")
    assert response.status_code == 200
    # response.data is a binary text version of the HTML page.
    assert (
        bytes('<form action="/processform" method="post">', encoding="utf-8")
        in response.data
    )
    assert response.data.startswith(bytes("<!DOCTYPE html>", encoding="utf-8"))


def test_form_operation(client, clean_up_db):
    """ Create some test/sample data, then POST the data to the server.  Ensure
        the request is using POST, then look for a 200 (all ok) status code.  Get the 
        response, check for a valid HTML page, then check that the submitted form data
        was received then send back to the browser in the response.
    """
    form_data = {
        "email": "test@test.ie",
        "message": "this is a test",
        "the_date": "1997/12/12",
        "time_visited": "00:00:00",
    }
    response = client.post("/processform", data=form_data)
    assert request.method == "POST"
    assert response.status_code == 200
    resp = response.data  # The binary text version of the HTML response.
    assert resp.startswith(bytes("<!DOCTYPE html>", encoding="utf-8"))
    assert bytes(form_data["the_date"], encoding="utf-8") in resp
    assert bytes(form_data["time_visited"], encoding="utf-8") in resp
