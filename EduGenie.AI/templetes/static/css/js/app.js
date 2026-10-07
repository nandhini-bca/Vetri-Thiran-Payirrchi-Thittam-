document.addEventListener('DOMContentLoaded', () => {
  const statusElm = document.getElementById('status');
  const button = document.getElementById('health-check');

  const fetchHealth = async () => {
    try {
      const response = await fetch('/health');
      const data = await response.json();
      statusElm.textContent = `${data.service}: ${data.status}`;
    } catch (error) {
      statusElm.textContent = 'Unable to reach the service. Check the backend logs.';
    }
  };

  button?.addEventListener('click', fetchHealth);
  fetchHealth();
});
