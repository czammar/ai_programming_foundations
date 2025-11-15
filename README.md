# ai_programming_foundations
A repository for "AI Programming Foundations" Course



# 1. ¿Cómo trabajar con un ambiente virtual?

## 1.1 Usando Python con mi instalación nativa:

### Creando un ambiente virtual
**Windows**
```
py -m venv venv\ # Opcion 1
\AppData\Local\Programs\Python\Python312\python -m venv venv\ # Opcion 2
```
**Nota:** Debes cambiar el PATH ´\AppData\Local\Programs\Python\Python312\python´ por donde se encuentra instalada tu versión de Python.

**MacOS o GNU/Linux**
```
python3 -m venv venv/
```

### Activando el ambiente
```
venv\Scripts\activate # Windows
source venv/bin/activate # Linux / MacOS
```

### Desactivando el ambiente

```
deactivate
```

Ver más: 1) https://docs.python.org/3/library/venv.html, 2) https://realpython.com/python-virtual-environments-a-primer/

## 1.2 Usando un manejador de versiones:
**Usando Conda**
Ejemplo usado Python 3.1.3
```
conda create --name py313 python=3.13 # Crea el ambiente
conda activate py313 # Activamos el ambiente
conda deactivate  # Desactivamos el ambiente
```
* Notas: Existen otros manejadores usados en la industria:
  * Poetry: https://python-poetry.org
  * UV:https://docs.astral.sh/uv/

# 2. ¿Cómo trabajar con un ambiente virtual?

## 2.1 Crear un kernel de Python
```
pip install ipykernel notebook jupyterlab
python -m ipykernel install --user --name=ai_tecmilenio --display-name="Python (ai_tecmilenio)"
```

## 2.2 Desplegando Jupyter Lab
```
jupyter notebook # Desplegar Jupyter Notebook
jupyter lab # Desplegar Jupyter Lab
```

# 3. ¿Cómo correr las aplicaciones de streamlit?

Con el ambiente virtual activo:

```
pip install streamlit
streamlit run path/to/my_app.py # Run the dashboard
streamlit run ./src/streamlit/04_app_pima.py # Class example
```