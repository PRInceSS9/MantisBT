from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_add_project_page(self):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-2.25.4/manage_proj_create_page.php')

    def open_project_page(self):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-2.25.4/manage_proj_page.php')


    def fill_add_form(self, project):
        wd = self.app.wd
        self.change_field_text_value("name", project.name)
        self.change_field_select_value("status", project.status)
        if not project.inherit_global:
            wd.find_element_by_name("inherit_global").click()
        self.change_field_select_value("view_state", project.view_state)
        self.change_field_text_value("description", project.description)

    def change_field_select_value(self, field_name, var):
        wd = self.app.wd
        if var is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(var)

    def change_field_text_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, project):
        wd = self.app.wd
        self.open_add_project_page()
        self.fill_add_form(project)
        wd.find_element_by_xpath("//input[@class='btn btn-primary btn-white btn-round']").click()

    def get_projects_list(self):
        wd = self.app.wd
        self.open_project_page()
        table = wd.find_elements_by_tag_name("table")[0]
        body = table.find_element_by_tag_name("tbody")
        row = body.find_elements_by_tag_name("tr")
        project_list = []
        for element in row:
            name = element.find_elements_by_tag_name("td")[0].text
            status = element.find_elements_by_tag_name("td")[1].text
            view_state = element.find_elements_by_tag_name("td")[3].text
            description = element.find_elements_by_tag_name("td")[4].text
            project_list.append(Project(name=name, status=status, view_state=view_state, description=description))
        return project_list

    def delete_project(self, project):
        wd = self.app.wd
        wd.find_element("link text", project.name).click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()


