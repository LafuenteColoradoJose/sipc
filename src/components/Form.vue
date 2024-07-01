<template>

    <div>
        <h1>Predicción del riesgo de enfermedades cardíacas</h1>
        <form @submit.prevent="predictHeartDisease" class="flex flex-col justify-between items-center m-2 gap-4 ">
            <section class="grid grid-cols-1 m-2 gap-6 md:grid-cols-2 lg:grid-cols-3">

                <div id="groups1+2" class="flex flex-col justify-between items-center gap-4">

                    <article id="group1" class="flex flex-col justify-between gap-2">
                        <div class="flex gap-2">
                            <label>Edad</label>
                            <input class="input input-bordered input-xs w-full max-w-xs" min="0" v-model="age"
                                label="Edad" type="number" />
                        </div>
                        <div class="flex gap-2">
                            <label>Género</label>
                            <select class="select select-xs w-full max-w-xs" v-model="gender" label="Género">
                                <option value=0>Masculino</option>
                                <option value=1>Femenino</option>
                            </select>
                        </div>
                        <div class="flex gap-2">
                            <label>Colesterol</label>
                            <input class="input input-bordered input-xs w-full max-w-xs" min="0" v-model="cholesterol"
                                label="Colesterol" type="number" />
                        </div>
                    </article>

                    <article id="group2" class="flex flex-col justify-between gap-2 ">
                        <div class="flex gap-2">
                            <label>Presión Arterial</label>
                            <input class="input input-bordered input-xs w-full max-w-xs" min="0" v-model="bloodPressure"
                                label="Presión Arterial" type="number" />
                        </div>
                        <div class="flex gap-2">
                            <label>Frecuencia Cardíaca</label>
                            <input class="input input-bordered input-xs w-full max-w-xs" min="0" v-model="heartRate"
                                label="Frecuencia Cardíaca" type="number" />
                        </div>
                        <div class="flex gap-2">
                            <label>Fumador</label>
                            <select class="select select-xs w-full max-w-xs" v-model="smoking" label="Fumador">
                                <option value=0>Nunca</option>
                                <option value=1>Anteriormente</option>
                                <option value=2>Actualmente</option>
                            </select>
                        </div>
                    </article>
                </div>

                <div id="groups3+4" class="flex flex-col justify-between items-center gap-4">

                    <article id="group3" class="flex flex-col justify-between gap-2 ">
                        <div class="flex gap-2">
                            <label for="">Consumo de alcohol</label>
                            <select class="select select-xs w-full max-w-xs" v-model="alcoholIntake"
                                label="Consumo de Alcohol">
                                <option value=0>Ninguno</option>
                                <option value=1>Moderado</option>
                                <option value=2>A menudo</option>
                            </select>
                        </div>
                        <div class="flex gap-2">
                            <label>Horas de Ejercicio</label>
                            <input class="input input-bordered input-xs w-full max-w-xs" min="0" v-model="exerciseHours"
                                label="Horas de Ejercicio" type="number" />
                        </div>
                        <div class="flex gap-2">
                            <label>Historial Familiar</label>
                            <select class="select select-xs w-full max-w-xs" v-model="familyHistory"
                                label="Historial Familiar">
                                <option value=0>No</option>
                                <option value=1>Sí</option>
                            </select>
                        </div>
                    </article>

                    <article id="group4" class="flex flex-col justify-between gap-2 ">
                        <div class="flex gap-2">
                            <label>Diabetes</label>
                            <select class="select select-xs w-full max-w-xs" v-model="diabetes" label="Diabetes"
                            >
                                <option value=0>No</option>
                                <option value=1>Sí</option>
                            </select>
                        </div>
                        <div class="flex gap-2">
                            <label>Obesidad</label>
                            <select class="select select-xs w-full max-w-xs" v-model="obesity" label="Obesidad"
                            >
                                <option value=0>No</option>
                                <option value=1>Sí</option>
                            </select>
                        </div>
                        <div class="flex gap-2">
                            <label>Nivel de Estrés</label>
                            <input class="input input-bordered input-xs w-full max-w-xs" min="0" v-model="stressLevel"
                                label="Nivel de Estrés" type="number" />
                        </div>
                    </article>
                </div>

                <div id="groups5+5" class="flex flex-col justify-between items-center gap-4">

                    <article id="group5" class="flex flex-col justify-between gap-2 ">
                        <div class="flex gap-2">
                            <label>Nivel de Azúcar</label>
                            <input class="input input-bordered input-xs w-full max-w-xs" min="0" v-model="bloodSugar"
                                label="Azúcar en Sangre" type="number" />
                        </div>
                        <div class="flex gap-2">
                            <label>Angina Inducida</label>
                            <select class="select select-xs w-full max-w-xs" v-model="exerciseInducedAngina"
                                label="Angina Inducida por Ejercicio">
                                <option value=0>No</option>
                                <option value=1>Sí</option>
                            </select>
                        </div>
                        <div class="flex gap-2">
                            <label>Tipo de dolor</label>
                            <select class="select select-xs w-full max-w-xs" v-model="chestPainType"
                                label="Tipo de dolor en el pecho">
                                <option value=0>Angina típica</option>
                                <option value=1>Angina atípica</option>
                                <option value=2>Dolor no anginal</option>
                                <option value=3>Asintomático</option>
                            </select>
                        </div>
                    </article>
                </div>


            </section>
            <section class="flex flex-row justify-center items-center gap-4">
                <button class="bg-[#1d3461] text-[#b1e0e7]  border-[#6290c8] border-2 rounded-box p-2 font-medium"
                    type="submit">Predecir riesgo</button>
                <button class="bg-[#1d3461] text-[#b1e0e7]  border-[#6290c8] border-2 rounded-box p-2 font-medium"
                    @click="dataReset">Resetear datos</button>
            </section>

        </form>
        <div>
            <div class="flex flex-row items-center gap-3 mb-2">
                <p class="text-lg font-semibold">Riesgo predicho:</p>
                <p v-if="predictionResult" class="text-lg font-semibold">{{ predictionResult }}</p>
                <span class="text-lg font-semibold" v-if="predictionResult">%</span>
            </div>
            <div class="flex flex-col justify-center items-center text-xs">
                <span class="text-center">Datos introducidos:</span>
                <div class="flex flex-row justify-between gap-6">
                    <ul>
                        <li>Edad: {{ age }}</li>
                        <li>Género: {{ gender }}</li>
                        <li>Colesterol: {{ cholesterol }}</li>
                        <li>Presión Arterial: {{ bloodPressure }}</li>
                        <li>Frecuencia Cardíaca: {{ heartRate }}</li>
                        <li>Fumador: {{ smoking }}</li>
                        <li>Consumo de alcohol: {{ alcoholIntake }}</li>
                    </ul>
                    <ul>
                        <li>Horas de Ejercicio: {{ exerciseHours }}</li>
                        <li>Historial Familiar: {{ familyHistory }}</li>
                        <li>Diabetes: {{ diabetes }}</li>
                        <li>Obesidad: {{ obesity }}</li>
                        <li>Nivel de Estrés: {{ stressLevel }}</li>
                        <li>Azúcar en Sangre: {{ bloodSugar }}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>




