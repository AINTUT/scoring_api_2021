from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Assignment(db.Model):
    __tablename__ = "assignments"

    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(), nullable=False)
    ordinal = db.Column(db.Integer, nullable=False)
    correctnesses = db.Column(db.String(), nullable=False)


class Midterm(db.Model):
    __tablename__ = "midterms"

    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(), nullable=False)
    ordinal = db.Column(db.Integer, nullable=False)
    answers = db.Column(db.String(), nullable=False)
    correctnesses = db.Column(db.String(), nullable=False)


class MidtermMember(db.Model):
    __tablename__ = "midterm_members"

    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(), nullable=False)
    credential = db.Column(db.String(), nullable=False)
