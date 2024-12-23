import os
from datetime import datetime

# Configuración de la base de datos
DB_NAME = "cris9546$corporaciondb"
DB_USER = "cris9546"
DB_PASSWORD = "BR3LAF+R7+xBee=t+d2F"
DB_HOST = "cris9546.mysql.pythonanywhere-services.com" 

# Carpeta para guardar los respaldos
BACKUP_DIR = "/home/cris9546/backups/corporacion/"
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

# Generar el nombre del archivo de respaldo
fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_file = os.path.join(BACKUP_DIR, f"backup_{fecha}.sql")

# Comando para generar el respaldo
command = f"mysqldump -h {DB_HOST} -u {DB_USER} -p'{DB_PASSWORD}' {DB_NAME} > {backup_file}"

# Ejecutar el comando
os.system(command)



# Eliminar respaldos más antiguos de 5 días
for file in os.listdir(BACKUP_DIR):
    file_path = os.path.join(BACKUP_DIR, file)
    if os.path.isfile(file_path):
        file_age = (datetime.now() - datetime.fromtimestamp(os.path.getmtime(file_path))).days
        if file_age > 5:
            os.remove(file_path)