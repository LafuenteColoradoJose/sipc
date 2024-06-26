<template>
    <div :class="{ 'theme-dark': theme === 'dark', 'theme-light': theme === 'light' }">
        <div>
            <h1>Predicción del riesgo de enfermedades cardíacas</h1>
            <form @submit.prevent="predictHeartDisease" class="flex flex-wrap justify-between items-center m-2 gap-4">
                <div class="flex gap-2">
                    <label>Edad</label>
                    <input min="0" v-model="age" label="Edad" type="number"  />
                </div>
                <div class="flex gap-2">
                    <label>Género</label>
                    <select v-model="gender" label="Género">
                        <option value=0>Masculino</option>
                        <option value=1>Femenino</option>
                    </select>
                </div>
                <div class="flex gap-2">
                    <label>Colesterol</label>
                    <input min="0" v-model="cholesterol" label="Colesterol" type="number" />
                </div>
                <div class="flex gap-2">
                    <label>Presión Arterial</label>
                    <input min="0" v-model="bloodPressure" label="Presión Arterial" type="number" />
                </div>
                <div class="flex gap-2">
                    <label>Frecuencia Cardíaca</label>
                    <input min="0" v-model="heartRate" label="Frecuencia Cardíaca" type="number" />
                </div>
                <div class="flex gap-2">
                    <label>Fumador</label>
                    <select v-model="smoking" label="Fumador">
                        <option value=0>Nunca</option>
                        <option value=1>Anteriormente</option>
                        <option value=2>Actualmente</option>
                    </select>
                </div>
                <div class="flex gap-2">
                    <label for="">Consumo de alcohol</label>
                    <select v-model="alcoholIntake" label="Consumo de Alcohol">
                        <option value=0>Ninguno</option>
                        <option value=1>Moderado</option>
                        <option value=2>A menudo</option>
                    </select>
                </div>
                <div class="flex gap-2">
                    <label>Horas de Ejercicio</label>
                    <input min="0" v-model="exerciseHours" label="Horas de Ejercicio" type="number" />
                </div>
                <div class="flex gap-2">
                    <label>Historial Familiar</label>
                    <select v-model="familyHistory" label="Historial Familiar">
                        <option value=0>No</option>
                        <option value=1>Sí</option>
                    </select>
                </div>
                <div class="flex gap-2">
                    <label>Diabetes</label>
                    <select v-model="diabetes" label="Diabetes">
                        <option value=0>No</option>
                        <option value=1>Sí</option>
                    </select>
                </div>
                <div class="flex gap-2">
                    <label>Obesidad</label>
                    <select v-model="obesity" label="Obesidad">
                        <option value=0>No</option>
                        <option value=1>Sí</option>
                    </select>
                </div>
                <div class="flex gap-2">
                    <label>Nivel de Estrés</label>
                    <input min="0" v-model="stressLevel" label="Nivel de Estrés" type="number" />
                </div>
                <div class="flex gap-2">
                    <label>Azúcar en Sangre</label>
                    <input min="0" v-model="bloodSugar" label="Azúcar en Sangre" type="number" />
                </div>
                <div class="flex gap-2">
                    <label>Angina Inducida por Ejercicio</label>
                    <select v-model="exerciseInducedAngina" label="Angina Inducida por Ejercicio">
                        <option value=0>No</option>
                        <option value=1>Sí</option>
                    </select>
                </div>
                <div class="flex gap-2">
                    <label>Tipo de dolor en el pecho</label>
                    <select v-model="chestPainType" label="Tipo de dolor en el pecho">
                        <option value=0>Angina típica</option>
                        <option value=1>Angina atípica</option>
                        <option value=2>Dolor no anginal</option>
                        <option value=3>Asintomático</option>
                    </select>
                </div>
                <button class="btn btn-primary border-slate-700" type="submit">Predecir riesgo</button>
                <button class="btn btn-primary border-slate-700" @click="dataReset" >Resetear datos</button>
                
            </form>
            <div>
            <div class="flex flex-row items-center gap-3 mb-2">
                <p class="text-lg font-semibold">Riesgo predicho:</p>
                <p class="text-lg font-semibold">{{predictionResult}} %</p>
            </div>
            <div class="flex flex-col justify-center items-center text-xs">
                <span class="text-center">Datos introducidos:</span>
                <div class="flex flex-row justify-between gap-6">
                    <ul>
                        <li>Edad: {{age}}</li>
                        <li>Género: {{gender}}</li>
                        <li>Colesterol: {{cholesterol}}</li>
                        <li>Presión Arterial: {{bloodPressure}}</li>
                        <li>Frecuencia Cardíaca: {{heartRate}}</li>
                        <li>Fumador: {{smoking}}</li>
                        <li>Consumo de alcohol: {{alcoholIntake}}</li>
                    </ul>
                    <ul>
                        <li>Horas de Ejercicio: {{exerciseHours}}</li>
                        <li>Historial Familiar: {{familyHistory}}</li>
                        <li>Diabetes: {{diabetes}}</li>
                        <li>Obesidad: {{obesity}}</li>
                        <li>Nivel de Estrés: {{stressLevel}}</li>
                        <li>Azúcar en Sangre: {{bloodSugar}}</li>
                    </ul>
                </div>
            </div>
        </div>
        </div>

       

    </div>
