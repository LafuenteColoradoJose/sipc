<template>
    <div class="container">
      <h1>Heart Disease Prediction</h1>
      <form @submit.prevent="predict">
        <div v-for="(feature, index) in features" :key="index" class="form-group">
          <label :for="feature">{{ feature }}</label>
          <input v-model="form[feature]" :id="feature" type="text" required />
        </div>
        <button type="submit">Predict</button>
      </form>
      <div v-if="prediction !== null">
        <h2>Prediction: {{ prediction }}</h2>
      </div>
    </div>
  </template>
  
  <script setup>
import { ref, onMounted } from 'vue';
import * as tf from '@tensorflow/tfjs';

const features = [
  'Age', 'Gender', 'Cholesterol', 'Blood Pressure', 'Heart Rate', 
  'Smoking', 'Alcohol Intake', 'Exercise Hours', 'Family History', 
  'Diabetes', 'Obesity', 'Stress Level', 'Blood Sugar', 
  'Exercise Induced Angina', 'Chest Pain Type'
];

const form = ref({
  Age: '', Gender: '', Cholesterol: '', 'Blood Pressure': '', 'Heart Rate': '', 
  Smoking: '', 'Alcohol Intake': '', 'Exercise Hours': '', 'Family History': '', 
  Diabetes: '', Obesity: '', 'Stress Level': '', 'Blood Sugar': '', 
  'Exercise Induced Angina': '', 'Chest Pain Type': ''
});

const model = ref(null);
const prediction = ref(null);

onMounted(async () => {
  model.value = await tf.loadLayersModel('/model/model.json');
});

async function predict() {
  // Lógica de predicción aquí
}
</script>
  
  <style>
  .container {
    width: 50%;
    margin: auto;
    padding: 50px 0;
  }
  .form-group {
    margin-bottom: 15px;
  }
  label {
    display: block;
    margin-bottom: 5px;
  }
  input, button {
    width: 100%;
    padding: 10px;
    margin: 5px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  button {
    background: #5cb85c;
    color: #fff;
    cursor: pointer;
  }
  button:hover {
    background: #4cae4c;
  }
  </style>