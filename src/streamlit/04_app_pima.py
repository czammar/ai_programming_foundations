import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Análisis de Diabetes Pima Indian",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Constantes y Carga de Datos ---
@st.cache_data
def load_data():
    """
    Carga el Pima Indian Diabetes Dataset desde el repositorio de la UCI.
    Se eliminan las filas donde Glucose, BloodPressure, SkinThickness, Insulin,
    o BMI son 0, ya que 0 en estos casos indica un valor faltante.
    """
    # URL del dataset (apunta a datos del repositorio de la clase)
    data_url = 'https://raw.githubusercontent.com/czammar/ai_programming_foundations/refs/heads/main/data/pima_diabetes.csv'
    
    data = pd.read_csv(data_url)
    
    # Manejo de valores cero (cero es un marcador de datos perdidos para estas columnas)
    cols_to_clean = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    data[cols_to_clean] = data[cols_to_clean].replace(0, np.nan)
    
    # Imputación simple: Reemplazar NaN por la media de la columna
    for col in cols_to_clean:
        data[col].fillna(data[col].mean(), inplace=True)

    return data

df = load_data()


# --- Sección 1: Análisis y Visualización de Insights ---
def show_eda_insights(data):
    st.header("1. Exploración de Insights del Dataset Pima Indian Diabetes")
    
    # Paginaciones del dashboard...
    tab1, tab2, tab3 = st.tabs(["Estadísticas", "Distribuciones", "Correlación"])
    
    with tab1:
        st.subheader("Estadísticas Descriptivas")
        st.write(data.describe().T.style.background_gradient(cmap='Blues'))
        st.markdown(
            """
            **Observaciones Clave:**
            - **Edad y Embarazos:** Los rangos son amplios, lo que sugiere una
            población diversa.
            - **Outcome (Target):** La media es de 0.349, lo que indica que
            aproximadamente el **34.9%** de las muestras tienen diabetes
            (es un dataset desbalanceado).
            """
        )

    with tab2:
        st.subheader("Visualización de Distribuciones por Outcome")

        # Histograma para Glucose
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data=data, x='Glucose', hue='Outcome', kde=True, bins=25, 
                     palette={0: '#3498db', 1: '#e74c3c'}, ax=ax)
        ax.set_title('Distribución de Glucose por Outcome (0: No Diabetes, 1: Diabetes)')
        ax.set_xlabel('Concentración de Glucose')
        ax.set_ylabel('Frecuencia')
        # Aqui le damos a streamlit plot como objeto de pyplot...
        st.pyplot(fig)
        plt.close(fig)

        st.markdown(
            """
            **Insight:** Las personas con diabetes (Outcome = 1) tienden
            a tener una concentración de Glucose significativamente más alta,
            con sus picos de distribución desplazados hacia la derecha en comparación
            con el grupo sin diabetes.
            """
        )
        
        # Histograma para BMI
        fig_bmi, ax_bmi = plt.subplots(figsize=(10, 6))
        sns.histplot(data=data, x='BMI', hue='Outcome', kde=True, bins=25,
                     palette={0: '#3498db', 1: '#e74c3c'}, ax=ax_bmi)
        ax_bmi.set_title('Distribución de BMI por Outcome')
        ax_bmi.set_xlabel('Índice de Masa Corporal (BMI)')
        ax_bmi.set_ylabel('Frecuencia')
        st.pyplot(fig_bmi)
        plt.close(fig_bmi)


    with tab3:
        st.subheader("Mapa de Calor de Correlación")
        
        fig, ax = plt.subplots(figsize=(10, 8))
        corr = data.corr()
        sns.heatmap(
            corr, annot=True, cmap='coolwarm', fmt=".2f",
            linewidths=.5, ax=ax,
            cbar_kws={'label': 'Coeficiente de Correlación'})
        ax.set_title('Mapa de Calor de Correlación de Características')
        st.pyplot(fig)
        plt.close(fig)
        
        st.markdown(
            """
            **Relación con la variable `Outcome`:**
            - **Glucose** (0.49) y **IMC** (0.31) muestran la correlación
            más fuerte con la probabilidad de diabetes.
            - **Embarazos** (0.22) y **Edad** (0.23) también tienen una
            correlación positiva moderada.
            """
        )


# --- Sección 2: Entrenamiento y Outcomes del Modelo ---
def show_model_results(data):
    st.header("2. Outcomes del Modelo de Regresión Logística")

    # 1. Preparación de datos
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']

    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # 2. Entrenamiento del Modelo
    model = LogisticRegression(solver='liblinear', random_state=42, max_iter=1000)
    model.fit(X_train, y_train)

    # 3. Predicciones
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    # --- Pestañas de Outcomes ---
    tab_metrics, tab_prob, tab_table = st.tabs(
        ["Métricas y Errores", "Curva ROC y Probabilidades", "Datos y Predicciones"]
        )
    
    with tab_metrics:
        st.subheader("Matriz de Confusión y Reporte de Clasificación")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("##### Matriz de Confusión")
            cm = confusion_matrix(y_test, y_pred)

            fig_cm, ax_cm = plt.subplots(figsize=(6, 5))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                        xticklabels=['No Diabetes (0)', 'Diabetes (1)'],
                        yticklabels=['No Diabetes (0)', 'Diabetes (1)'],
                        ax=ax_cm)
            ax_cm.set_ylabel('Valores Reales')
            ax_cm.set_xlabel('Predicciones del Modelo')
            ax_cm.set_title('Matriz de Confusión')
            st.pyplot(fig_cm)
            plt.close(fig_cm)

        with col2:
            st.markdown("##### Reporte de Clasificación")
            report = classification_report(
                y_test, y_pred,
                output_dict=True, target_names=['No Diabetes (0)', 'Diabetes (1)'])
            report_df = pd.DataFrame(report).transpose().round(3)
            st.dataframe(report_df, use_container_width=True)
            
            st.markdown(
                """
                **Métricas (Macro Avg):**
                - **Precisión (Precision):** Del total de predicciones
                positivas para una clase, cuántas fueron correctas.
                - **Recuperación (Recall):** De todos los casos reales 
                de una clase, cuántos se predijeron correctamente.
                - **F1-Score:** Media armónica de precisión y recuperación.
                """
            )
            
    with tab_prob:
        st.subheader("Distribución de Predicciones y Curva ROC")
        
        col_prob1, col_prob2 = st.columns(2)
        
        with col_prob1:
            st.markdown("##### Distribución de Probabilidades Predichas")
            # Distribución de probabilidades
            fig_dist, ax_dist = plt.subplots(figsize=(8, 6))
            sns.histplot(y_proba[y_test == 0], color='#3498db', kde=True, label='No Diabetes (0)', bins=20, ax=ax_dist)
            sns.histplot(y_proba[y_test == 1], color='#e74c3c', kde=True, label='Diabetes (1)', bins=20, ax=ax_dist)
            ax_dist.set_title('Distribución de Probabilidades Predichas')
            ax_dist.set_xlabel('Probabilidad Predicha (P(y=1))')
            ax_dist.set_ylabel('Frecuencia')
            ax_dist.legend()
            st.pyplot(fig_dist)
            plt.close(fig_dist)
            
            st.markdown(
                """
                **Distribución:** Idealmente, las distribuciones de probabilidad para ambas clases no deberían superponerse; la superposición indica la zona de confusión del modelo.
                """
            )

        with col_prob2:
            st.markdown("##### Curva ROC (Receiver Operating Characteristic)")
            # Curva ROC
            fpr, tpr, thresholds = roc_curve(y_test, y_proba)
            roc_auc = auc(fpr, tpr)
            
            fig_roc, ax_roc = plt.subplots(figsize=(8, 6))
            ax_roc.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (área = {roc_auc:.2f})')
            ax_roc.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Azar')
            ax_roc.set_xlim([0.0, 1.0])
            ax_roc.set_ylim([0.0, 1.05])
            ax_roc.set_xlabel('Tasa de Falsos Positivos (FPR)')
            ax_roc.set_ylabel('Tasa de Verdaderos Positivos (TPR)')
            ax_roc.set_title('Curva ROC para Regresión Logística')
            ax_roc.legend(loc="lower right")
            st.pyplot(fig_roc)
            plt.close(fig_roc)
            
            st.markdown(
                f"""**AUC:** Un valor de AUC de **{roc_auc:.2f}** indica la 
                capacidad del modelo para distinguir entre las clases 
                positiva y negativa. Cuanto más cerca de 1, mejor.""")
            
    with tab_table:
        st.subheader("Datos de Prueba y Predicciones del Modelo")
        
        # Combinar datos de prueba, predicciones y probabilidades
        results_df = X_test.copy()
        results_df['real_Outcome'] = y_test
        results_df['predicted'] = y_pred
        results_df['probability (y=1)'] = y_proba.round(4)
        
        # Calcular el error: 1 si la predicción es incorrecta, 0 si es correcta
        results_df['Error'] = np.where(
            results_df['real_Outcome'] == results_df['predicted'],
            'Correcto', 'Incorrecto')
        
        st.markdown(
            """
            Tabla con los datos de prueba (`X_test`), el valor real (`y_test`),
            la predicción del modelo y si el Outcome fue un error.
            """
        )
        
        # Mostrar las primeras 20 filas ordenadas por probabilidad para ver el límite de decisión
        st.dataframe(
            results_df.sort_values(by='probability (y=1)', ascending=False).head(20),
            use_container_width=True)

# --- Estructura Principal de la App ---

st.title("Aplicación de Análisis Predictivo de Diabetes")
st.markdown("### Modelo de Clasificación con Regresión Logística")

# Ejecutar las funciones
show_eda_insights(df)
st.markdown("---")
show_model_results(df)

st.markdown(
    """
    **Nota sobre la limpieza de datos:** Se imputaron los valores 0 
    (que representan datos faltantes) 
    con la media de la columna correspondiente para permitir el entrenamiento del modelo.
    """
)