</template>

<script setup>
import { inject, ref } from 'vue';
// import * as tf from '@tensorflow/tfjs';

useHead({
    title: 'S.I.P.C.',
    meta: [
        {
            name: 'description',
            content: 'Sistema Inteligente de Predicción Cardiovascular',
        },
    ],
    script: [
        {
            src: "https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js",
        },
    ],
});

const theme = inject('theme');

let inpust = ref(null);
let outputs = ref(null);
let inputTensor = ref(null);
let outputTensor = ref(null);
let h = ref(null);
let model = ref(null);

const age = ref(null);
const gender = ref(null);
const cholesterol = ref(null);
const bloodPressure = ref(null);
const heartRate = ref(null);
const smoking = ref(null);
const alcoholIntake = ref(null);
const exerciseHours = ref(null);
const familyHistory = ref(null);
const diabetes = ref(null);
const obesity = ref(null);
const stressLevel = ref(null);
const bloodSugar = ref(null);
const exerciseInducedAngina = ref(null);
const chestPainType = ref(null);
const heartDisease = ref(null);
const predictionResult = ref(null);

async function predictHeartDisease() {
    console.log('pulsado predictHeartDisease');
    
    await makePrediction({
        age: age.value,
        gender: gender.value,
        cholesterol: cholesterol.value,
        bloodPressure: bloodPressure.value,
        heartRate: heartRate.value,
        smoking: smoking.value,
        alcoholIntake: alcoholIntake.value,
        exerciseHours: exerciseHours.value,
        familyHistory: familyHistory.value,
        diabetes: diabetes.value,
        obesity: obesity.value,
        stressLevel: stressLevel.value,
        bloodSugar: bloodSugar.value,
        exerciseInducedAngina: exerciseInducedAngina.value,
        chestPainType: chestPainType.value,

    });

}

onMounted(() => {
    loadData();
    createModel();
    trainModel(inputTensor, outputTensor);

    // // Asegúrate de que esta parte del código se ejecuta después de que TensorFlow.js esté cargado
    // // Aquí puedes inicializar tus tensores o realizar operaciones con ellos
    // inputTensor = tf.tensor2d([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], [1, 15]);
    // outputTensor = tf.tensor2d([[1]], [1, 1]);

    // console.log(inputTensor.shape); // Debería mostrar [1, 15]
    // console.log(outputTensor.shape); // Debería mostrar [1, 1]
});

async function dataReset() {
    age.value = null,
    gender.value = null,
    cholesterol.value = null,
    bloodPressure.value = null,
    heartRate.value = null,
    smoking.value = null,
    alcoholIntake.value = null,
    exerciseHours.value = null,
    familyHistory.value = null,
    diabetes.value = null,
    obesity.value = null,
    stressLevel.value = null,
    bloodSugar.value = null,
    exerciseInducedAngina.value = null,
    chestPainType.value = null,
    heartDisease.value = null,
    predictionResult.value = null;
}

