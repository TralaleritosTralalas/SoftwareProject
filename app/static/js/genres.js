document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.genre-checkbox');
    const countDisplay = document.getElementById('count');
    const continueBtn = document.getElementById('continue-btn');
    const counterWrapper = document.getElementById('selection-counter');

    function updateCounter() {
        const selected = document.querySelectorAll('.genre-checkbox:checked').length;
        const prevCount = parseInt(countDisplay.textContent) || 0;

        countDisplay.textContent = selected;

        if (selected >= 3) {
            continueBtn.disabled = false;
            countDisplay.classList.remove('text-white');
            countDisplay.classList.add('text-green-400');
            counterWrapper.classList.add('border-green-500/50', 'shadow-[0_0_15px_rgba(34,197,94,0.2)]');
        } else {
            continueBtn.disabled = true;
            countDisplay.classList.add('text-white');
            countDisplay.classList.remove('text-green-400');
            counterWrapper.classList.remove('border-green-500/50', 'shadow-[0_0_15px_rgba(34,197,94,0.2)]');
        }

        if (selected !== prevCount) {
            countDisplay.style.transform = 'scale(1.3)';
            setTimeout(() => {
                countDisplay.style.transform = 'scale(1)';
            }, 150);
        }
    }

    checkboxes.forEach(cb => {
        cb.addEventListener('change', updateCounter);
    });

    updateCounter();
});