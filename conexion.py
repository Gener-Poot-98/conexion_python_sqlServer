from bd import conexion

#CRUD
#Read
#seleccionar toda la información de la tabla películas
try:
    with conexion.cursor() as cursor:
        cursor.execute("select idPel, titulo, year from peliculas")
        peliculas = cursor.fetchall()
        for pelicula in peliculas:
            print(pelicula)
except Exception as e:
    print("Ocurrió un error al consultar peliculas: ", e)
#finally:
    #conexion.close
    
  
    
    