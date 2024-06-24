<template>
    <div :class="{ 'theme-dark': theme === 'dark', 'theme-light': theme === 'light' }">
        <!-- <form @submit.prevent="predict" class="flex flex-wrap justify-between items-center m-2 gap-4">
            <div>
                <label for="age" class="block text-sm font-medium text-gray-700">Edad</label>
                <input type="number" id="age" v-model="age" class="input input-bordered">
            </div>
            <div>
                <label for="gender" class="block text-sm font-medium text-gray-700">Género</label>
                <select id="gender" v-model="gender" class="select select-bordered">
                    <option value="Male">Masculino</option>
                    <option value="Female">Femenino</option>
                </select>
            </div>
            <div>
                <label for="cholesterol" class="block text-sm font-medium text-gray-700">Colesterol</label>
                <input type="number" id="cholesterol" v-model="cholesterol" class="input input-bordered">
            </div>
            <div>
                <label for="bloodPressure" class="block text-sm font-medium text-gray-700">Presión Arterial</label>
                <input type="number" id="bloodPressure" v-model="bloodPressure" class="input input-bordered">
            </div>
            <div>
                <label for="heartRate" class="block text-sm font-medium text-gray-700">Frecuencia Cardíaca</label>
                <input type="number" id="heartRate" v-model="heartRate" class="input input-bordered">
            </div>
            <div>
                <label for="smoking" class="block text-sm font-medium text-gray-700">Fumador</label>
                <select id="smoking" v-model="smoking" class="select select-bordered">
                    <option value="Never">Nunca</option>
                    <option value="Former">Anteriormente</option>
                    <option value="Current">Actualmente</option>
                </select>
            </div>
            <div>
                <label for="alcoholIntake" class="block text-sm font-medium text-gray-700">Consumo de Alcohol</label>
                <select id="alcoholIntake" v-model="alcoholIntake" class="select select-bordered">
                    <option value="None">Ninguno</option>
                    <option value="Moderate">Moderado</option>
                    <option value="Heavy">Pesado</option>
                </select>
            </div>
            <div>
                <label for="exerciseHours" class="block text-sm font-medium text-gray-700">Horas de Ejercicio</label>
                <input type="number" id="exerciseHours" v-model="exerciseHours" class="input input-bordered">
            </div>
            <div>
                <label for="familyHistory" class="block text-sm font-medium text-gray-700">Historial Familiar</label>
                <select id="familyHistory" v-model="familyHistory" class="select select-bordered">
                    <option value="Yes">Sí</option>
                    <option value="No">No</option>
                </select>
            </div>
            <div>
                <label for="diabetes" class="block text-sm font-medium text-gray-700">Diabetes</label>
                <select id="diabetes" v-model="diabetes" class="select select-bordered">
                    <option value="Yes">Sí</option>
                    <option value="No">No</option>
                </select>
            </div>
            <div>
                <label for="obesity" class="block text-sm font-medium text-gray-700">Obesidad</label>
                <select id="obesity" v-model="obesity" class="select select-bordered">
                    <option value="Yes">Sí</option>
                    <option value="No">No</option>
                </select>
            </div>
            <div>
                <label for="stressLevel" class="block text-sm font-medium text-gray-700">Nivel de Estrés</label>
                <input type="number" id="stressLevel" v-model="stressLevel" class="input input-bordered">
            </div>
            <div>
                <label for="bloodSugar" class="block text-sm font-medium text-gray-700">Azúcar en Sangre</label>
                <input type="number" id="bloodSugar" v-model="bloodSugar" class="input input-bordered">
            </div>
            <div>
                <label for="exerciseInducedAngina" class="block text-sm font-medium text-gray-700">Angina Inducida por
                    Ejercicio</label>
                <select id="exerciseInducedAngina" v-model="exerciseInducedAngina" class="select select-bordered">
                    <option value="Yes">Sí</option>
                    <option value="No">No</option>
                </select>
            </div>
            <div>
                <label for="chestPainType" class="block text-sm font-medium text-gray-700">Tipo de Dolor de
                    Pecho</label>
                <select id="chestPainType" v-model="chestPainType" class="select select-bordered">
                    <option value="Typical Angina">Angina Típica</option>
                    <option value="Atypical Angina">Angina Atípica</option>
                    <option value="Non-anginal Pain">Dolor No Anginal</option>
                    <option value="Asymptomatic">Asintomático</option>
                </select>
            </div>
            <div>
                <label for="heartDisease" class="block text-sm font-medium text-gray-700">Enfermedad Cardíaca</label>
                <select id="heartDisease" v-model="heartDisease" class="select select-bordered">
                    <option value="0">No</option>
                    <option value="1">Sí</option>
                </select>
            </div>
            <div class="flex justify-center mt-8">
                <button type="submit" class="btn btn-neutral">Enviar</button>
            </div>
        </form> -->



        <!-- <div class="mt-8">
            <label class="text-2xl font-semibold">Resultado</label>
            <p>Probabilidad de enfermedad cardíaca: {{ heartDisease }}</p>
        </div> -->

        <div>
            <h1>Predicción del riesgo de enfermedades cardíacas</h1>
            <form @submit.prevent="predictHeartDisease" class="flex flex-wrap justify-between items-center m-2 gap-4">
                <div class="flex gap-2">
                    <label>Edad</label>
                    <input v-model="age" label="Edad" type="number" />
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
                    <input v-model="cholesterol" label="Colesterol" type="number" />
                </div>
                <div class="flex gap-2">
                    <label>Presión Arterial</label>
                    <input v-model="bloodPressure" label="Presión Arterial" type="number" />
                </div>
                <div class="flex gap-2">
                    <label>Frecuencia Cardíaca</label>
                    <input v-model="heartRate" label="Frecuencia Cardíaca" type="number" />
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
                    <input v-model="exerciseHours" label="Horas de Ejercicio" type="number" />
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
                    <input v-model="stressLevel" label="Nivel de Estrés" type="number" />
                </div>
                <div class="flex gap-2">
                    <label>Azúcar en Sangre</label>
                    <input v-model="bloodSugar" label="Azúcar en Sangre" type="number" />
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
                <button type="submit">Predecir riesgo</button>
            </form>
            <p v-if="predictionResult">Riesgo predicho: {{ predictionResult }}</p>
        </div>

    </div>
