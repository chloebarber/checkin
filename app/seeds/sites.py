from app.models import db, Site


def seed_sites():
    seedArray = []

    seedArray.append(Site(name="MPATH Building Boston"))




    for item in seedArray:
        db.session.add(item)

    db.session.commit()