async function loadData() {
    const response = await fetch('heart_disease_dataset_trans.csv');
    const data = await response.text();
    const rows = data.split(/\r\n|\n/).slice(1);

    const processedRows = rows.map((row) => {
        const values = row.split(","); // Asumiendo que es un CSV estándar separado por comas
        return {
            Age: values[0],
            Gender: values[1],
            Cholesterol: values[2],
            BloodPressure: values[3],
            HeartRate: values[4],
            Smoking: values[5],
            AlcoholIntake: values[6],
            ExerciseHours: values[7],
            FamilyHistory: values[8],
            Diabetes: values[9],
            Obesity: values[10],
            StressLevel: values[11],
            BloodSugar: values[12],
            ExerciseInducedAngina: values[13],
            ChestPainType: values[14],
            HeartDisease: values[15], // Asegúrate de que este es el índice correcto
        };
    });
    console.log(processedRows[0]); // Debería mostrar el primer objeto en el array

    // Ahora puedes usar `map` en `processedRows`, que es un array de objetos
    const inputs = processedRows
        .map((row) => [
            parseFloat(row.Age),
            parseFloat(row.Gender),
            parseFloat(row.Cholesterol),
            parseFloat(row.BloodPressure),
            parseFloat(row.HeartRate),
            parseFloat(row.Smoking),
            parseFloat(row.AlcoholIntake),
            parseFloat(row.ExerciseHours),
            parseFloat(row.FamilyHistory),
            parseFloat(row.Diabetes),
            parseFloat(row.Obesity),
            parseFloat(row.StressLevel),
            parseFloat(row.BloodSugar),
            parseFloat(row.ExerciseInducedAngina),
            parseFloat(row.ChestPainType),
        ])
        .filter((row) => row.every((value) => !isNaN(value)));

    const outputs = processedRows
        .map((row) => [parseFloat(row.HeartDisease)])
        .filter((output) => !isNaN(output[0]));

    console.log(inputs);
    console.log(outputs);

    // Convertir a tensores
    inputTensor = tf.tensor2d(inputs);
    outputTensor = tf.tensor2d(outputs);

    // Asegúrate de que las dimensiones de los tensores coincidan con las expectativas del modelo
    console.log(inputTensor.shape); // Debería mostrar [num_samples, 15]
    console.log(outputTensor.shape); // Debería mostrar [num_samples, 1]

    // console.log(inputTensor);
    // console.log(outputTensor);

}

async function createModel() {
    model = tf.sequential();
    console.log(model);
    const hidden = tf.layers.dense({
        units: 10, // Número de nodos en la capa oculta
        inputShape: [15], // Forma de los datos de entrada
        activation: "tanh", // Función de activación
    });

    model.add(hidden);
    console.log(model);

    const output = tf.layers.dense({
        units: 1, // Número de nodos en la capa de salida
        // inputShape: [10], // Forma de los datos de entrada para esta capa
        activation: "sigmoid", // Función de activación para clasificación binaria
    });

    model.add(output);
    console.log(model);

    await model.compile({
        optimizer: "sgd", // Optimizador
        loss: "binaryCrossentropy", // Función de pérdida para clasificación binaria
    });

    console.log(model);

}


async function trainModel(inputTensor, outputTensor) {
    // Verifica que inputTensor y outputTensor no sean undefined o null
    if (!inputTensor || !outputTensor) {
        console.error(
            "trainModel: inputTensor or outputTensor is undefined or null",
        );
        return; // Detiene la ejecución de la función
    }

    // Asegúrate de que inputTensor y outputTensor sean numéricos
    const numericInputTensor = tf.tensor2d(
        inputTensor.arraySync().map((row) => convertToNumeric(row)),
    );
    const numericOutputTensor = tf.tensor2d(
        outputTensor.arraySync().map((row) => convertToNumeric(row)),
    );

    const configTrain = {
        epochs: 10,
        shuffle: true,
        // Añade aquí el resto de la configuración de entrenamiento si es necesario
    };

    await model.fit(numericInputTensor, numericOutputTensor, configTrain);
    console.log("Model trained successfully");
}


async function makePrediction(inputData) {
    console.log('variable inputData:', inputData);

    const inputArray = [
        inputData.age,
        inputData.gender,
        inputData.cholesterol,
        inputData.bloodPressure,
        inputData.heartRate,
        inputData.smoking,
        inputData.alcoholIntake,
        inputData.exerciseHours,
        inputData.familyHistory,
        inputData.diabetes,
        inputData.obesity,
        inputData.stressLevel,
        inputData.bloodSugar,
        inputData.exerciseInducedAngina,
        inputData.chestPainType,
    ];

     // Convertir el array a un tensor 2D (1 fila con N columnas)
     const inputTensor = tf.tensor2d([inputArray]);

    // Realizar la predicción
    let prediction = await model.predict(inputTensor);
    prediction.print(); // Opcional: imprimir el tensor de predicción en la consola

    // Convertir el tensor de predicción a un valor utilizable
    const predictionValue = (prediction.arraySync()[0][0] * 100).toFixed(0);
    console.log(predictionValue);

    // Actualizar el estado de Vue con el resultado
    predictionResult.value = predictionValue; // Asegúrate de que predictionResult esté definido como ref() en <script setup>
}


</script>

<style scoped>
.theme-dark label {
    color: #b1e0e7;
}

.theme-light label {
    color: #007ea8;
}
</style>