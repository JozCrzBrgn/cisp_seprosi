
import json

def read_json_from_supabase(db, bucket_name, file_name):
        # Descarga el archivo desde el almacenamiento de Supabase
        response = db.storage.from_(bucket_name).download(file_name)
        # Carga el contenido del archivo JSON
        json_data = json.loads(response)
        return json_data