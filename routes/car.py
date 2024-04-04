from app import app
from models import Session, Car
from flask import render_template
from sqlalchemy import select


@app.get("/cars_list")
def cars_list():
    # get cars from db
    context = dict()
    with Session.begin() as session:
        context["items"] = session.scalars(select(Car)).all()
        return render_template("list.html", **context)
