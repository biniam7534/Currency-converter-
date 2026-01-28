document.addEventListener('DOMContentLoaded', () => {
    const convertBtn = document.getElementById('convert-btn');
    const amountInput = document.getElementById('amount');
    const fromSelect = document.getElementById('from-currency');
    const toSelect = document.getElementById('to-currency');
    const resultArea = document.getElementById('result-area');
    const resultMain = document.getElementById('result-main');
    const exchangeRateText = document.getElementById('exchange-rate');
    const swapBtn = document.getElementById('swap-btn');
    const loader = document.getElementById('loader');
    const btnText = document.getElementById('btn-text');

    async function performConversion() {
        const amount = amountInput.value;
        const from = fromSelect.value;
        const to = toSelect.value;

        if (!amount || amount <= 0) {
            alert('Please enter a valid amount');
            return;
        }

        // UI State: Loading
        convertBtn.disabled = true;
        loader.style.display = 'block';
        btnText.style.display = 'none';

        try {
            const response = await fetch(`/convert/?amount=${amount}&from=${from}&to=${to}`);
            const data = await response.json();

            if (data.error) {
                throw new Error(data.error);
            }

            resultMain.textContent = `${data.result.toLocaleString()} ${to}`;
            exchangeRateText.textContent = `1 ${from} = ${data.rate.toFixed(4)} ${to}`;
            
            resultArea.classList.add('active');
        } catch (error) {
            console.error('Conversion error:', error);
            alert('Error converting currency. Please try again later.');
        } finally {
            convertBtn.disabled = false;
            loader.style.display = 'none';
            btnText.style.display = 'block';
        }
    }

    convertBtn.addEventListener('click', performConversion);

    swapBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const temp = fromSelect.value;
        fromSelect.value = toSelect.value;
        toSelect.value = temp;
        if (resultArea.classList.contains('active')) {
            performConversion();
        }
    });

    // Enter key support
    amountInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            performConversion();
        }
    });
});
