from flask_seeder import Seeder
from app.models import District,Province,LocalBody
from excel_reader import parse_data

class SeedProvincesField(Seeder):
    def run(self):
        data=parse_data()
        for province in data:
            district_list=[]
            for district in province['info']:
                localbody_list=[]
                for local_level in district['local_level']:
                    if local_level!="Sub Total":
                        local_level=LocalBody(name=local_level)
                        localbody_list.append(local_level)
                        self.db.session.add(local_level)


                district_to_db=District(name=district['district'])
                district_to_db.localbodies=localbody_list
                district_list.append(district_to_db)
                self.db.session.add(district_to_db)

            province_to_db=Province(name=province['province'])
            province_to_db.districts=district_list
            self.db.session.add(province_to_db)
            self.db.session.commit()