</template>

<script setup>
import * as tf from '@tensorflow/tfjs';
import Papa from 'papaparse';
import { inject, ref } from 'vue';

const theme = inject('theme');
const inpust = ref(null);
const outputs = ref(null);
const xs = ref(null);
const ys = ref(null);

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
    await createModel();
    predictionResult.value = prediction.dataSync()[0];

}

onMounted(() => {
    loadData();
});

async function loadData() {
    const response = await fetch('heart_disease_dataset.csv');
    const data = await response.text();
    const rows = data.split(/\r\n|\n/).slice(1);

    // Mapeos
    const genderMapping = { Male: 0, Female: 1 };
    const smokingMapping = { Never: 0, Former: 1, Current: 2 };
    const alcoholIntakeMapping = { None: 0, Moderate: 1, Heavy: 2 };
    const familyHistoryMapping = { No: 0, Yes: 1 };
    const diabetesMapping = { No: 0, Yes: 1 };
    const obesityMapping = { No: 0, Yes: 1 };
    const exerciseInducedAnginaMapping = { No: 0, Yes: 1 };
    const chestPainTypeMapping = { 'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3 };

    // Definiciones de los índices de las columnas basadas en tu tabla
    const genderIndex = 1;
    const smokingIndex = 5;
    const alcoholIntakeIndex = 6;
    const familyHistoryIndex = 8;
    const diabetesIndex = 9;
    const obesityIndex = 10;
    const exerciseInducedAnginaIndex = 13;
    const chestPainTypeIndex = 14;

    const processedData = rows.map(row => {
        const items = row.split(',');
        items[genderIndex] = genderMapping[items[genderIndex]];
        items[smokingIndex] = smokingMapping[items[smokingIndex]];
        items[alcoholIntakeIndex] = alcoholIntakeMapping[items[alcoholIntakeIndex]];
        items[familyHistoryIndex] = familyHistoryMapping[items[familyHistoryIndex]];
        items[diabetesIndex] = diabetesMapping[items[diabetesIndex]];
        items[obesityIndex] = obesityMapping[items[obesityIndex]];
        items[exerciseInducedAnginaIndex] = exerciseInducedAnginaMapping[items[exerciseInducedAnginaIndex]];
        items[chestPainTypeIndex] = chestPainTypeMapping[items[chestPainTypeIndex]];

        // Convertir el resto de los elementos a números si es posible
        return items.map((item, index) => {
            if ([genderIndex, smokingIndex, alcoholIntakeIndex, familyHistoryIndex, diabetesIndex, obesityIndex, exerciseInducedAnginaIndex, chestPainTypeIndex].includes(index)) {
                return item; // Estos ya han sido convertidos a sus valores mapeados
            }
            return isNaN(Number(item)) ? item : Number(item);
        });
    });

    /// Separar en características (xs) y etiquetas (ys)
    xs.value = processedData.map(row => row.slice(0, -1)); // Todas menos la última columna
    ys.value = processedData.map(row => row.slice(-1)); // Solo la última columna

    // console.log(xs.value);
    // console.log(ys.value);

    // Convertir a tensores
    inpust.value = tf.tensor2d(xs.value);
    outputs.value = tf.tensor2d(ys.value);

}

async function createModel() {

    const model = tf.sequential();

    const hidden = tf.layers.dense({
        units: 10,
        inputShape: [15],
        activation: 'tanh'
    });

    model.add(hidden);

    const output = tf.layers.dense({
        units: 1,
        inputShape: [10],
        activation: 'tanh'
    });

    model.add(output);

    model.compile({
        optimizer: 'sgd',
        loss: 'meanSquaredError'
    });

    const configTrain = {
        epochs: 100,
        shuffle: true
    }

    h = await model.fit(inpust.value, outputs.value, configTrain);
    console.log(h.history.loss[h.history.loss.length - 1]);

    let prediction = model.predict(tf.tensor2d([
        [age.value],
        [cholesterol.value],
        [bloodPressure.value],
        [heartRate.value],
        [smoking.value],
        [alcoholIntake.value],
        [exerciseHours.value],
        [familyHistory.value],
        [diabetes.value],
        [obesity.value],
        [stressLevel.value],
        [bloodSugar.value],
        [exerciseInducedAngina.value],
        [chestPainType.value],

    ]));

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