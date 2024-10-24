from flask import Blueprint
from controllers.patient_controller import PatientController

# Create a Blueprint for the API
api_bp = Blueprint('api', __name__)

# Patient routes
@api_bp.route('/patients', methods=['GET'])
def get_patients():
    return PatientController.get_patients()

@api_bp.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    return PatientController.get_patient(patient_id)

@api_bp.route('/patients', methods=['POST'])
def create_patient():
    return PatientController.create_patient()

@api_bp.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    return PatientController.update_patient(patient_id)

@api_bp.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    return PatientController.delete_patient()
