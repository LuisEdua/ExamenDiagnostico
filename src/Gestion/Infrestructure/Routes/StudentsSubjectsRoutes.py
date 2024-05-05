from flask import Blueprint, request
from src.Gestion.Infrestructure.Controllers.StudentsSubjects.Create import CreateController
from src.Gestion.Infrestructure.Controllers.StudentsSubjects.Get import GetController
from src.Gestion.Infrestructure.Repositories.MySQLRepositories.StudentsSubjectsRepository import \
    StudentsSubjectsRepository

repo = StudentsSubjectsRepository()
get_controller = GetController(repo)
create_controller = CreateController(repo)

students_subjects_routes = Blueprint('students_subjects_routes', __name__)

@students_subjects_routes.route('/<string:student_uuid>', methods=['GET'])
def get_students_subjects(student_uuid):
    return get_controller.run(student_uuid)

@students_subjects_routes.route('/', methods=['POST'])
def create_students_subjects():
    return create_controller.run(request)
