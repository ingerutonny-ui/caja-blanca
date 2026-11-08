def calcular_estadistica(opcion, datos):
    """
    Función única que calcula la Media Aritmética, Mediana o Moda
    según la opción seleccionada.
    """
    n = len(datos)
    
    # Validar si la lista está vacía
    if n == 0:
        return "Error: La lista de datos está vacía"

    # Opción 1: Media Aritmética
    if opcion == 1:
        suma = 0
        for x in datos:
            suma += x
        media = suma / n
        return media

    # Opción 2: Mediana
    elif opcion == 2:
        # Ordenar los datos para encontrar el valor central
        datos_ordenados = sorted(datos)
        mitad = n // 2
        
        if n % 2 == 0:
            mediana = (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            mediana = datos_ordenados[mitad]
        return mediana

    # Opción 3: Moda
    elif opcion == 3:
        max_frecuencia = 0
        moda = datos[0]
        
        for i in range(n):
            frecuencia = 0
            for j in range(n):
                if datos[j] == datos[i]:
                    frecuencia += 1
            
            if frecuencia > max_frecuencia:
                max_frecuencia = frecuencia
                moda = datos[i]
        return moda

    # Opción inválida
    else:
        return "Error: Opción no válida"

# Ejemplo de prueba local
if __name__ == "__main__":
    muestra = [2, 4, 4, 6, 8]
    print("Media:", calcular_estadistica(1, muestra))
    print("Mediana:", calcular_estadistica(2, muestra))
    print("Moda:", calcular_estadistica(3, muestra))
