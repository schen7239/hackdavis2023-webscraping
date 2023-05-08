from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re

from helper import *

    
if __name__ == "__main__":
    # basic json structure
    teacher_ids = {
        "entries": None,
        "result": []
    }
    # url to the teachers page
    url = f'https://www.ratemyprofessors.com/search/teachers?sid=1073'
    # use selenium to create a webdriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    # get rid of the initial modal
    # close_modal(driver)
    # automatically click the load more btn to get all paginated items
    # load_all_paginated_reviews(driver)
    # store in a html in a beautiful soup object
    bs = BeautifulSoup(driver.page_source, "html.parser")
    teachers = bs.find_all("a", {"class": "TeacherCard__StyledTeacherCard-syjs0d-0"})
    for teacher in teachers:
        rmp_identification = {
            "name": None,
            # "identification": None,
            # "department": None
        }
        try:
            teacher_id = teacher.get('href')
            id_pattern = r'/professor\?tid=(?P<rmp_id>\d+)'
            pattern = re.compile(id_pattern)
            id = pattern.match(teacher_id)
            # rmp_identification["identification"] = id.group('rmp_id')
            rmp_identification["name"] = teacher.find("div", {"class": "CardName__StyledCardName-sc-1gyrgim-0"}).get_text()
            # rmp_identification["department"] = teacher.find("div", {"class": "CardSchool__Department-sc-19lmz2k-0"}).get_text()
            teacher_ids["result"].append(rmp_identification)
        except:
            pass
    driver.quit()
    teacher_ids["entries"] = len(teacher_ids['result'])
    write_to_json_file("teachers.json", teacher_ids)