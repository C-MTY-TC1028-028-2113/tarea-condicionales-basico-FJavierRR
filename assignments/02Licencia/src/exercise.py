
def main():
    edad = int(input("Ingresa tu edad: "))

    if edad >= 18:
        documentos = str(input("¿Tienes identificación oficial? (s/n): "))
        if documentos == "s":
            print("Trámite de licencia concedido")
        elif documentos == "n":
            print("No cumples requisitos")
        else: 
            print("Respuesta incorrecta")
    elif edad > 0 and edad < 18:
        print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")
        
    

if __name__ == '__main__':
    main()
