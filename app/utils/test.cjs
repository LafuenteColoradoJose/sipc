const fs = require('fs');
const buffer = fs.readFileSync('/home/pp/Escritorio/Proyectos/sipc/public/model/tfjs_model/group1-shard1of1.bin');
const float32Array = new Float32Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / 4);

// shape [15, 64]
const w1 = float32Array.slice(0, 960);
const b1 = float32Array.slice(960, 1024);
const w2 = float32Array.slice(1024, 1088);
const b2 = float32Array.slice(1088, 1089);

const inputs = [80, 0, 270, 120, 80, 0, 0, 2, 1, 0, 1, 2, 120, 0, 0];

const hidden = new Float32Array(64);
for (let i = 0; i < 64; i++) {
    let sum = b1[i];
    for (let j = 0; j < 15; j++) {
        // w1 is row-major: j is input, i is hidden
        // Wait! tf.tensor2d([15, 64]) means row is input, col is hidden!
        // So index is j * 64 + i
        sum += inputs[j] * w1[j * 64 + i];
    }
    // relu
    hidden[i] = Math.max(0, sum);
}

let out = b2[0];
for (let i = 0; i < 64; i++) {
    out += hidden[i] * w2[i];
}
// sigmoid
const prediction = 1 / (1 + Math.exp(-out));
console.log("Prediction:", prediction);
