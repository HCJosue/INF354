class alumno:
  def __init__(self, nombre, edad,direccion):
    self.nombre=nombre
    self.edad=edad
    self.direccion=direccion
  def __str__(self):
    return f"Name: {self.nombre}; Edad: {self.edad}; Direccion: {self.direccion}"
class gondola:
  def __init__(self,nombrechofer,placa):
    self.nombrechofer=nombrechofer
    self.placa=placa
    self.listarecoger=[]
  def agregar(self,alumno):
    self.listarecoger.append(alumno)
  def mostrargondola(self):
    resultado=f"Nombre del chofer: {self.nombrechofer}; placa: {self.placa} \n"
    resultado=resultado+"Lista de alumno para recoger \n"
    for i in range(len(self.listarecoger)):
      resultado=resultado+"Alumno "+str(i+1)+"\n"+self.listarecoger[i].__str__()+"\n"
    print(resultado)
alumno1=alumno("Josue",23,"Miraflores")
alumno2=alumno("Gabriel",23,"Vita")
alumno3=alumno("Quispe",22,"Stadium")
alumno4=alumno("Huiza",20,"Obelisco")
gondola1=gondola("Prueba","ABC123")
gondola1.agregar(alumno1)
gondola1.agregar(alumno2)
gondola1.agregar(alumno3)
gondola1.agregar(alumno4)
print("======Mostrado con procedimiento y funciones dentro de las clases======")
gondola1.mostrargondola()
print("======Mostrado sin procedimiento y funciones dentro de las clases======")
print("Nombre del chofer: "+gondola1.nombrechofer+"; placa: "+gondola1.placa)
print("Lista de alumno para recoger")
for i in range(len(gondola1.listarecoger)):
  print("Alumno "+str(i+1))
  print("Nombre: "+gondola1.listarecoger[i].nombre+"; Edad: "+str(gondola1.listarecoger[i].edad)+"; Direccion: "+gondola1.listarecoger[i].direccion)
