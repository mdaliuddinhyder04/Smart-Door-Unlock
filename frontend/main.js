async function requestAccess() {
  const res = await fetch('/api/visitor_request', { method: 'POST' });
  const data = await res.json();
  alert("Request sent to owner.");
}

async function verifyCode() {
  const code = document.getElementById('codeInput').value.trim();
  const res = await fetch('/api/verify_code', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code })
  });
  const data = await res.json();
  const msg = {
    success: "✅ Door Unlocked",
    fail: "❌ Incorrect Code",
    expired: "⌛ Code Expired"
  };
  document.getElementById('resultMsg').innerText = msg[data.result];
}
