import random
import string

class ProjectHelper:
    def __init__(self, app):
        self.app = app


    def create(self):
        wd = self.app.wd
        self.open_projects_page()
        # init project creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # fill form
        wd.find_element_by_name("name").clear()
        project = self.random_string("project", 20)
        wd.find_element_by_name("name").send_keys(project)
        # submit project creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_projects_page()

    def random_string(self, prefix, maxlen):
            symbols = string.ascii_letters + string.digits + " "
            return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


    def delete_project(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text(name).click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.open_projects_page()


    def get_project(self):
        wd = self.app.wd
        self.open_projects_page()
        table = wd.find_elements_by_xpath("//table")[2]
        project_list = table.find_elements_by_tag_name("tr")
        return project_list


    def get_project_name(self):
        names = self.get_project()
        name = names[2].find_elements_by_tag_name("td")[0].text
        return name


    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()




