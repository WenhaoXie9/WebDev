# Generated by Django 4.1.2 on 2022-10-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('Sim_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Pixel_name', models.CharField(max_length=32)),
                ('Size', models.CharField(max_length=32)),
                ('True_w_h', models.CharField(max_length=32)),
                ('K1_1', models.FloatField()),
                ('K2_1', models.FloatField()),
                ('A1P_1', models.FloatField()),
                ('A1_OS1', models.CharField(max_length=32)),
                ('A2P_1', models.FloatField()),
                ('A2_OS1', models.CharField(max_length=32)),
                ('Mesh_width', models.FloatField()),
                ('A1_1', models.FloatField()),
                ('A2_1', models.FloatField()),
                ('Comment', models.CharField(max_length=64)),
                ('Time_stamp', models.CharField(max_length=32)),
                ('SSIM', models.FloatField()),
                ('STD', models.FloatField()),
                ('STD_BOX', models.FloatField()),
                ('Entropy_gau', models.FloatField()),
                ('Dots_box', models.IntegerField()),
                ('Dots_Regularity', models.FloatField()),
                ('Closest_color_std', models.FloatField()),
                ('RMSE', models.FloatField()),
                ('Entropy_dot', models.FloatField()),
                ('CSF_lvl', models.FloatField()),
                ('Lowpass_lvl', models.FloatField()),
                ('STD_CSF_lvl', models.FloatField()),
                ('STD_lowpass_lvl', models.FloatField()),
                ('Dot_Box_Regularity', models.FloatField()),
                ('Crossed_RGB', models.CharField(max_length=64)),
                ('Crossed_RGB_std', models.FloatField()),
                ('Color_hist', models.IntegerField()),
                ('Color_color', models.CharField(max_length=64)),
                ('PSNR', models.FloatField()),
                ('Lvl_Gau', models.CharField(max_length=32)),
                ('Diag_ratio', models.FloatField()),
                ('Distance_Weighted_FFT_Sum', models.FloatField()),
                ('Peaks_freaq', models.CharField(max_length=64)),
                ('Peaks_mag', models.CharField(max_length=64)),
                ('Weighted_Mag_Sum', models.FloatField()),
                ('FFT_Grade', models.IntegerField()),
                ('Peak12_min', models.FloatField()),
                ('Ref_color', models.CharField(max_length=32)),
                ('Coords', models.CharField(max_length=64)),
                ('Mesh_density', models.FloatField()),
                ('Diag_31', models.FloatField()),
                ('Diag_24', models.FloatField()),
                ('Aspect_ratio', models.IntegerField()),
                ('v2v4_ppdd', models.CharField(max_length=32)),
                ('Frac_SP', models.CharField(max_length=64)),
            ],
        ),
    ]