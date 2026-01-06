<template>

    <div>
        <h1>Predicción del riesgo de enfermedades cardíacas</h1>
        <form @submit.prevent="predictHeartDisease" class="flex flex-col justify-between items-center m-2 gap-4 ">
            <section class="grid grid-cols-1 m-2 gap-6 md:grid-cols-2 lg:grid-cols-3">

                <div id="groups1+2" class="flex flex-col justify-between items-center gap-4 w-full">

                    <article id="group1" class="flex flex-col justify-between gap-4 w-full">
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Edad</span></label>
                            <input class="input input-bordered w-full" min="0" v-model="age" type="number"
                                placeholder="Ej: 45" />
                        </div>
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Género</span></label>
                            <select class="select select-bordered w-full" v-model="gender">
                                <option value=0>Masculino</option>
                                <option value=1>Femenino</option>
                            </select>
                        </div>
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Colesterol</span></label>
                            <input class="input input-bordered w-full" min="0" v-model="cholesterol" type="number"
                                placeholder="Ej: 200" />
                        </div>
                    </article>

                    <article id="group2" class="flex flex-col justify-between gap-4 w-full">
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Presión Arterial</span></label>
                            <input class="input input-bordered w-full" min="0" v-model="bloodPressure" type="number"
                                placeholder="Ej: 120" />
                        </div>
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Frecuencia Cardíaca</span></label>
                            <input class="input input-bordered w-full" min="0" v-model="heartRate" type="number"
                                placeholder="Ej: 75" />
                        </div>
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Fumador</span></label>
                            <select class="select select-bordered w-full" v-model="smoking">
                                <option value=0>Nunca</option>
                                <option value=1>Anteriormente</option>
                                <option value=2>Actualmente</option>
                            </select>
                        </div>
                    </article>
                </div>

                <div id="groups3+4" class="flex flex-col justify-between items-center gap-4 w-full">

                    <article id="group3" class="flex flex-col justify-between gap-4 w-full">
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Consumo de alcohol</span></label>
                            <select class="select select-bordered w-full" v-model="alcoholIntake">
                                <option value=0>Ninguno</option>
                                <option value=1>Moderado</option>
                                <option value=2>A menudo</option>
                            </select>
                        </div>
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Horas de Ejercicio</span></label>
                            <input class="input input-bordered w-full" min="0" v-model="exerciseHours" type="number"
                                placeholder="Ej: 5" />
                        </div>
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Historial Familiar</span></label>
                            <select class="select select-bordered w-full" v-model="familyHistory">
                                <option value=0>No</option>
                                <option value=1>Sí</option>
                            </select>
                        </div>
                    </article>

                    <article id="group4" class="flex flex-col justify-between gap-4 w-full">
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Diabetes</span></label>
                            <select class="select select-bordered w-full" v-model="diabetes">
                                <option value=0>No</option>
                                <option value=1>Sí</option>
                            </select>
                        </div>
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Obesidad</span></label>
                            <select class="select select-bordered w-full" v-model="obesity">
                                <option value=0>No</option>
                                <option value=1>Sí</option>
                            </select>
                        </div>
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Nivel de Estrés</span></label>
                            <input class="input input-bordered w-full" min="0" v-model="stressLevel" type="number"
                                placeholder="1-10" />
                        </div>
                    </article>
                </div>

                <div id="groups5+5" class="flex flex-col justify-between items-center gap-4 w-full">

                    <article id="group5" class="flex flex-col justify-between gap-4 w-full">
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Nivel de Azúcar</span></label>
                            <input class="input input-bordered w-full" min="0" v-model="bloodSugar" type="number" />
                        </div>
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Angina Inducida</span></label>
                            <select class="select select-bordered w-full" v-model="exerciseInducedAngina">
                                <option value=0>No</option>
                                <option value=1>Sí</option>
                            </select>
                        </div>
                        <div class="flex flex-col w-full">
                            <label class="label"><span class="label-text">Tipo de dolor</span></label>
                            <select class="select select-bordered w-full" v-model="chestPainType">
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
import { inject, ref, onMounted } from 'vue';

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
            defer: true,
        },
    ],
});

const theme = useState('theme');

// No need for these to be reactive refs as they hold complex TF objects
let inputTensor = null;
let outputTensor = null;
let model = null;

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
const predictionResult = ref(null);

async function predictHeartDisease() {
    if (!model) {
        console.error("Model not trained yet");
        return;
    }
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

// Function to wait for tf to be loaded
async function waitForTf() {
    return new Promise((resolve) => {
        if (window.tf) {
            resolve(window.tf);
        } else {
            const checkTf = setInterval(() => {
                if (window.tf) {
                    clearInterval(checkTf);
                    resolve(window.tf);
                }
            }, 100);
        }
    });
}

onMounted(async () => {
    try {
        await waitForTf();
        await loadData(); // Wait for data to load
        await createModel();
        // Check if tensors are valid before training
        if (inputTensor && outputTensor) {
            await trainModel();
        } else {
            console.error("Data loading failed, cannot train model");
        }
    } catch (error) {
        console.error("Initialization error:", error);
    }
});

function dataReset() {
    window.location.reload();
}

async function loadData() {
    try {
        const response = await fetch('/heart_disease_dataset_trans.csv');
        if (!response.ok) throw new Error("Failed to load CSV data");

        const data = await response.text();
        const rows = data.split(/\r\n|\n/).slice(1);

        const processedRows = rows.map((row) => {
            const values = row.split(",");
            if (values.length < 16) return null; // Skip invalid rows
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
        }).filter(r => r !== null);

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

        if (inputs.length === 0 || outputs.length === 0) {
            console.error("No valid data found in CSV");
            return;
        }

        inputTensor = tf.tensor2d(inputs);
        outputTensor = tf.tensor2d(outputs);
    } catch (e) {
        console.error("Error loading data:", e);
    }
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
        activation: "sigmoid",
    });

    model.add(output);

    await model.compile({
        optimizer: "sgd",
        loss: "binaryCrossentropy",
    });
}

async function trainModel() {
    if (!inputTensor || !outputTensor) {
        console.error("trainModel: inputTensor or outputTensor is undefined or null");
        return;
    }

    // Direct usage since they are already numbers
    // Note: If you really wanted to create new tensors, you can, but typically you fit directly on existing tensors
    // However, keeping closer to original logic without the missing function:
    const numericInputTensor = inputTensor;
    const numericOutputTensor = outputTensor;

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

    const inputTensorPred = tf.tensor2d([inputArray]);

    let prediction = await model.predict(inputTensorPred);
    prediction.print();

    const predictionValue = (prediction.arraySync()[0][0] * 100).toFixed(0);
    predictionResult.value = predictionValue;
}
</script>




<style scoped>
/* Removed fixed width label to improve responsiveness */
</style>