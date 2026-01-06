<template>
    <div class="w-full max-w-6xl mx-auto px-4 pb-12">
        <h1
            class="text-3xl md:text-5xl font-bold text-center mb-10 text-[var(--color-primary)] dark:text-[var(--color-primary-dark)]">
            Predicción de Riesgo Cardiovascular</h1>

        <form @submit.prevent="predictHeartDisease" class="flex flex-col gap-8">
            <!-- Main Grid Layout -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

                <!-- Section 1: Datos Personales -->
                <section
                    class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg border border-gray-100 dark:border-gray-700 transition-all hover:shadow-xl">
                    <h2 class="text-xl font-semibold mb-6 flex items-center gap-2 text-gray-700 dark:text-gray-200">
                        <Icon name="uil:user" class="w-6 h-6 text-[var(--color-primary)]" />
                        Datos Personales
                    </h2>

                    <div class="space-y-6">
                        <div class="form-control">
                            <label class="label"><span class="label-text">Edad (años)</span></label>
                            <input class="input" min="0" max="120" v-model="age" type="number" placeholder="Ej: 45" />
                        </div>

                        <div class="form-control">
                            <label class="label"><span class="label-text">Género</span></label>
                            <div class="flex bg-gray-100 dark:bg-gray-700 p-1 rounded-lg">
                                <button type="button" @click="gender = 0"
                                    class="flex-1 py-2 rounded-md transition-all text-sm font-medium"
                                    :class="gender === 0 ? 'bg-white text-[var(--color-primary)] shadow-sm dark:bg-gray-600 dark:text-white' : 'text-gray-500 hover:text-gray-700 dark:text-gray-400'">
                                    Masculino
                                </button>
                                <button type="button" @click="gender = 1"
                                    class="flex-1 py-2 rounded-md transition-all text-sm font-medium"
                                    :class="gender === 1 ? 'bg-white text-[var(--color-primary)] shadow-sm dark:bg-gray-600 dark:text-white' : 'text-gray-500 hover:text-gray-700 dark:text-gray-400'">
                                    Femenino
                                </button>
                            </div>
                        </div>

                        <div class="form-control">
                            <label class="label"><span class="label-text">Historial Familiar</span></label>
                            <div class="flex gap-4">
                                <label
                                    class="flex items-center gap-2 cursor-pointer p-3 border rounded-lg flex-1 transition-colors"
                                    :class="familyHistory === 1 ? 'border-[var(--color-primary)] bg-red-50 dark:bg-red-900/10' : 'border-gray-200 dark:border-gray-600'">
                                    <input type="radio" :value="1" v-model="familyHistory"
                                        class="text-[var(--color-primary)] focus:ring-[var(--color-primary)]" />
                                    <span class="text-sm">Sí</span>
                                </label>
                                <label
                                    class="flex items-center gap-2 cursor-pointer p-3 border rounded-lg flex-1 transition-colors"
                                    :class="familyHistory === 0 ? 'border-green-500 bg-green-50 dark:bg-green-900/10' : 'border-gray-200 dark:border-gray-600'">
                                    <input type="radio" :value="0" v-model="familyHistory"
                                        class="text-green-600 focus:ring-green-500" />
                                    <span class="text-sm">No</span>
                                </label>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Section 2: Estilo de Vida -->
                <section
                    class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg border border-gray-100 dark:border-gray-700 transition-all hover:shadow-xl">
                    <h2 class="text-xl font-semibold mb-6 flex items-center gap-2 text-gray-700 dark:text-gray-200">
                        <Icon name="uil:heart-medical" class="w-6 h-6 text-[var(--color-primary)]" />
                        Estilo de Vida
                    </h2>

                    <div class="space-y-6">
                        <div class="form-control">
                            <label class="label"><span class="label-text">Fumador</span></label>
                            <select class="select" v-model="smoking">
                                <option :value="0">Nunca</option>
                                <option :value="1">Anteriormente</option>
                                <option :value="2">Actualmente</option>
                            </select>
                        </div>

                        <div class="form-control">
                            <label class="label"><span class="label-text">Consumo de Alcohol</span></label>
                            <div class="grid grid-cols-3 gap-2">
                                <button type="button" @click="alcoholIntake = 0"
                                    class="py-2 px-1 rounded-lg border text-xs font-medium transition-all"
                                    :class="alcoholIntake === 0 ? 'border-green-500 bg-green-50 text-green-700 dark:bg-green-900/20 dark:text-green-300' : 'border-gray-200 text-gray-500 dark:border-gray-600'">
                                    Ninguno
                                </button>
                                <button type="button" @click="alcoholIntake = 1"
                                    class="py-2 px-1 rounded-lg border text-xs font-medium transition-all"
                                    :class="alcoholIntake === 1 ? 'border-yellow-500 bg-yellow-50 text-yellow-700 dark:bg-yellow-900/20 dark:text-yellow-300' : 'border-gray-200 text-gray-500 dark:border-gray-600'">
                                    Moderado
                                </button>
                                <button type="button" @click="alcoholIntake = 2"
                                    class="py-2 px-1 rounded-lg border text-xs font-medium transition-all"
                                    :class="alcoholIntake === 2 ? 'border-red-500 bg-red-50 text-red-700 dark:bg-red-900/20 dark:text-red-300' : 'border-gray-200 text-gray-500 dark:border-gray-600'">
                                    Alto
                                </button>
                            </div>
                        </div>

                        <div class="form-control">
                            <label class="label flex justify-between">
                                <span class="label-text">Horas Ejercicio/Semana</span>
                                <span class="text-xs font-bold text-[var(--color-primary)]">{{ exerciseHours || 0
                                }}h</span>
                            </label>
                            <input type="range" min="0" max="20" v-model="exerciseHours"
                                class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700 accent-[var(--color-primary)]" />
                        </div>

                        <div class="form-control">
                            <label class="label flex justify-between">
                                <span class="label-text">Nivel de Estrés (1-10)</span>
                                <span class="text-xs font-bold text-[var(--color-primary)]">{{ stressLevel || 1
                                }}</span>
                            </label>
                            <input type="range" min="1" max="10" v-model="stressLevel"
                                class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700 accent-[var(--color-primary)]" />
                        </div>
                    </div>
                </section>

                <!-- Section 3: Métricas Clínicas -->
                <section
                    class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg border border-gray-100 dark:border-gray-700 transition-all hover:shadow-xl md:col-span-2 lg:col-span-1">
                    <h2 class="text-xl font-semibold mb-6 flex items-center gap-2 text-gray-700 dark:text-gray-200">
                        <Icon name="uil:stethoscope" class="w-6 h-6 text-[var(--color-primary)]" />
                        Métricas Clínicas
                    </h2>

                    <div class="space-y-4">
                        <div class="grid grid-cols-2 gap-4">
                            <div class="form-control">
                                <label class="label"><span class="label-text text-xs">Colesterol</span></label>
                                <input class="input text-sm" type="number" v-model="cholesterol" placeholder="mg/dL" />
                            </div>
                            <div class="form-control">
                                <label class="label"><span class="label-text text-xs">Presión Art.</span></label>
                                <input class="input text-sm" type="number" v-model="bloodPressure" placeholder="mmHg" />
                            </div>
                        </div>

                        <div class="grid grid-cols-2 gap-4">
                            <div class="form-control">
                                <label class="label"><span class="label-text text-xs">Frec. Cardíaca</span></label>
                                <input class="input text-sm" type="number" v-model="heartRate" placeholder="bpm" />
                            </div>
                            <div class="form-control">
                                <label class="label"><span class="label-text text-xs">Azúcar</span></label>
                                <input class="input text-sm" type="number" v-model="bloodSugar" placeholder="mg/dL" />
                            </div>
                        </div>

                        <!-- Toggles Grid -->
                        <div class="grid grid-cols-2 gap-4 pt-2">
                            <div class="form-control">
                                <label class="label"><span class="label-text text-xs">Diabetes</span></label>
                                <button type="button" @click="diabetes = diabetes === 1 ? 0 : 1"
                                    class="w-full py-2 rounded-lg border transition-all text-xs font-semibold"
                                    :class="diabetes === 1 ? 'border-[var(--color-primary)] bg-red-50 text-[var(--color-primary)] dark:bg-red-900/20' : 'border-gray-200 text-gray-500 hover:border-gray-300 dark:border-gray-600'">
                                    {{ diabetes === 1 ? 'Sí' : 'No' }}
                                </button>
                            </div>
                            <div class="form-control">
                                <label class="label"><span class="label-text text-xs">Obesidad</span></label>
                                <button type="button" @click="obesity = obesity === 1 ? 0 : 1"
                                    class="w-full py-2 rounded-lg border transition-all text-xs font-semibold"
                                    :class="obesity === 1 ? 'border-[var(--color-primary)] bg-red-50 text-[var(--color-primary)] dark:bg-red-900/20' : 'border-gray-200 text-gray-500 hover:border-gray-300 dark:border-gray-600'">
                                    {{ obesity === 1 ? 'Sí' : 'No' }}
                                </button>
                            </div>
                        </div>

                        <div class="form-control">
                            <label class="label"><span class="label-text text-xs">Angina Inducida</span></label>
                            <button type="button" @click="exerciseInducedAngina = exerciseInducedAngina === 1 ? 0 : 1"
                                class="w-full py-2 rounded-lg border transition-all text-xs font-semibold"
                                :class="exerciseInducedAngina === 1 ? 'border-[var(--color-primary)] bg-red-50 text-[var(--color-primary)] dark:bg-red-900/20' : 'border-gray-200 text-gray-500 hover:border-gray-300 dark:border-gray-600'">
                                {{ exerciseInducedAngina === 1 ? 'Sí, inducida' : 'No detectada' }}
                            </button>
                        </div>

                        <div class="form-control">
                            <label class="label"><span class="label-text text-xs">Tipo de Dolor</span></label>
                            <select class="select text-sm h-10 py-0" v-model="chestPainType">
                                <option :value="0">Típica</option>
                                <option :value="1">Atípica</option>
                                <option :value="2">No anginal</option>
                                <option :value="3">Asintomático</option>
                            </select>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Actions -->
            <div class="flex flex-col-reverse md:flex-row justify-center items-center gap-6 mt-8">
                <button type="button" @click="dataReset"
                    class="px-8 py-3 rounded-full border-2 border-slate-300 text-slate-500 font-semibold hover:border-slate-400 hover:text-slate-600 transition-all focus:outline-none focus:ring-2 focus:ring-slate-200 dark:border-slate-600 dark:text-slate-400">
                    Resetear formulario
                </button>
                <button type="submit"
                    class="px-12 py-3 rounded-full bg-[var(--color-primary)] text-white font-bold text-lg shadow-lg shadow-red-500/30 hover:shadow-red-500/50 hover:scale-105 transition-all focus:outline-none focus:ring-4 focus:ring-red-500/20 active:scale-95">
                    Calcular Riesgo
                </button>
            </div>
        </form>

        <!-- Result Feedback (Modal Overlay or Fixed Bottom) -->
        <transition enter-active-class="transition duration-300 ease-out"
            enter-from-class="transform scale-95 opacity-0" enter-to-class="transform scale-100 opacity-100"
            leave-active-class="transition duration-200 ease-in" leave-from-class="transform scale-100 opacity-100"
            leave-to-class="transform scale-95 opacity-0">
            <div v-if="predictionResult"
                class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
                @click="predictionResult = null">
                <div class="bg-white dark:bg-gray-800 p-8 rounded-3xl shadow-2xl max-w-md w-full text-center relative border border-gray-100 dark:border-gray-700"
                    @click.stop>
                    <button @click="predictionResult = null"
                        class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
                        <Icon name="mdi:close" class="w-6 h-6" />
                    </button>

                    <div class="mb-4 inline-flex items-center justify-center w-24 h-24 rounded-full"
                        :class="predictionResult > 50 ? 'bg-red-100 text-red-500' : 'bg-green-100 text-green-500'">
                        <Icon name="uil:heart-rate" class="w-12 h-12" />
                    </div>

                    <h3 class="text-2xl font-bold mb-2 text-gray-800 dark:text-white">Resultado del Análisis</h3>
                    <p class="text-gray-500 dark:text-gray-400 mb-6">Basado en sus métricas clínicas y estilo de vida.
                    </p>

                    <div class="text-6xl font-black mb-2"
                        :class="predictionResult > 50 ? 'text-[var(--color-primary)]' : 'text-green-500'">
                        {{ predictionResult }}<span class="text-3xl">%</span>
                    </div>

                    <p class="font-medium text-lg mb-8"
                        :class="predictionResult > 50 ? 'text-red-600' : 'text-green-600'">
                        {{ predictionResult > 50 ? 'Riesgo Elevado Detectado' : 'Riesgo Bajo' }}
                    </p>

                    <button @click="predictionResult = null"
                        class="w-full py-3 bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-white rounded-xl font-semibold transition-colors">
                        Entendido
                    </button>
                </div>
            </div>
        </transition>
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