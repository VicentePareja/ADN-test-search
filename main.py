import pandas as pd

# Función para cargar datos del archivo Excel
def cargar_datos(ruta_archivo):
    df = pd.read_excel(ruta_archivo)
    print("\nDataFrame cargado correctamente:\n", df)  # Verificar que el DataFrame se cargó
    return df

# Función para contar coincidencias en cada test
def contar_coincidencias(df, genes_usuario):
    coincidencias = {}
    if df.empty:
        print("El DataFrame está vacío. Verifica el archivo de origen.")
        return coincidencias

    for _, row in df.iterrows():
        test_name = row["test"]
        genes_testeados = row["genes testeados"].split(', ')   
        coincidencias[test_name] = len(set(genes_testeados) & set(genes_usuario))
        print(f"Coincidencias en {test_name}: {coincidencias[test_name]}")
    return coincidencias

# Función para ranquear tests por número de coincidencias
def ranquear_tests(coincidencias):
    ranking = sorted(coincidencias.items(), key=lambda x: x[1], reverse=True)
    return ranking

# Función principal que ejecuta el flujo completo
def ejecutar(ruta_archivo):
    df = cargar_datos(ruta_archivo)
    if df.empty:
        print("Error: El archivo de datos está vacío o no se cargó correctamente.")
        return

    genes_usuario = input("Ingrese los genes separados por comas (ej: AAA4, BBB3): ").replace(" ", "").split(',')
    # Contar coincidencias y ranquear
    coincidencias = contar_coincidencias(df, genes_usuario)
    ranking = ranquear_tests(coincidencias)
    
    # Mostrar solo los 10 tests con más coincidencias
    print("\nTop 10 tests por coincidencias:")
    for test, count in ranking[:10]:
        print(f"{test}: {count} coincidencia(s)")

# Llamar a la función principal
ruta_archivo = "DB ADN.xlsx"
ejecutar(ruta_archivo)
