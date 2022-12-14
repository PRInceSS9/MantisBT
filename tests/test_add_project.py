from model.project import Project


def test_add_project(app):
    # old_projects = app.project.get_projects_list()
    old_projects = app.soap.get_project_list()
    app.project.create(Project(name='00012', status='в разработке', view_state='приватный',
                                    description='Project_description', inherit_global=True))
    # new_projects = app.project.get_projects_list()
    new_projects = app.soap.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
