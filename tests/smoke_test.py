from pages.a_login_page import LoginPage
from pages.b_dashboard_page import DashboardPage
from pages.c_add_patient_page import AddPatientPage
from playwright.sync_api import expect
import time

def test_smoke(hospital_url):
     login_page_obj = LoginPage(hospital_url)
     dashboard_page_obj = DashboardPage(hospital_url)
     add_patient_page_obj = AddPatientPage(hospital_url) 

     login_page_obj.login("nurse_admin", "clinical2026")
     dashboard_page_obj.click_all_tabs()
     dashboard_page_obj.add_patient()
     add_patient_page_obj.fill_patient_details("12345", "QA test", "ICU", "Stable", "Dr. test", "Ward A")
     add_patient_page_obj.search_patient("QA test")
     


def test_visual_url():
     expect(LoginPage).to_have_url("https://qahackeru3.netlify.app/")

def test_logout_btn(page):
    expect(page.locator(".btn-logout")).to_be_visible()

def patient_text(page):
     expect(page.locator("//*[@id='dataContainer']")).to_contain_text()


time.sleep(5)