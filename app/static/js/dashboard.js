document.addEventListener('DOMContentLoaded', function () {
    /* ── Shared configuration ── */
    const GRID_COLOR  = 'rgba(255,255,255,0.05)';
    const TICK_COLOR  = '#64748b';
    const BLUE        = '#3b82f6';
    const PURPLE      = '#8b5cf6';
    const PALETTE     = [BLUE, PURPLE, '#ec4899', '#14b8a6', '#f59e0b', '#ef4444', '#22c55e', '#f97316'];

    const TOOLTIP_DEFAULTS = {
        backgroundColor: '#0f172a',
        titleFont: { size: 10 },
        bodyFont: { size: 12, weight: 'bold' },
        padding: 12,
        borderColor: '#1e293b',
        borderWidth: 1
    };

    window.chartRegistry = {};

    window.downloadChart = function(canvasId, filename) {
        const chart = window.chartRegistry[canvasId];
        if (!chart) return;
        const link = document.createElement('a');
        link.download = filename + '.png';
        link.href = chart.toBase64Image('image/png', 1);
        link.click();
    };

    /* ── Helpers de Validación de Datos ── */
    function hasValidData(labels, datasets) {
        // Falla si no hay labels o el backend mandó "No Data"
        if (!labels || labels.length === 0 || labels[0] === "No Data") return false;

        // Falla si todos los valores en todos los arrays son exactamente 0
        let hasValue = false;
        for (let dataArray of datasets) {
            if (dataArray && dataArray.some(val => Number(val) > 0)) {
                hasValue = true;
                break;
            }
        }
        return hasValue;
    }

    function showNoData(canvasId) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;

        const parent = canvas.parentElement;
        canvas.style.display = 'none'; // Ocultamos el canvas

        // Evitar renderizar múltiples placeholders
        if (parent.querySelector('.no-data-placeholder')) return;

        // FIX: Forzamos al padre a ser 'relative' para que el div absoluto no se escape al centro de la pantalla
        parent.classList.add('relative', 'flex', 'items-center', 'justify-center');

        const placeholder = document.createElement('div');
        placeholder.className = 'no-data-placeholder absolute inset-0 flex flex-col items-center justify-center text-center bg-slate-900/40 rounded-2xl border border-slate-800/50 backdrop-blur-sm z-10';
        placeholder.innerHTML = `
            <span class="material-symbols-outlined text-slate-600 text-5xl mb-3">query_stats</span>
            <p class="text-slate-500 font-black tracking-widest text-[10px] uppercase">No activity data found</p>
        `;
        parent.appendChild(placeholder);
    }

    /* ── 1. TREND LINE ── */
    const trendEl = document.getElementById('trendChart');
    if (trendEl) {
        const labels = JSON.parse(trendEl.dataset.labels || '[]');
        const values = JSON.parse(trendEl.dataset.values || '[]');

        if (!hasValidData(labels, [values])) {
            showNoData('trendChart');
        } else {
            window.chartRegistry['trendChart'] = new Chart(trendEl.getContext('2d'), {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Clicks',
                        data: values,
                        borderColor: BLUE,
                        backgroundColor: 'rgba(59,130,246,0.08)',
                        borderWidth: 3,
                        fill: true, tension: 0.4, pointRadius: 4, pointBackgroundColor: BLUE, pointHoverRadius: 7
                    }]
                },
                options: {
                    responsive: true, maintainAspectRatio: false,
                    plugins: { legend: { display: false }, tooltip: TOOLTIP_DEFAULTS },
                    scales: {
                        y: { beginAtZero: true, grid: { color: GRID_COLOR }, ticks: { color: TICK_COLOR, font: { size: 10 } } },
                        x: { grid: { display: false }, ticks: { color: TICK_COLOR, font: { size: 10 } } }
                    }
                }
            });
        }
    }

    /* ── 2. DOUGHNUT ── */
    const donutEl = document.getElementById('donutChart');
    if (donutEl) {
        const labels = JSON.parse(donutEl.dataset.labels || '[]');
        const values = JSON.parse(donutEl.dataset.values || '[]');

        if (!hasValidData(labels, [values])) {
            showNoData('donutChart');
        } else {
            window.chartRegistry['donutChart'] = new Chart(donutEl.getContext('2d'), {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        data: values,
                        backgroundColor: [BLUE, PURPLE],
                        borderColor: '#0f172a', borderWidth: 4, hoverOffset: 10
                    }]
                },
                options: {
                    responsive: true, maintainAspectRatio: false, cutout: '70%',
                    plugins: {
                        legend: { position: 'bottom', labels: { color: TICK_COLOR, font: { size: 11, weight: 'bold' }, padding: 16, boxWidth: 12 } },
                        tooltip: TOOLTIP_DEFAULTS
                    }
                }
            });
        }
    }

    /* ── 3. GENRE BAR ── */
    const genreEl = document.getElementById('genreChart');
    if (genreEl) {
        const labels = JSON.parse(genreEl.dataset.labels || '[]');
        const values = JSON.parse(genreEl.dataset.values || '[]');

        if (!hasValidData(labels, [values])) {
            showNoData('genreChart');
        } else {
            window.chartRegistry['genreChart'] = new Chart(genreEl.getContext('2d'), {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{ label: 'Titles', data: values, backgroundColor: PALETTE, borderRadius: 8 }]
                },
                options: {
                    responsive: true, maintainAspectRatio: false,
                    plugins: { legend: { display: false }, tooltip: TOOLTIP_DEFAULTS },
                    scales: {
                        y: { beginAtZero: true, grid: { color: GRID_COLOR }, ticks: { color: TICK_COLOR, font: { size: 10 } } },
                        x: { grid: { display: false }, ticks: { color: TICK_COLOR, font: { size: 10 }, maxRotation: 30 } }
                    }
                }
            });
        }
    }

    /* ── 4. PLATFORM GROUPED BAR ── */
    const platformEl = document.getElementById('platformChart');
    if (platformEl) {
        const labels = JSON.parse(platformEl.dataset.labels || '[]');
        const clicks = JSON.parse(platformEl.dataset.clicks || '[]');
        const favs = JSON.parse(platformEl.dataset.favs || '[]');

        if (!hasValidData(labels, [clicks, favs])) {
            showNoData('platformChart');
        } else {
            window.chartRegistry['platformChart'] = new Chart(platformEl.getContext('2d'), {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [
                        { label: 'Clicks', data: clicks, backgroundColor: BLUE, borderRadius: 6 },
                        { label: 'Favorites', data: favs, backgroundColor: PURPLE, borderRadius: 6 }
                    ]
                },
                options: {
                    responsive: true, maintainAspectRatio: false,
                    plugins: { legend: { position: 'top', labels: { color: TICK_COLOR, font: { size: 11, weight: 'bold' }, boxWidth: 12, padding: 12 } }, tooltip: TOOLTIP_DEFAULTS },
                    scales: {
                        y: { beginAtZero: true, grid: { color: GRID_COLOR }, ticks: { color: TICK_COLOR, font: { size: 10 } } },
                        x: { grid: { display: false }, ticks: { color: TICK_COLOR, font: { size: 10 } } }
                    }
                }
            });
        }
    }

    /* ── 5. TOP CONTENT HORIZONTAL BAR ── */
    const topEl = document.getElementById('topContentChart');
    if (topEl) {
        const labels = JSON.parse(topEl.dataset.labels || '[]');
        const values = JSON.parse(topEl.dataset.values || '[]');

        if (!hasValidData(labels, [values])) {
            showNoData('topContentChart');
        } else {
            window.chartRegistry['topContentChart'] = new Chart(topEl.getContext('2d'), {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{ label: 'Favorites', data: values, backgroundColor: PALETTE, borderRadius: 6 }]
                },
                options: {
                    indexAxis: 'y', responsive: true, maintainAspectRatio: false,
                    plugins: { legend: { display: false }, tooltip: TOOLTIP_DEFAULTS },
                    scales: {
                        x: { beginAtZero: true, grid: { color: GRID_COLOR }, ticks: { color: TICK_COLOR, font: { size: 10 } } },
                        y: { grid: { display: false }, ticks: { color: '#cbd5e1', font: { size: 11, weight: 'bold' } } }
                    }
                }
            });
        }
    }
});