class SampleController:
    def __init__(self, sample_dao):
        self.sample_dao = sample_dao

    def create_sample(self, patient_name):
        sample_id = self.sample_dao.add_sample(patient_name)
        return sample_id

    def get_all_samples(self):
        return self.sample_dao.get_all_samples()

    def get_sample(self, sample_id):
        return self.sample_dao.get_by_id(sample_id)

    def update_status(self, sample_id, status):
        success = self.sample_dao.update_status(sample_id, status)
        return success

    def search_patient(self, name):
        return self.sample_dao.search_by_patient(name)

    def delete_sample(self, sample_id):
        return self.sample_dao.delete_sample(sample_id)