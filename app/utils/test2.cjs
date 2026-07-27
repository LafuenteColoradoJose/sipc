const fs = require('fs');
const buffer = fs.readFileSync('/home/pp/Escritorio/Proyectos/sipc/public/model/tfjs_model/group1-shard1of1.bin');
const float32Array = new Float32Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / 4);

const w1 = float32Array.slice(0, 960);
const b1 = float32Array.slice(960, 1024);
const w2 = float32Array.slice(1024, 1088);
const b2 = float32Array.slice(1088, 1089);

// inputData from the user's screenshot: age: 57, gender: 0, cholesterol: 0, bloodPressure: 0, heartRate: 75, smoking: 1, alcoholIntake: 1, exerciseHours: 8, familyHistory: 1, diabetes: 1
const inputs = [57, 0, 0, 0, 75, 1, 1, 8, 1, 1, 0, 0, 0, 0, 0];

const hidden = new Float32Array(64);
for (let i = 0; i < 64; i++) {
    let sum = b1[i];
    for (let j = 0; j < 15; j++) {
        sum += inputs[j] * w1[j * 64 + i];
    }
    hidden[i] = Math.max(0, sum);
}

let out = b2[0];
for (let i = 0; i < 64; i++) {
    out += hidden[i] * w2[i];
}
const prediction = 1 / (1 + Math.exp(-out));
console.log("Prediction:", prediction);
