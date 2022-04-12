from datetime import datetime
from email.policy import default
from unicodedata import name

from sqlalchemy import false
from api.models.db import db 

class Plant(db.Model):
  __tablename__ = 'plants'
  id = db.Column(db.Integer, primary_key=True)
  plant_name = db.Column(db.String)
  plant_description = db.Column(db.String)
  is_watered = db.Column(db.Boolean, default=False, nullable=False)
  water_schedule = db.Column('water schedule', db.Enum('Daily', 'Every Other Day', 'Every Three Days', 'Weekly', 'Top-Up Whenever', name='water_schedule_type'))
  created_at = db.Column(db.DateTime, default=datetime.now(tz=None))
  garden_id = db.Column(db.Integer, db.ForeignKey('gardens.id'))

  def __repr__(self):
    return f"Plant('{self.id}', '{self.plant_name}'"

  def serialize(self):
      plant = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return plant