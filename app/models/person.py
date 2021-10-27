from .db import db

class Person(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    zone_id = db.Column(db.Integer, db.ForeignKey("zones.id"), nullable=False)

    zone = db.relationship("Site", back_populates="people")

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'zone_id': self.zone_id,
        }