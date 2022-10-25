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
       
        # self.__id_equipamento =
        # self.__id_paciente =
        # self.__olho =
        # self.__method =
        # self.__status =
        # self.__planned_by =
        # self.__treated_by =
        # self.__planning_date =
        # self.__treatment_date =
        # self.__confirmed_by =
        # self.__device_sn =
        # self.__refraction_clinical_id =
        # self.__pupil =
        # self.__pachymetry_superior =
        # self.__pachymetry_temporal =
        # self.__pachymetry_central =
        # self.__pachymetry_nasal =
        # self.__pachymetry_inferior =
        # self.__k1 =
        # self.__axis1 =
        # self.__q1 =
        # self.__k2 =
        # self.__q2 =
        # self.__axis2 =
        # self.__refraction_measured_id =
        # self.__refraction_target_id =
        # self.__refraction_correction_id =
        # self.__target_q =
        # self.__optical_zone =
        # self.__transition_zone =
        # self.__ablation_zone =
        # self.__flap_epi_thickness =
        # self.__cornea_thickness =
        # self.__residual_stroma =
        # self.__cyclorotation =
        # self.__centration_x =
        # self.__centration_y =
        # self.__total_duration =
        # self.__breaks_qt =
        # self.__breaks_seconds =
        # self.__pachymetry_records_preop =
        # self.__pachymetry_records_flap_epi_off =
        # self.__pachymetry_records_post_op =
        # self.__maximum_depth =
        # self.__central_depth =
        # self.__memo =
        # self.__flap_diameter =
        # self.__flap_thickness =
        # self.__flap_side_cut_angle =
        # self.__flap_canal_width =
        # self.__flap_canal_lenght_offset =
        # self.__hinge_position =
        # self.__hinge_lenght =
        # self.__hinge_angle =
        # self.__hinge_width =
        # self.__laser_separations_bed_cut_line_separations =
        # self.__laser_separations_bed_cut_spot_separations =
        # self.__laser_separations_side_cut_line_separations =
        # self.__laser_separations_side_cut_spot_separations =
        # self.__measured_data_pulse_energy_bed_cut =
        # self.__measured_data_pulse_energy_side_cut =
        # self.__measured_data_suction_time =
        # self.__measured_data_device_temperature =
        # self.__treatment_data_treatment_progress =
        # self.__treatment_data_treatment_breaks =
        # self.__treatment_data_x_offset =
        # self.__treatment_data_y_offset =
        # self.__ring_outer_diameter =
        # self.__ring_inner_diameter =
        # self.__ring_depth_in_cornea =
        # self.__incision_length =
        # self.__incision_width =
        # self.__incision_position =
        # self.__laser_separations_ring_spot_separations =
        # self.__laser_separations_ring_line_separations =
        # self.__laser_separations_incision_spot_separations =
        # self.__laser_separations_incision_line_separations =
        # self.__measured_data_pulse_energy_ring =
        # self.__measured_data_pulse_energy_incision =
        # self.__flap_offset_torsion =
        # self.__measured_data_pulse_energy_canal =
        # self.__target_data_pulse_energy_ring =
        # self.__target_data_pulse_energy_incision =
        # self.__target_data_pulse_energy_canal =
        # self.__pdf_file =

        