<template>
    <div :class="{'theme-dark': theme === 'dark', 'theme-light': theme === 'light'}" >
        <form class="space-y-4">
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
                <label for="exerciseInducedAngina" class="block text-sm font-medium text-gray-700">Angina Inducida por Ejercicio</label>
                <select id="exerciseInducedAngina" v-model="exerciseInducedAngina" class="select select-bordered">
                    <option value="Yes">Sí</option>
                    <option value="No">No</option>
                </select>
            </div>
            <div>
                <label for="chestPainType" class="block text-sm font-medium text-gray-700">Tipo de Dolor de Pecho</label>
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
            <button type="submit" class="btn btn-neutral">Enviar</button>
        </form>
    </div>
</template>

<script setup>
import { ref, inject } from 'vue';

const theme = inject('theme');

const age = ref(0);
const gender = ref('');
const cholesterol = ref(0);
const bloodPressure = ref(0);
const heartRate = ref(0);
const smoking = ref('');
const alcoholIntake = ref('');
const exerciseHours = ref(0);
const familyHistory = ref('');
const diabetes = ref('');
const obesity = ref('');
const stressLevel = ref(0);
const bloodSugar = ref(0);
const exerciseInducedAngina = ref('');
const chestPainType = ref('');
const heartDisease = ref('');


</script>

<style scoped>
.theme-dark label {
  color: #b1e0e7;
}

.theme-light label {
  color: #007ea8;
}


</style>