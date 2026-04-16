
class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.patients_tab = page.locator("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[1]")
        self.laboratory_tab = page.locator("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[2]")
        self.pharmacy_tab = page.locator ("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[3]")


    def click_all_tabs (self):
        self.laboratory_tab.click()
        self.pharmacy_tab.click()
        self.patients_tab.click()
    
    def add_patient(self):
      self.page.locator("#addPatientBtn").click()

    