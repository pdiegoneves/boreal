from app import db
from core.dataproviders.tratamento_dpo import TratamentoDpo

class Tratament():
    def __init__(self, id_equipamento, id_paciente, olho, method, status, planned_by, treated_by, planning_date, treatment_date, confirmed_by, device_sn,
          refraction_clinical_id, pupil, pachymetry_superior, pachymetry_temporal, pachymetry_central, pachymetry_nasal, pachymetry_inferior, k1, axis1, 
          q1, k2, q2, axis2, refraction_measured_id, refraction_target_id, refraction_correction_id, target_q, optical_zone, transition_zone, ablation_zone,
          flap_epi_thickness, cornea_thickness, residual_stroma, cyclorotation, centration_x, centration_y, total_duration, breaks_qt, breaks_seconds, 
          pachymetry_records_preop, pachymetry_records_flap_epi_off, pachymetry_records_post_op, maximum_depth, central_depth, memo, flap_diameter, flap_thickness, 
          flap_side_cut_angle, flap_canal_width, flap_canal_lenght_offset, hinge_position, hinge_lenght, hinge_angle, hinge_width, 
          laser_separations_bed_cut_line_separations, laser_separations_bed_cut_spot_separations, laser_separations_side_cut_line_separations, 
          laser_separations_side_cut_spot_separations, measured_data_pulse_energy_bed_cut, measured_data_pulse_energy_side_cut, measured_data_suction_time, 
          measured_data_device_temperature, treatment_data_treatment_progress, treatment_data_treatment_breaks, treatment_data_x_offset, treatment_data_y_offset, 
          ring_outer_diameter, ring_inner_diameter, ring_depth_in_cornea, incision_length, incision_width, incision_position, laser_separations_ring_spot_separations, 
          laser_separations_ring_line_separations, laser_separations_incision_spot_separations, laser_separations_incision_line_separations, 
          measured_data_pulse_energy_ring, measured_data_pulse_energy_incision, flap_offset_torsion, measured_data_pulse_energy_canal, target_data_pulse_energy_ring, 
          target_data_pulse_energy_incision, target_data_pulse_energy_canal, pdf_file):
       
        self.__id = 0
        self.__id_equipamento = id_equipamento
        self.__id_paciente = id_paciente
        self.__olho = olho
        self.__method = method
        self.__status = status
        self.__planned_by = planned_by
        self.__treated_by = treated_by
        self.__planning_date = planning_date
        self.__treatment_date = treatment_date
        self.__confirmed_by = confirmed_by
        self.__device_sn = device_sn
        self.__refraction_clinical_id = refraction_clinical_id
        self.__pupil = pupil
        self.__pachymetry_superior = pachymetry_superior
        self.__pachymetry_temporal = pachymetry_temporal
        self.__pachymetry_central = pachymetry_central
        self.__pachymetry_nasal = pachymetry_nasal
        self.__pachymetry_inferior = pachymetry_inferior
        self.__k1 = k1
        self.__axis1 = axis1
        self.__q1 = q1
        self.__k2 = k2
        self.__q2 = q2
        self.__axis2 = axis2
        self.__refraction_measured_id = refraction_measured_id
        self.__refraction_target_id = refraction_target_id
        self.__refraction_correction_id = refraction_correction_id
        self.__target_q = target_q
        self.__optical_zone = optical_zone
        self.__transition_zone = transition_zone
        self.__ablation_zone = ablation_zone
        self.__flap_epi_thickness = flap_epi_thickness
        self.__cornea_thickness = cornea_thickness
        self.__residual_stroma = residual_stroma
        self.__cyclorotation = cyclorotation
        self.__centration_x = centration_x
        self.__centration_y = centration_y
        self.__total_duration = total_duration
        self.__breaks_qt = breaks_qt
        self.__breaks_seconds = breaks_seconds
        self.__pachymetry_records_preop = pachymetry_records_preop
        self.__pachymetry_records_flap_epi_off = pachymetry_records_flap_epi_off
        self.__pachymetry_records_post_op = pachymetry_records_post_op
        self.__maximum_depth = maximum_depth
        self.__central_depth = central_depth
        self.__memo = memo
        self.__flap_diameter = flap_diameter
        self.__flap_thickness = flap_thickness
        self.__flap_side_cut_angle = flap_side_cut_angle
        self.__flap_canal_width = flap_canal_width
        self.__flap_canal_lenght_offset = flap_canal_lenght_offset
        self.__hinge_position = hinge_position
        self.__hinge_lenght = hinge_lenght
        self.__hinge_angle = hinge_angle
        self.__hinge_width = hinge_width
        self.__laser_separations_bed_cut_line_separations = laser_separations_bed_cut_line_separations
        self.__laser_separations_bed_cut_spot_separations = laser_separations_bed_cut_spot_separations
        self.__laser_separations_side_cut_line_separations = laser_separations_side_cut_line_separations
        self.__laser_separations_side_cut_spot_separations = laser_separations_side_cut_spot_separations
        self.__measured_data_pulse_energy_bed_cut = measured_data_pulse_energy_bed_cut
        self.__measured_data_pulse_energy_side_cut = measured_data_pulse_energy_side_cut
        self.__measured_data_suction_time = measured_data_suction_time
        self.__measured_data_device_temperature = measured_data_device_temperature
        self.__treatment_data_treatment_progress = treatment_data_treatment_progress
        self.__treatment_data_treatment_breaks = treatment_data_treatment_breaks
        self.__treatment_data_x_offset = treatment_data_x_offset
        self.__treatment_data_y_offset = treatment_data_y_offset
        self.__ring_outer_diameter = ring_outer_diameter
        self.__ring_inner_diameter = ring_inner_diameter
        self.__ring_depth_in_cornea = ring_depth_in_cornea
        self.__incision_length = incision_length
        self.__incision_width = incision_width
        self.__incision_position = incision_position
        self.__laser_separations_ring_spot_separations = laser_separations_ring_spot_separations
        self.__laser_separations_ring_line_separations = laser_separations_ring_line_separations
        self.__laser_separations_incision_spot_separations = laser_separations_incision_spot_separations
        self.__laser_separations_incision_line_separations = laser_separations_incision_line_separations
        self.__measured_data_pulse_energy_ring = measured_data_pulse_energy_ring
        self.__measured_data_pulse_energy_incision = measured_data_pulse_energy_incision
        self.__flap_offset_torsion = flap_offset_torsion
        self.__measured_data_pulse_energy_canal = measured_data_pulse_energy_canal
        self.__target_data_pulse_energy_ring = target_data_pulse_energy_ring
        self.__target_data_pulse_energy_incision = target_data_pulse_energy_incision
        self.__target_data_pulse_energy_canal = target_data_pulse_energy_canal
        self.__pdf_file = pdf_file

        @property
        def id(self):
            return self.__id
        
        @id.setter
        def id(self, value):
            self.__id = value

        @property
        def id_equipamento(self):
            return self.__id_equipamento
        
        @id_equipamento.setter
        def id_equipamento(self, value):
            self.__id_equipamento = value

        @property
        def id_paciente(self):
            return self.__id_paciente
        
        @id_paciente.setter
        def id_paciente(self, value):
            self.__id_paciente = value

        @property
        def olho(self):
            return self.__olho
        
        @olho.setter
        def olho(self, value):
            self.__olho = value

        @property
        def method(self):
            return self.__method
        
        @method.setter
        def method(self, value):
            self.__method = value

        @property
        def status(self):
            return self.__status
        
        @status.setter
        def status(self, value):
            self.__status = value

        @property
        def planned_by(self):
            return self.__planned_by
        
        @planned_by.setter
        def planned_by(self, value):
            self.__planned_by = value

        @property
        def treated_by(self):
            return self.__treated_by
        
        @treated_by.setter
        def treated_by(self, value):
            self.__treated_by = value

        @property
        def planning_date(self):
            return self.__planning_date
        
        @planning_date.setter
        def planning_date(self, value):
            self.__planned_date = value

        @property
        def treatment_date(self):
            return self.__treatment_date
        
        @treatment_date.setter
        def treatment_date(self, value):
            self.__treatment_date = value

        @property
        def confirmed_by(self):
            return self.__confirmed_by
        
        @confirmed_by.setter
        def confirmed_by(self, value):
            self.__confirmed_by = value

            
            # device_sn
            # refraction_clinical_id
            # pupil
            # pachymetry_superior
            # pachymetry_temporal
            # pachymetry_central
            # pachymetry_nasal
            # pachymetry_inferior
            # k1
            # axis1
            # q1
            # k2
            # q2
            # axis2
            # refraction_measured_id
            # refraction_target_id
            # refraction_correction_id
            # target_q
            # optical_zone
            # transition_zone
            # ablation_zone
            # flap_epi_thickness
            # cornea_thickness
            # residual_stroma
            # cyclorotation
            # centration_x
            # centration_y
            # total_duration
            # breaks_qt
            # breaks_seconds
            # pachymetry_records_preop
            # pachymetry_records_flap_epi_off
            # pachymetry_records_post_op
            # maximum_depth
            # central_depth
            # memo
            # flap_diameter
            # flap_thickness
            # flap_side_cut_angle
            # flap_canal_width
            # flap_canal_lenght_offset
            # hinge_position
            # hinge_lenght
            # hinge_angle
            # hinge_width
            # laser_separations_bed_cut_line_separations
            # laser_separations_bed_cut_spot_separations
            # laser_separations_side_cut_line_separations
            # laser_separations_side_cut_spot_separations
            # measured_data_pulse_energy_bed_cut
            # measured_data_pulse_energy_side_cut
            # measured_data_suction_time
            # measured_data_device_temperature
            # treatment_data_treatment_progress
            # treatment_data_treatment_breaks
            # treatment_data_x_offset
            # treatment_data_y_offset
            # ring_outer_diameter
            # ring_inner_diameter
            # ring_depth_in_cornea
            # incision_length
            # incision_width
            # incision_position
            # laser_separations_ring_spot_separations
            # laser_separations_ring_line_separations
            # laser_separations_incision_spot_separations
            # laser_separations_incision_line_separations
            # measured_data_pulse_energy_ring
            # measured_data_pulse_energy_incision
            # flap_offset_torsion
            # measured_data_pulse_energy_canal
            # target_data_pulse_energy_ring
            # target_data_pulse_energy_incision
            # target_data_pulse_energy_canal
            # pdf_file