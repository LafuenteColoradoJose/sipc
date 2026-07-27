import re

with open('app/components/Form.vue', 'r') as f:
    content = f.read()

# Fields to fix
fields = ['age', 'smoking', 'exerciseHours', 'stressLevel', 'cholesterol', 'bloodPressure', 'heartRate', 'bloodSugar', 'chestPainType']

for field in fields:
    # 1. Add id="field" to the input/select that has v-model="field"
    # Find <input ... v-model="field" ...> or <select ... v-model="field" ...>
    content = re.sub(rf'(<(?:input|select)[^>]+v-model="{field}")', rf'\1 id="{field}"', content)
    
    # 2. Add for="field" to the <label class="label"> immediately preceding it
    # We find `<label class="label"[^>]*>` followed by `.*?v-model="field"`
    # But regex might be greedy. We just replace `<label class="label">` with `<label class="label" for="field">` if it's the one for this field.
    # Actually, let's just do a manual replace for the labels.
    
with open('app/components/Form.vue', 'w') as f:
    f.write(content)

