import os
import sys
import ast
import json

class AnalizadorComplejidad(ast.NodeVisitor):
    def __init__(self):
        self.complejidad = 1

    def visit_If(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.complejidad += len(node.values) - 1
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_match_case(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_ListComp(self, node):
        self.complejidad += 1
        self.generic_visit(node)
        
    def visit_DictComp(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_SetComp(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_GeneratorExp(self, node):
        self.complejidad += 1
        self.generic_visit(node)

def calcular(codigo_fuente: str) -> int:
    try:
        arbol = ast.parse(codigo_fuente)
    except SyntaxError:
        return 0 
        
    visitante = AnalizadorComplejidad()
    visitante.visit(arbol)
    return visitante.complejidad

DIRECTORIOS_IGNORADOS = {'venv', 'env', '.venv', 'migrations', '__pycache__', '.git', 'tests'}
ARCHIVOS_IGNORADOS = {'manage.py', 'settings.py', 'wsgi.py', 'asgi.py'}

def es_archivo_valido(ruta):
    nombre = os.path.basename(ruta)
    
    if nombre in ARCHIVOS_IGNORADOS or not nombre.endswith('.py'):
        return False
    
    partes_ruta = ruta.split(os.sep)
    for ignorado in DIRECTORIOS_IGNORADOS:
        if ignorado in partes_ruta:
            return False
            
    return True

def analizar_archivos(rutas_archivos: list, limite_complejidad: int = 15):
    resultados_array = []
    archivos_procesados = 0
    archivos_fallidos = 0
    
    for ruta in rutas_archivos:
        if not os.path.exists(ruta):
            continue 
            
        if not es_archivo_valido(ruta):
            continue
            
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
            
        complejidad = calcular(contenido)
        archivos_procesados += 1
        
        # Asignar el status_code que solicitaste
        if complejidad > limite_complejidad:
            status_code = "DANGER"
            archivos_fallidos += 1
        elif complejidad >= limite_complejidad - 5:
            status_code = "WARN"
        else:
            status_code = "OK"
            
        resultados_array.append({
            "file": ruta,
            "complexity": complejidad,
            "status_code": status_code
        })
    
    # Construcción del diccionario final con la estructura requerida
    salida_json = {
        "analysis_type": "Cyclomatic Complexity",
        "threshold": limite_complejidad,
        "summary": {
            "total_files": archivos_procesados,
            "failed_files": archivos_fallidos
        },
        "results": resultados_array
    }
    
    # Imprimir el JSON formateado con indentación
    print(json.dumps(salida_json, indent=4))
    sys.exit(0)

if __name__ == "__main__":
    archivos_a_analizar = sys.argv[1:]
    limite = 15
    
    if not archivos_a_analizar:
        # Estructura vacía consistente si no hay archivos
        salida_vacia = {
            "analysis_type": "Cyclomatic Complexity",
            "threshold": limite,
            "summary": {
                "total_files": 0,
                "failed_files": 0
            },
            "results": []
        }
        print(json.dumps(salida_vacia, indent=4))
        sys.exit(0)
        
    analizar_archivos(archivos_a_analizar, limite)
