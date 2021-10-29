from app.models import db, Zone


def seed_zones():
    seedArray = []

    seedArray.append(Zone(name="East Wing", site_id=1))
    seedArray.append(Zone(name="North Wing", site_id=1))
    seedArray.append(Zone(name="South Wing", site_id=1))
    seedArray.append(Zone(name="West Wing", site_id=1))





    for item in seedArray:
        db.session.add(item)

    db.session.commit()