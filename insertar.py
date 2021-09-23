from bd import conexion

try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO peliculas(titulo, year) VALUES (?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, ("Volver al futuro 1", 1985))
        cursor.execute(consulta, ("Pulp Fiction", 1994))
        cursor.execute(consulta, ("It", 2017))
        cursor.execute(consulta, ("Ready Player One", 2018))
        cursor.execute(consulta, ("Spider-Man: un nuevo universo", 2018))
        cursor.execute(consulta, ("Avengers: Endgame", 2019))
        cursor.execute(consulta, ("John Wick 3: Parabellum", 2019))
        cursor.execute(consulta, ("Toy Story 4", 2019))
        cursor.execute(consulta, ("It 2", 2019))
        cursor.execute(consulta, ("Spider-Man: lejos de casa", 2019))

except Exception as e:
    print("Ocurrió un error al insertar: ", e)
#finally:
 #   conexion.close() 
try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO cines(nombre, direc) VALUES (?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, ("cinemex polanco", "polanco"))
        cursor.execute(consulta, ("cinemex loreto", "loreto"))
        cursor.execute(consulta, ("cinepolis san angel", "san angel"))
        cursor.execute(consulta, ("cinepolis pedregal", "pedregal"))
        
except Exception as e:
    print("Ocurrió un error al insertar: ", e)
#finally:
 #   conexion.close()
try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO pelicula_cines(idPel, idCine) VALUES (?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, (1,1))
        cursor.execute(consulta, (2,2))
        cursor.execute(consulta, (3,3))
        cursor.execute(consulta, (4,4))
        cursor.execute(consulta, (5,4))
        cursor.execute(consulta, (6,3))
        cursor.execute(consulta, (7,2))
        cursor.execute(consulta, (8,1))
        cursor.execute(consulta, (9,1))
        cursor.execute(consulta, (10,1))
        
except Exception as e:
    print("Ocurrió un error al insertar: ", e)
#finally:
    #conexion.close()