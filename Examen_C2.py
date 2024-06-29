import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3


total_alumnos = 25596861
hombres = 13004267
mujeres = total_alumnos - hombres
secundaria_total = 3083130
hombres_secundaria = 3083130  
mujeres_secundaria = secundaria_total - hombres_secundaria
primaria_total = 14860704
mujeres_primaria = 7267292
hombres_primaria = primaria_total - mujeres_primaria
preescolar_total = 4608255
hombres_preescolar = 2327725
mujeres_preescolar = preescolar_total - hombres_preescolar


p_mujer = mujeres / total_alumnos
p_preescolar_primaria = (preescolar_total + primaria_total) / total_alumnos
p_hombre_preescolar = hombres_preescolar / total_alumnos
p_mujer_secundaria = mujeres_secundaria / total_alumnos
p_hombre_primaria = (hombres + primaria_total - hombres_primaria) / total_alumnos
p_hombre_dado_secundaria = hombres_secundaria / secundaria_total
p_secundaria_dado_mujer = mujeres_secundaria / mujeres

p_hombre_y_secundaria = hombres_secundaria / total_alumnos
p_hombre = hombres / total_alumnos
p_secundaria = secundaria_total / total_alumnos
independientes = p_hombre_y_secundaria == p_hombre * p_secundaria


print(f"Probabilidad de que un alumno elegido al azar sea mujer: {p_mujer:.4f}")
print(f"Probabilidad de que curse preescolar o primaria: {p_preescolar_primaria:.4f}")
print(f"Probabilidad de que sea hombre y esté en preescolar: {p_hombre_preescolar:.4f}")
print(f"Probabilidad de que sea mujer y curse nivel secundaria: {p_mujer_secundaria:.4f}")
print(f"Probabilidad de que sea hombre o curse nivel primaria: {p_hombre_primaria:.4f}")
print(f"Probabilidad de que sea hombre, dado que estudia en nivel secundaria: {p_hombre_dado_secundaria:.4f}")
print(f"Probabilidad de que estudie secundaria, dado que es mujer: {p_secundaria_dado_mujer:.4f}")
print(f"¿Son eventos independientes ser hombre y estudiar el nivel secundaria?: {independientes}")

plt.figure(figsize=(8, 8))
venn2(subsets=(preescolar_total, primaria_total, 0),
      set_labels=('Preescolar', 'Primaria'))
plt.title('Diagrama de Venn para preescolar o primaria')
plt.show()

plt.figure(figsize=(8, 8))
venn3(subsets=(hombres, primaria_total, hombres_primaria, 0, 0, 0, 0),
      set_labels=('Hombres', 'Primaria', 'Intersección'))
plt.title('Diagrama de Venn para hombre o primaria')
plt.show()
