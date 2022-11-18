from rest_framework import serializers
from ProjectView.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=Project
        field=('Sim_ID','Pixel_name','Size', 'True_w_h','K1_1','K2_1','A1P_1','A1_OS1','A2P_1','A2_OS1', 'Mesh_width', 'A1_1','A2_1','Comment','Time_stamp', 'SSIM','STD','STD_BOX','Entropy_gau', 
                'Dots_box', 'Dots_Regularity','Closest_color_std','RMSE', 'Entropy_dot','CSF_lvl', 'Lowpass_lvl','STD_CSF_lvl','STD_lowpass_lvl', 'Dot_Box_Regularity','Crossed_RGB', 'Crossed_RGB_std', 
                'Color_hist', 'Color_color', 'PSNR', 'Lvl_Gau', 'Diag_ratio','Distance_Weighted_FFT_Sum','Peaks_freaq', 'Peaks_mag','Weighted_Mag_Sum','FFT_Grade', 'Peak12_min', 'Ref_color', 
                'Coords', 'Mesh_density','Diag_31','Diag_24','Aspect_ratio','v2v4_ppdd', 'Frac_SP')