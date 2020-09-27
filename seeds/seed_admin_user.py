from flask_seeder import Seeder
from app.models import User


class AdminSeeder(Seeder):
    def run(self):
        print("Seeding database")
        user=User("spravesh1818","secret@","spravesh1818@gmail.com")
        self.db.session.add(user)
        self.db.session.commit()
