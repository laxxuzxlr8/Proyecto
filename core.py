import json
import os

# --- #: Rutas de Base de Datos :# --- #

RUTA_INVENTARIO = "data/inventario.json"
RUTA_COMBATES = "data/combates.json"

# --- #: Variables Datos Cargados :# --- #

COMBATES = []
INVENTARIO = {}


# --- #: Función Cargar data :# --- #

def cargar_combates():             # Cargar Combates #
    global COMBATES
    
    if not os.path.exists(RUTA_COMBATES):
        return
    try:
        with open(RUTA_COMBATES, "r") as f:
            COMBATES = json.load(f)   
    except Exception as e:
        print(f'Error al cargar datos: {e}')
        
def cargar_inventario():          # Cargar Inventario #
    global INVENTORIO
    
    if not os.path.exists(RUTA_INVENTARIO):
        return
    try:
        with open(RUTA_INVENTARIO, "r") as f:
            data = json.load(f)
            INVENTORIO = data.get("inventorio", {})  
            INVENTORIO = {k: v for k, v in INVENTORIO.items()}
    except Exception as e:
        print(f'Error al cargar datos: {e}')
        
def guardar_combates():           # Guardar Combates #
    global COMBATES
    data = {
        "combates": COMBATES
    }
    with open(RUTA_COMBATES, "w") as f:
        json.dump(data, f, indent=4)