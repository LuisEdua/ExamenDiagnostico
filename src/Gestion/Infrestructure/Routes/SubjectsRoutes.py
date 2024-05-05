from flask import Blueprint, request
from src.Gestion.Infrestructure.Controllers.Subjects.Create import CreateController
from src.Gestion.Infrestructure.Controllers.Subjects.Get import GetController
from src.Gestion.Infrestructure.Repositories.MySQLRepositories.SubjectsRepository import SubjectsRepository

repo = SubjectsRepository()
create_controller = CreateController(repo)
get_controller = GetController(repo)

subjects_routes = Blueprint('subjects_routes', __name__)

@subjects_routes.route('/', methods=['GET'])
def get_subjects():
    return get_controller.run()

@subjects_routes.route('/', methods=['POST'])
def create_subject():
    return create_controller.run(request)
