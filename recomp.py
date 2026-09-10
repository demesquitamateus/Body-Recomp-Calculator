## This beginning portion is to tackle the low hanging fruit of getting the macro nutrient math out of the way

weight=150
fat=0.3*weight
protein=1*weight
fatcal=fat*9
proteincal=protein*4
cal=fatcal+proteincal

weightdelta=-1
caldelta=(weightdelta*3500)/14

averagecal=1845

TDEE=averagecal-caldelta
MaintenanceCarbs=(TDEE-fatcal-proteincal)/4
CutCarbs=(TDEE-fatcal-proteincal-250)/4
BulkCarbs=(TDEE-fatcal-proteincal+250)/4

print("Your total daily calories are", TDEE)
print("Your required carb intake is", CutCarbs)
print("Your required protein intake is", protein)
print("Your required fat intake is", fat)