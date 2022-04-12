from datetime import datetime
from api.models.db import db

class Garden(db.Model):
  __tablename__ = 'gardens'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  gardenDescription = db.Column(db.String)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

  def __repr__(self):
    return f"Garden('{self.id}', '{self.name}'"

  def serialize(self):
      garden = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return garden