</template>

<script setup>
import { inject, ref } from 'vue';

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
// let h = ref(null);
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
    
});

async function dataReset() {
    // age.value = null,
    // gender.value = null,
    // cholesterol.value = null,
    // bloodPressure.value = null,
    // heartRate.value = null,
    // smoking.value = null,
    // alcoholIntake.value = null,
    // exerciseHours.value = null,
    // familyHistory.value = null,
    // diabetes.value = null,
    // obesity.value = null,
    // stressLevel.value = null,
    // bloodSugar.value = null,
    // exerciseInducedAngina.value = null,
    // chestPainType.value = null,
    // heartDisease.value = null,
    // predictionResult.value = null;
    window.location.reload();
}

async function loadData() {
    const response = await fetch('heart_disease_dataset_trans.csv');
    const data = await response.text();
    const rows = data.split(/\r\n|\n/).slice(1);

    const processedRows = rows.map((row) => {
        const values = row.split(",");
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
            HeartDisease: values[15],
        };
    });

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

    inputTensor = tf.tensor2d(inputs);
    outputTensor = tf.tensor2d(outputs);

}

async function createModel() {
    model = tf.sequential();
    const hidden = tf.layers.dense({
        units: 10, 
        inputShape: [15],
        activation: "tanh",
    });

    model.add(hidden);

    const output = tf.layers.dense({
        units: 1,
        // inputShape: [10], 
        activation: "sigmoid",
    });

    model.add(output);

    await model.compile({
        optimizer: "sgd",
        loss: "binaryCrossentropy",
    });
}

async function trainModel(inputTensor, outputTensor) {
    if (!inputTensor || !outputTensor) {
        console.error(
            "trainModel: inputTensor or outputTensor is undefined or null",
        );
        return;
    }

    const numericInputTensor = tf.tensor2d(
        inputTensor.arraySync().map((row) => convertToNumeric(row)),
    );
    const numericOutputTensor = tf.tensor2d(
        outputTensor.arraySync().map((row) => convertToNumeric(row)),
    );

    const configTrain = {
        epochs: 30,
        shuffle: true,
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

    const inputTensor = tf.tensor2d([inputArray]);

    let prediction = await model.predict(inputTensor);
    prediction.print(); 

    const predictionValue = (prediction.arraySync()[0][0] * 100).toFixed(0);
    // console.log(predictionValue);

    predictionResult.value = predictionValue;
}


</script>

<style scoped>
label {
    width: 250px;
}
</style>