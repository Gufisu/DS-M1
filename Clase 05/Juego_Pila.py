import random as r

class Juego_Pila(object):
    def __init__(self):
        self.__list = []
        
    def crearPila(self):
        self.__list = list(range(1,21))

    def jugar(self):
        self.crearPila()
        self.__desordenarPilaAleatorio()
        calificacion = 10
        nro = 20
        lista_esperados = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
        while (nro > 19):
            nro = input('Ingresar la cantidad de elementos:')
            if (nro not in lista_esperados):
                nro = 20
            else:
                nro = int(nro)
        print('Pila Original:')
        self.__mostrarPila()
        suma = 0
        while (nro > 0):
            suma += self.__pop()
            nro-= 1

        print('Pila Obtenida:')
        self.__mostrarPila()
        nro = self.__size()
        print('Con esa cantidad de elementos se sumó:', suma)
        if(suma > 50):
            print('No se cumplió el objetivo')
        else:
            while(suma <= 50):
                suma += self.__pop()
                if (suma <= 50):
                    calificacion-=1
            print('objetivo cumplido!!! Calificacion:', calificacion)
        
    def __desordenarPilaAleatorio(self):
        for i in range(0,20):
            aux = self.__list[i]
            i_rand = r.randint(0,19)
            self.__list[i] = self.__list[i_rand]
            self.__list[i_rand] = aux

    def __mostrarPila(self):
        print(self.__list)

    # Quitar un elemento de la Pila
    def __pop(self):
        return self.__list.pop()

    # Devuelve el número de elementos en la Pila
    def __size(self):
         return len(self.__list)

j=Juego_Pila()

j.jugar()