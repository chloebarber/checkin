from .db import db

class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    person_logged = db.Column(db.Integer, db.ForeignKey("people.id"), nullable=False)
    timestamp = db.Column(db.Integer)

    person = db.relationship("Person", back_populates="logs")

    def to_dict(self):
        return {
            'id': self.id,
            'person_logged': self.name,
            'timestamp': self.timestamp,
        }