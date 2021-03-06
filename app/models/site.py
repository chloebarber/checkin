from .db import db

class Site(db.Model):
    __tablename__ = 'sites'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    zones = db.relationship("Zone", back_populates="site")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }