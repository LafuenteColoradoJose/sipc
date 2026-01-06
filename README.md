# Sistema Inteligente de Predicción Cardiovascular (SIPC)

## Descripción
El Sistema Inteligente de Predicción Cardiovascular (SIPC) es una herramienta diseñada para predecir el riesgo de enfermedades cardiovasculares en pacientes utilizando algoritmos de aprendizaje automático. Este sistema utiliza datos clínicos del paciente para evaluar el riesgo y proporcionar recomendaciones preventivas.

## Características
- **Predicción Basada en Datos Clínicos**: Utiliza información clínica del paciente como niveles de azúcar en sangre, tipo de dolor en el pecho, entre otros, para realizar predicciones.
- **Interfaz Moderna y Responsive**: Rediseñada con secciones claras, controles interactivos (sliders, toggles) y visualización de datos mejorada.
- **Modo Oscuro**: Soporte nativo para tema claro y oscuro, con detección automática de preferencia del sistema y persistencia.
- **Resultados Inmediatos**: Proporciona predicciones en tiempo real con una representación porcentual del riesgo cardiovascular.

## Tecnologías Utilizadas
- [Nuxt 4](https://nuxt.com/ "Title"): Para la interfaz de usuario y la interactividad del frontend, utilizando la última arquitectura de Nuxt.
![Nuxtjs](https://img.shields.io/badge/Nuxt-002E3B?style=for-the-badge&logo=nuxtdotjs&logoColor=#00DC82)

- [Tensorflow.js](https://www.tensorflow.org/js?hl=es): Para ejecutar modelos de aprendizaje automático directamente en el navegador.
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

- [Tailwind CSS v4](https://tailwindcss.com/): Para estilizar la aplicación con el nuevo motor de estilos y theming manual mediante variables CSS.
![Tailwind](https://img.shields.io/badge/TailwindCSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

- [Heart Disease prediction](https://www.kaggle.com/datasets/rashadrmammadov/heart-disease-prediction?resource=download)

## Instalación
Para instalar y ejecutar el SIPC en tu entorno local, sigue estos pasos:

1. Clona el repositorio:
```bash
git clone https://github.com/LafuenteColoradoJose/sipc.git
```
2. Navega al directorio del proyecto:
```bash
cd sipc
```
3. Instala las dependencias:
```bash
npm install
```
4. Inicia la aplicación en modo desarrollo:
```bash
npm run dev
```
5. Abre tu navegador y navega a la siguiente dirección:
```
http://localhost:3000/
```

## Uso
Para utilizar el SIPC, sigue estos pasos:
1. Ingresa los datos clínicos del paciente utilizando los formularios interactivos.
2. Haz clic en el botón "Calcular Riesgo" para procesar los datos con el modelo de IA.
3. Revisa la predicción visual y las métricas proporcionadas por el sistema.

## Para probarlo en línea
Desplegado en Vercel: [SIPC](https://sipc.vercel.app/)