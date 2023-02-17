from sqlalchemy import update

from . import Session
from .model import User


def get(user_id):
    with Session() as sess:
        user = sess.get(User, user_id)
    return user


def all():
    with Session() as sess:
        users = sess.query(User).all()
    return users


def add(newUser):
    with Session.begin() as sess:
        sess.add(newUser)


def addAll(users=None):
    if users is None:
        users = []
    with Session.begin() as sess:
        sess.add_all(users)


def update(user_name, data):
    with Session() as sess:
        stmt = (
            update(User)
                .where(User.name == user_name)
                .values(password=data)
                .execution_options(synchronize_session="fetch")
        )

        sess.execute(stmt)


def delete(user):
    with Session.begin() as sess:
        sess.delete(user)

# end of file.