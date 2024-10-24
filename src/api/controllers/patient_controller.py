from flask import request, jsonify
from models.patient import Patient
from serializers.patient_serializer import PatientSchema

class PatientController:
    @staticmethod
    def get_patients():
        patients = Patient.query.all()  # Fetch all patients from the database
        patient_schema = PatientSchema(many=True)
        return jsonify(patient_schema.dump(patients)), 200

    @staticmethod
    def get_patient(patient_id):
        patient = Patient.query.get(patient_id)
        if patient:
            patient_schema = PatientSchema()
            return jsonify(patient_schema.dump(patient)), 200
        return jsonify({"error": "Patient not found"}), 404

    @staticmethod
    def create_patient():
        patient_schema = PatientSchema()
        patient_data = patient_schema.load(request.json)  # Validate and deserialize input
        new_patient = Patient(**patient_data)
        new_patient.save()  # Save to the database
        return jsonify(patient_schema.dump(new_patient)), 201

    @staticmethod
    def update_patient(patient_id):
        patient = Patient.query.get(patient_id)
        if not patient:
            return jsonify({"error": "Patient not found"}), 404
        
        patient_schema = PatientSchema()
        patient_data = patient_schema.load(request.json)  # Validate and deserialize input
        patient.update(**patient_data)  # Update patient data
        return jsonify(patient_schema.dump(patient)), 200

    @staticmethod
    def delete_patient(patient_id):
        patient = Patient.query.get(patient_id)
        if not patient:
            return jsonify({"error": "Patient not found"}), 404
        
        patient.delete()  # Delete from the database
        return jsonify({"message": "Patient deleted successfully"}), 204
