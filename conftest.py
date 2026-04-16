import pytest

@pytest.fixture
def hospital_url(page):
    page.goto("https://qahackeru3.netlify.app/")

    
    return page

