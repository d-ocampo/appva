# Proyecto de Visualización de Clusters en Dash - Francia

Este proyecto es una aplicación web desarrollada con [Dash](https://dash.plotly.com/), que permite la visualización interactiva de clusters y análisis de datos geográficos y demográficos. La aplicación está diseñada para analizar y visualizar datos agrupados por entidades, departamentos y regiones, con un enfoque específico en los datos de Francia.

## Características

- **Visualización de clusters**: Muestra gráficos de categorías paralelas para explorar la distribución de clusters por región y ANS.
- **Análisis por departamento y entidad**: Proporciona gráficos que permiten explorar diversas variables a nivel de departamento y entidad.
- **Integración con ObservableHQ**: Incluye un iframe que carga contenido interactivo desarrollado en ObservableHQ.
- **Interfaz interactiva**: Permite la selección dinámica de entidades, variables y departamentos para actualizar las visualizaciones en tiempo real.

## Requisitos previos

Antes de ejecutar la aplicación, asegúrate de tener instalado lo siguiente:

- Python 3.7+
- Las siguientes bibliotecas de Python:

```bash
pip install dash plotly pandas numpy
```

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación Dash.
- `assets/`: Carpeta que contiene archivos estáticos, como CSS, JS, imágenes, y datos.
  - `data/`: Contiene los archivos CSV de clusters y diccionarios de variables.
  - `figs.py`: Módulo con funciones para la generación de gráficos.
  - `prueba.html`: Archivo HTML cargado en el iframe desde ObservableHQ.

## Ejecución de la Aplicación

Para ejecutar la aplicación localmente, sigue estos pasos:

1. Clona el repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Ejecuta el archivo `app.py`:

```bash
python app.py
```

4. Abre un navegador web y dirígete a `http://localhost:8051` para interactuar con la aplicación.

## Uso

1. **Selecciona una Entidad**: Usa las opciones del menú de radio para seleccionar la entidad de interés.
2. **Selecciona una Variable**: Usa el menú desplegable para seleccionar la variable que deseas analizar.
3. **Selecciona un Departamento**: (Opcional) Filtra los resultados por un departamento específico.
4. **Visualiza los Gráficos**: Observa cómo cambian los gráficos en función de tus selecciones.

## Personalización

Si necesitas adaptar la aplicación a diferentes conjuntos de datos o visualizaciones, puedes modificar los archivos en la carpeta `assets/data` y ajustar las funciones en `figs.py` para generar nuevos gráficos.

## Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para sugerencias o mejoras.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.
