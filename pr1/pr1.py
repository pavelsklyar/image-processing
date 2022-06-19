from colormath.color_conversions import *
from colormath.color_objects import *
from colormath.color_diff import *

lab_color = LabColor(36, 81, -104)
lch_color = convert_color(lab_color, LCHabColor)
rgb_color = convert_color(lab_color, sRGBColor)
hsv_color = convert_color(rgb_color, HSVColor)
hsl_color = convert_color(rgb_color, HSLColor)

print("Цвет в LAB пространстве и конвертации:\n")
print(lab_color)
print(lch_color)
print(f'RGB color: {rgb_color.get_upscaled_value_tuple()}')
print(hsv_color)
print(hsl_color)

print('-----------------------')

lch_to_lab = convert_color(lch_color, LabColor)
rgb_to_lab = convert_color(rgb_color, LabColor)
hsv_to_rgb = convert_color(hsv_color, LabColor)
hsl_to_rgb = convert_color(hsl_color, LabColor)

print("Обратная конвертация в LAB:\n")
print(f"LCH в LAB: {lch_to_lab}")
print(f"RGB в LAB: {rgb_to_lab}")
print(f"HSV в LAB: {hsv_to_rgb}")
print(f"HSL в LAB: {hsl_to_rgb}")

print('-----------------------')

e_lab_lch_to_lab = delta_e_cie1976(lab_color, lch_to_lab)
e_lab_rgb_to_lab = delta_e_cie1976(lab_color, rgb_to_lab)
e_lab_hsv_to_lab = delta_e_cie1976(lab_color, hsv_to_rgb)
e_lab_hsl_to_lab = delta_e_cie1976(lab_color, hsl_to_rgb)

print("Вычисление ΔE:\n")
print(e_lab_lch_to_lab)
print(e_lab_rgb_to_lab)
print(e_lab_hsv_to_lab)
print(e_lab_hsl_to_lab)

print('-----------------')

e_94_lab_lch_to_lab = delta_e_cie1994(lab_color, lch_to_lab)
e_94_lab_rgb_to_lab = delta_e_cie1994(lab_color, rgb_to_lab)
e_94_lab_hsv_to_lab = delta_e_cie1994(lab_color, hsv_to_rgb)
e_94_lab_hsl_to_lab = delta_e_cie1994(lab_color, hsl_to_rgb)

print("Вычисление ΔE94:\n")
print(e_94_lab_lch_to_lab)
print(e_94_lab_rgb_to_lab)
print(e_94_lab_hsv_to_lab)
print(e_94_lab_hsl_to_lab)

print('-----------------')

e_00_lab_lch_to_lab = delta_e_cie2000(lab_color, lch_to_lab)
e_00_lab_rgb_to_lab = delta_e_cie2000(lab_color, rgb_to_lab)
e_00_lab_hsv_to_lab = delta_e_cie2000(lab_color, hsv_to_rgb)
e_00_lab_hsl_to_lab = delta_e_cie2000(lab_color, hsl_to_rgb)

print("Вычисление ΔE00:\n")
print(e_00_lab_lch_to_lab)
print(e_00_lab_rgb_to_lab)
print(e_00_lab_hsv_to_lab)
print(e_00_lab_hsl_to_lab)
