from abc import ABC, abstractmethod

#Clase abstracta que contendrá los comportamientos para los tipos de membresía a implementar
class  Membresia (ABC):
    
    #constructor 
    
    def __init__(self, correo_subs: str, num_tarjeta: str): 
        self.__correo_subs = correo_subs
        self.__num_tarjeta = num_tarjeta
        
    #getter 
    
    #Metodo que devuelve el correo del suscriptor
    @property
    def correo_subs(self):
        return self.__correo_subs
    #Metodo que devuelve el numero de tarjeta 
    @property
    def num_tarjeta(self):
        return self.__num_tarjeta
    
    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int ):
        pass 
     #El metodo va a hacer modificado en cada clase para que 
    #se comporte de cierta manera segun situación
    #se le coloca un pass porque no tiene implementación lógica. 
    
    #Se le agrega '_' para que quede como protegido
    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1: 
            return Membresia_Basica(self.correo_subs, self.num_tarjeta)
        if nueva_membresia == 2: 
            return Membresia_Familiar(self.correo_subs, self.num_tarjeta)
        if nueva_membresia == 3: 
            return Membresia_SinConexion(self.correo_subs, self.num_tarjeta)
        if nueva_membresia == 4: 
            return Membresia_Pro(self.correo_subs, self.num_tarjeta)
    #El metodo va a hacer modificado en cada clase para que 
    #se comporte de cierta manera segun situación
    
class Membresia_Gratis(Membresia):
    
    
    #Atributos
    costo = 0 
    cantidad_dispositivos = 1
    
    def cambiar_suscripcion(self, nueva_membresia: int):
      
      if nueva_membresia < 1 or nueva_membresia > 4: 
          return self
      else: 
        return self._crear_nueva_membresia(nueva_membresia)
    
    
class Membresia_Basica(Membresia):
    #Clase para la membresía básica
    
    costo = 3000
    cantidad_dispositivos = 2
    
    #Constructor de la membresía basica, donde toma igualmente 
    #El constructor de la clase padre 'membresia' por medio del super() y sus parametros
    def __init__(self, correo_subs: str, num_tarjeta: str):
        super().__init__(correo_subs, num_tarjeta)
        
        #El isinstance es para comprobar si el objeto ya creado pertenece a las clases consultadas,
        #este caso membresía familiar o sin conexión y retorna true si es verdadero o false si no es así
        #Esta condicional debe revisarse porque le entrega 7 dias a todos. 
        if isinstance(self, Membresia_Familiar) or isinstance(self, Membresia_SinConexion):
            self.dias_regalo = 7 
        elif isinstance(self, Membresia_Pro):
            self.dias_regalo = 15
        
    def cancelar_suscripcion(self):
        
        return Membresia_Gratis(self.correo_subs, self.num_tarjeta)
    
    def cambiar_suscripcion(self, nueva_membresia: int):
        
        if nueva_membresia < 2 or nueva_membresia > 4: 
            return self #retorna 1 que seria la basica
        else:
            return self._crear_nueva_membresia(nueva_membresia)
        #Si no , creará la nueva membresía tipo gratis

#Se usa la clase membresia básica para utilizar todo lo que hay en ella
class Membresia_Familiar(Membresia_Basica):
    
    #atributos de clase
    
    costo = 5000
    cantidad_dispositivos = 5 
    
#Se agrega este metodo nuevamente para sobreescribirlo     
    def cambiar_suscripcion (self, nueva_membresia: int):
        #si la membresia nueva no está entre la secuencia de numeros de la lista
        if nueva_membresia not in [1,3,4]:    
            return self #Se retorna a si misma
        else: #Si no, crea la nueva membresia de tipo familiar
            return self._crear_nueva_membresia(nueva_membresia)

    def modificar_control_parental(self):
        pass
    #No se ha definido aun la lógica de este método
    
class Membresia_SinConexion(Membresia_Basica):
    
    #atributos de clase 
    costo = 3500
    cantidad_dispositivos =2
    
    #Se escribe este metodo en cada clase, debido a su comportamiento 
    #distinto en cada una de ellas
    def cambiar_suscripcion(self, nueva_membresia: int):
        
        if nueva_membresia not in [1,2,4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_contenido(self):
        pass
    #Este método no tiene sentido(?)
    
class Membresia_Pro(Membresia_Familiar,Membresia_SinConexion,Membresia_Basica):
    
    #atributos de clase
    costo = 7000
    cantidad_dispositivos = 6
    
    def __init__(self, correo_subs: str, num_tarjeta: str):
        super().__init__(correo_subs, num_tarjeta)
    
    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 1 or nueva_membresia >3: 
            return self
        else: 
            return self._crear_nueva_membresia(nueva_membresia)
        
        
#Caso 1: 
g = Membresia_Gratis("correodeprueba@correo.cl", "123")
print(type(g))
#Caso 2: Cambiar de gratis a basica 

#Se crea un objeto basico y se cambia la suscripcion pasandole un uno
basica = g.cambiar_suscripcion(1)
print(type(basica))

#Caso 3: Cambiar de básica a familiar 
f = basica.cambiar_suscripcion(2)
print(type(f))

#Caso 4 : Cambiar a Sin Conexion 
sc = f.cambiar_suscripcion(3)
print(f.dias_regalo)
print(type(sc))
print ("dias de regalo: ", sc.dias_regalo)
#Caso 5: Cambiar a Pro 
p = sc.cambiar_suscripcion(4)
print(type(p))
print("Costo:",p.costo)
print ("dias de regalo: ", p.dias_regalo)


#Caso 6 : Cancelar suscripcion 
#Volvemos a la membresia Gratis
c =  p.cancelar_suscripcion()
print(type(c))


#Conclusión: 
#Se aplicó Herencia , Herencia multiple y polimorfismo al ver comportamientos diferentes para un mismo método
#Se utilizó encapsulación,  ya que los atributos estan protegidos. 