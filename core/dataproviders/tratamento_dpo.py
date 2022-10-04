from enum import unique
from app import db
from sqlalchemy.ext.declarative import declarative_base


class TratamentoDpo(db.Model):
    __tablename__ = 'tratamentos'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_equipamento = db.Column(db.Integer, db.ForeignKey('equipamentos.id'))
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id'))
    olho = db.Column(db.String(2))

    #Treatment information - EX500 e FS200
    method = db.Column(db.String(255))
    status = db.Column(db.String(255))
    planned_by = db.Column(db.String(255))
    treated_by = db.Column(db.String(255))
    planning_date = db.Column(db.DateTime)
    treatment_date = db.Column(db.DateTime, unique=True)
    confirmed_by = db.Column(db.String(255))
    device_sn = db.Column(db.String(10))

    #Refractive & Corneal details
    refraction_clinical_id = db.Column(db.Integer, db.ForeignKey('refracoes.id'))
    pupil = db.Column(db.Float)
    pachymetry_superior = db.Column(db.Integer)
    pachymetry_temporal = db.Column(db.Integer)
    pachymetry_central = db.Column(db.Integer)
    pachymetry_nasal = db.Column(db.Integer)
    pachymetry_inferior = db.Column(db.Integer)
    k1 = db.Column(db.Float)
    axis1 = db.Column(db.Integer)
    q1 = db.Column(db.Float)
    k2 = db.Column(db.Float)
    q2 = db.Column(db.Float)
    axis2 = db.Column(db.Integer)

    #Treatment details
    refraction_measured_id = db.Column(db.Integer, db.ForeignKey('refracoes.id'))
    refraction_target_id = db.Column(db.Integer, db.ForeignKey('refracoes.id'))
    refraction_correction_id = db.Column(db.Integer, db.ForeignKey('refracoes.id'))
    target_q = db.Column(db.Float)
    optical_zone = db.Column(db.Float)
    transition_zone = db.Column(db.Float)
    ablation_zone = db.Column(db.Float)
    flap_epi_thickness = db.Column(db.Integer)
    cornea_thickness = db.Column(db.Integer)
    residual_stroma = db.Column(db.Integer)

    #Treatment related information
    cyclorotation = db.Column(db.Float)
    centration_x = db.Column(db.Integer)
    centration_y = db.Column(db.Integer)
    total_duration = db.Column(db.Integer)
    breaks_qt = db.Column(db.Integer)
    breaks_seconds = db.Column(db.Integer)
    pachymetry_records_preop = db.Column(db.Integer)
    pachymetry_records_flap_epi_off = db.Column(db.Integer)
    pachymetry_records_post_op = db.Column(db.Integer)

    maximum_depth= db.Column(db.Float)
    central_depth= db.Column(db.Float)

    #observacao
    memo = db.Column(db.String)

    #FS200
    flap_diameter = db.Column(db.Float)
    flap_thickness = db.Column(db.Integer)
    flap_side_cut_angle = db.Column(db.Integer)
    flap_canal_width = db.Column(db.Integer)
    flap_canal_lenght_offset = db.Column(db.Float)

    hinge_position = db.Column(db.Integer)
    hinge_lenght = db.Column(db.Float)
    hinge_angle = db.Column(db.Integer)
    hinge_width = db.Column(db.Float)

    laser_separations_bed_cut_line_separations = db.Column(db.Float)
    laser_separations_bed_cut_spot_separations = db.Column(db.Float)
    laser_separations_side_cut_line_separations = db.Column(db.Float)
    laser_separations_side_cut_spot_separations = db.Column(db.Float)

    measured_data_pulse_energy_bed_cut = db.Column(db.Float)
    measured_data_pulse_energy_side_cut = db.Column(db.Float)
    measured_data_suction_time = db.Column(db.Float)
    measured_data_device_temperature = db.Column(db.Float)
   
    treatment_data_treatment_progress = db.Column(db.Integer)
    treatment_data_treatment_breaks = db.Column(db.Integer)
    treatment_data_x_offset = db.Column(db.Float)
    treatment_data_y_offset = db.Column(db.Float)

    ## ANEL

    ring_outer_diameter = db.Column(db.Float)
    ring_inner_diameter = db.Column(db.Float)
    ring_depth_in_cornea = db.Column(db.Integer)
    incision_length = db.Column(db.Float)
    incision_width = db.Column(db.Float)
    incision_position = db.Column(db.Integer)

    laser_separations_ring_spot_separations = db.Column(db.Float)
    laser_separations_ring_line_separations = db.Column(db.Float)
    laser_separations_incision_spot_separations = db.Column(db.Float)
    laser_separations_incision_line_separations = db.Column(db.Float)

    measured_data_pulse_energy_ring = db.Column(db.Float)
    measured_data_pulse_energy_incision = db.Column(db.Float)
    flap_offset_torsion = db.Column(db.Integer)
    
    measured_data_pulse_energy_canal = db.Column(db.Float)

    target_data_pulse_energy_ring = db.Column(db.Float)
    target_data_pulse_energy_incision = db.Column(db.Float)
    target_data_pulse_energy_canal = db.Column(db.Float)


    #URL
    pdf_file = db.Column(db.String)