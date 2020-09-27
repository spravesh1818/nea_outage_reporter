from flask_seeder import Seeder
from app.models import User


class AdminSeeder(Seeder):
    def run(self):
        user=User("NEAadmin","secret@","nea@nea.com")
        self.db.session.add(user)
        self.db.session.commit()
