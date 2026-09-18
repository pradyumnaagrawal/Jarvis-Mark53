async function executeBackendAction(actionName, payload) {
  try {
    const response = await fetch('https://your-backend-url.onrender.com/api/execute', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action: actionName, args: payload })
    });
    return await response.json();
  } catch (error) {
    console.error("Backend execution failed:", error);
    return { ok: false, error: error.message };
  }
}

