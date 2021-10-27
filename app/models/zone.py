from .db import db

class Zone(db.Model):
    __tablename__ = 'zones'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    site_id = db.Column(db.Integer, db.ForeignKey("sites.id"), nullable=False)

    site = db.relationship("Site", back_populates="zones")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'site_id': self.site_id,
        }