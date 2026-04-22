async function calculateNow() {
    const payload = {
        cid: 1,
        step: currentStep

    };

    document.querySelectorAll('#inputs-container input').forEach(input => {
        payload[input.name] = input.value;
    });

    console.log("Sending to Python:", payload);

    const response = await fetch('/run_calculation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });

    const results = await response.json();
    document.getElementById('terminal').innerText = results.join('\n');
}
let currentStep = 1;
const totalSteps = 27;

async function advanceStep() {
    currentStep = (currentStep % totalSteps) + 1;
    await syncAndLoad();
}

async function jumpToStep() {
    currentStep = parseInt(document.getElementById('step-select').value);
    await syncAndLoad();
}

async function syncAndLoad() {

    document.getElementById('step-ui').innerText = currentStep;

    try {
        const response = await fetch(`/get_fields?cid=1&step=${currentStep}`);
        const fields = await response.json();

        const container = document.getElementById('inputs-container');
        container.innerHTML = '';

        fields.forEach(field => {

            const wrapper = document.createElement('div');
            wrapper.className = "input-group";
            wrapper.style.marginBottom = "15px";

            const label = document.createElement('label');
            label.innerText = field.label;
            label.style.display = "block";
            label.style.marginBottom = "5px";
            label.style.fontWeight = "bold";
            label.style.color = "#fff";

            const input = document.createElement('input');
            input.type = field.type || "number";
            input.id = field.id;
            input.name = field.id;
            input.value = field.default;

            if (field.min !== undefined) input.min = field.min;
            if (field.max !== undefined) input.max = field.max;

            input.className = "calc-input";
            input.style.width = "100%";
            input.style.padding = "8px";
            input.style.backgroundColor = "#fff";
            input.style.color = "#333";
            input.style.border = "1px solid #444";
            input.style.borderRadius = "4px";

            wrapper.appendChild(label);
            wrapper.appendChild(input);
            container.appendChild(wrapper);
        });

        document.getElementById('terminal').innerText = `>> MODULE ${currentStep} LOADED`;
    } catch (err) {
        document.getElementById('terminal').innerText = `>> ERROR LOADING STEP ${currentStep}`;
    }
}

async function loadFields() {
    const response = await fetch(`/get_fields?step=${currentStep}`);
    const fields = await response.json();

    const container = document.getElementById('inputs-container');

    container.innerHTML = '';

    fields.forEach(field => {
        const wrapper = document.createElement('div');
        wrapper.style.marginBottom = "10px";

        wrapper.innerHTML = `
            <label style="display:block; font-weight:bold;">${field.label}</label>
            <input type="${field.type}" 
                   id="${field.id}" 
                   name="${field.id}" 
                   value="${field.default}" 
                   class="calc-input" 
                   style="width:100%; padding:5px;">
        `;

        container.appendChild(wrapper);
    });
}
async function runProcess() {
    const payload = {
        action: "execute",
        cid: document.getElementById('cid').value,
        step: currentStep
    };
    const inputs = document.querySelectorAll('#dynamic-grid input');
    let isValid = true;

    inputs.forEach(i => {
        i.classList.remove('invalid');

        if (i.type === 'number' && (!i.value || i.value <= 0)) {
            i.classList.add('invalid');
            isValid = false;
        }
        payload[i.id] = i.type === 'checkbox' ? i.checked : i.value;
    });

    if (!isValid) {
        document.getElementById('terminal').innerText = ">> ERROR: INVALID INPUTS DETECTED";
        return;
    }

    const res = await fetch('/exp/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });
    const data = await res.json();
    document.getElementById('terminal').innerHTML = data.lines.map(l => `<div>${l}</div>`).join('');
}

function resetEngine() {
    currentStep = 1;
    document.getElementById('step-ui').innerText = 1;
    loadFields();
}
loadFields();
