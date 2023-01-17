d = float(input('Digite uma distância em metros: '))

km = d/1000
hm = d/100
dam = d/10
dm = d*10
cm = d*100
mm = d*1000

print(f'A medida de {d} corresponde a:')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')