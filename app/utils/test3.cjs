const fs = require('fs');
const buffer = fs.readFileSync('/home/pp/Escritorio/Proyectos/sipc/public/model/tfjs_model/group1-shard1of1.bin');
const float32Array = new Float32Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / 4);

const w1 = float32Array.slice(0, 960);
const b1 = float32Array.slice(960, 1024);
const w2 = float32Array.slice(1024, 1088);
const b2 = float32Array.slice(1088, 1089);

// User's exact input from screenshot 2
const inputs = [
    80,   // age
    0,    // gender
    270,  // cholesterol
    120,  // bloodPressure
    75,   // heartRate
    1,    // smoking
    1,    // alcoholIntake
    7,    // exerciseHours
    1,    // familyHistory
    0,    // diabetes (null -> 0)
    1,    // obesity
    2,    // stressLevel
    0,    // bloodSugar (null -> 0)
    0,    // exerciseInducedAngina (null -> 0)
    0     // chestPainType (null -> 0)
];

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
console.log("Prediction for user inputs:", prediction);
