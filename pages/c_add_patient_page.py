
class AddPatientPage:
    def __init__(self, page):
        self.page = page

    def fill_patient_details(self, patient_id, patient_name, category, status, assigned_doctor, Ward): 
        self.patient_id = self.page.locator("#patientId").fill(patient_id)
        self.name = self.page.locator("#patientName").fill(patient_name)
        self.category_dropdown = self.page.locator("#patientCategory").select_option(category)
        self.patient_status_dropdown.page.locator("#patientStatus").select_option(status)
        self.assigned_doctor.page.locator("#patientDoctor").fill(assigned_doctor)
        self.ward.page.locator("#patientWard").fill(Ward)
        self.admit_patient_btn.page.locator("#submitPatientBtn").click()
        
        
    def search_patient(self, patient_id):
        self.search_patient_input ("#searchInput").fill(patient_id)
        