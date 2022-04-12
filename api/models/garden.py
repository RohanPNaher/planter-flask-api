from datetime import datetime
from api.models.db import db

class Garden(db.Model):
  __tablename__ = 'gardens'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  garden_description = db.Column(db.String)
  garden_type = db.Column('garden_type', db.Enum('Outdoor', 'Indoor', name='garden_type'))
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
  plants = db.relationship('Plant', cascade='all')

  def __repr__(self):
    return f"Garden('{self.id}', '{self.name}'"

  def serialize(self):
    garden = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    plants = [plant.serialize() for plant in self.plants]
    garden['plants'] = plants
    return garden

  # Add method to show that all plants in a garden have been watered?