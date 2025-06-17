import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('logs.db')
cur = conn.cursor()

# Exécute la requête pour récupérer toutes les données
cur.execute("SELECT * FROM utilisateur")
utilisateurs = cur.fetchall()

print("""
      







`7MN.   `7MF'     db      `7MMF'  `7MMF'`7MN.   `7MF'     db      `7MMF'  `7MMF' 
  MMN.    M      ;MM:       MM      MM    MMN.    M      ;MM:       MM      MM 
  M YMb   M     ,V^MM.      MM      MM    M YMb   M     ,V^MM.      MM      MM  
  M  `MN. M    ,M  `MM      MMmmmmmmMM    M  `MN. M    ,M  `MM      MMmmmmmmMM  
  M   `MM.M    AbmmmqMA     MM      MM    M   `MM.M    AbmmmqMA     MM      MM 
  M     YMM   A'     VML    MM      MM    M     YMM   A'     VML    MM      MM 
.JML.    YM .AMA.   .AMMA..JMML.  .JMML..JML.    YM .AMA.   .AMMA..JMML.  .JMML. 

      

      """)

# Affiche les résultats
print("Utilisateurs enregistrés avec leurs mots de passes :")
for email, password in utilisateurs:
    print(f"Email : {email} | Password : {password}")

# Ferme la connexion de la data.base
conn.close()
