import sys
import json

def get_top_n(data, n):
    """
    Extrae los N elementos con mayor conteo
    """
    # Convertir a lista de pares (clave, valor)
    items = data.items()
    
    # Ordenar por valor descendente
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    
    # Tomar los primeros N
    top_items = sorted_items[:n]
    
    # Convertir de vuelta a diccionario
    top_dict = dict(top_items)
    
    return top_dict

if __name__ == "__main__":
    # Si no se pasa argumento, usar 5 por defecto
    if len(sys.argv) == 1:
        n = 5
    elif len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            if n <= 0:
                print("Error: N debe ser un número positivo", file=sys.stderr)
                sys.exit(1)
        except ValueError:
            print("Error: N debe ser un número entero", file=sys.stderr)
            sys.exit(1)
    else:
        print("Uso: python3 topn.py [N]", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Leer JSON desde stdin
        input_data = sys.stdin.read()
        data = json.loads(input_data)
        
        # Obtener top N
        top_n_data = get_top_n(data, n)
        
        # Imprimir resultado
        print(json.dumps(top_n_data, indent=2))
        
    except json.JSONDecodeError:
        print("Error: Entrada no es JSON válido", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
        