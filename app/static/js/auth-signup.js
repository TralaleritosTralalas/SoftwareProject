document.addEventListener('DOMContentLoaded', function() {
    const password1 = document.getElementById('id_password1');
    const password2 = document.getElementById('id_password2');
    const submitBtn = document.getElementById('submit-btn');

    const lengthCheck = document.getElementById('length-check');
    const commonCheck = document.getElementById('common-check');
    const numberCheck = document.getElementById('number-check');
    const password2Match = document.getElementById('password2-match');
    const matchIcon = document.getElementById('match-icon');
    const matchText = document.getElementById('match-text');

    const commonPasswords = [
        'password', '12345678', '123456789', 'qwerty', 'abc123', 'password1',
        '1234567', 'password123', 'welcome', 'hello', 'admin', 'letmein',
        'sunshine', 'princess', 'football', 'monkey', 'dragon'
    ];

    function validatePassword1() {
        const pwd = password1.value;
        let valid = true;

        if (pwd.length >= 8) {
            lengthCheck.textContent = '✓';
            lengthCheck.className = 'text-green-500';
        } else {
            lengthCheck.textContent = '○';
            lengthCheck.className = 'text-slate-400';
            valid = false;
        }

        if (!commonPasswords.includes(pwd.toLowerCase())) {
            commonCheck.textContent = '✓';
            commonCheck.className = 'text-green-500';
        } else {
            commonCheck.textContent = '○';
            commonCheck.className = 'text-slate-400';
            valid = false;
        }

        if (!/^\d+$/.test(pwd)) {
            numberCheck.textContent = '✓';
            numberCheck.className = 'text-green-500';
        } else {
            numberCheck.textContent = '○';
            numberCheck.className = 'text-slate-400';
            valid = false;
        }

        return valid;
    }

    function validatePassword2() {
        const pwd1 = password1.value;
        const pwd2 = password2.value;

        password2Match.classList.remove('hidden');

        if (pwd2.length === 0) {
            password2Match.classList.add('hidden');
            return false;
        }

        if (pwd1 === pwd2) {
            matchIcon.textContent = '✓';
            matchText.textContent = 'Passwords match';
            matchIcon.className = 'text-green-500';
            matchText.className = 'text-green-500';
            return true;
        } else {
            matchIcon.textContent = '✗';
            matchText.textContent = 'Passwords do not match';
            matchIcon.className = 'text-red-500';
            matchText.className = 'text-red-500';
            return false;
        }
    }

    function updateSubmitButton() {
        const pwd1Valid = validatePassword1();
        const pwd2Valid = validatePassword2();
        const termsChecked = document.getElementById('id_terms_of_service').checked;
        const privacyChecked = document.getElementById('id_privacy_policy').checked;

        if (pwd1Valid && pwd2Valid && termsChecked && privacyChecked) {
            submitBtn.disabled = false;
        } else {
            submitBtn.disabled = true;
        }
    }

    password1.addEventListener('input', function() {
        validatePassword1();
        validatePassword2();
        updateSubmitButton();
    });

    password2.addEventListener('input', function() {
        validatePassword2();
        updateSubmitButton();
    });

    document.getElementById('id_terms_of_service').addEventListener('change', updateSubmitButton);
    document.getElementById('id_privacy_policy').addEventListener('change', updateSubmitButton);
});