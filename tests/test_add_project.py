from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    # old_projects = app.project.get_projects_list()
    old_projects = app.soap.get_project_list("administrator", "root")
    app.project.create(Project(name='00012', status='в разработке', view_state='приватный',
                                    description='Project_description', inherit_global=True))
    # new_projects = app.project.get_projects_list()
    new_projects = app.soap.get_project_list("administrator", "root")
    assert len(old_projects) + 1 == len(new_projects)