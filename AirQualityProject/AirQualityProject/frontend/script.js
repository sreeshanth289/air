const FEATURES = ["PT08.S1(CO)", "PT08.S2(NMHC)", "PT08.S3(NOx)", "PT08.S4(NO2)",
                  "PT08.S5(O3)", "T", "RH", "AH", "hour", "month"];
const fields = document.getElementById("fields");
FEATURES.forEach(f => {
  fields.insertAdjacentHTML("beforeend",
    `<label>${f}<input type="number" step="any" id="${f}"></label>`);
});

document.getElementById("predictBtn").addEventListener("click", async () => {
  const payload = {};
  FEATURES.forEach(f => {
    const v = document.getElementById(f).value;
    payload[f] = v === "" ? null : parseFloat(v);
  });
  try {
    const res = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const out = await res.json();
    document.getElementById("result").textContent =
      `CO: ${out.CO_prediction} mg/m³ — ${out.status}`;
  } catch (e) {
    document.getElementById("result").textContent = "Could not reach the backend.";
  }
});
