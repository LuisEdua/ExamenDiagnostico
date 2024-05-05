from flask import request, Blueprint

from src.Gestion.Infrestructure.Controllers.Tutors.Create import CreateController
from src.Gestion.Infrestructure.Controllers.Tutors.Get import GetController
from src.Gestion.Infrestructure.Repositories.MySQLRepositories.TutorsRepository import TutorsRepository

tutors_routes = Blueprint('tutors_routes', __name__)

repo = TutorsRepository()
get_controller = GetController(repo)
create_controller = CreateController(repo)

@tutors_routes.route('/', methods=['GET'])
def get_all():
    return get_controller.run()

@tutors_routes.route('/', methods=['POST'])
def create_tutor():
    return create_controller.run(request)
