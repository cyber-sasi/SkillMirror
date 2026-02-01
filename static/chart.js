const canvas = document.getElementById("skillChart");

if (canvas) {
    const skills = JSON.parse(canvas.dataset.skills);

    const labels = skills.map(s => s.language);
    const data = skills.map(s => s.count);

    let chartType = "pie";
    const ctx = canvas.getContext("2d");

    const chartData = {
        labels: labels,
        datasets: [{
            data: data,
            backgroundColor: [
                "#4dabf7",
                "#ff6b81",
                "#ffa94d",
                "#ffd43b",
                "#4ecdc4",
                "#9775fa",
                "#ced4da"
            ]
        }]
    };

    /* 🥧 PIE OPTIONS */
    const pieOptions = {
        responsive: true,
        maintainAspectRatio: false,
        resizeDelay: 150,

        /* ✅ STEP 5: Mobile touch-friendly interaction */
        interaction: {
            mode: "nearest",
            intersect: true
        },

        animation: {
            animateRotate: true,
            animateScale: true,
            duration: 1300,
            easing: "easeInOutCubic"
        },
        plugins: {
            legend: {
                display: true,

                /* ✅ STEP 4: Auto font scaling (mobile friendly) */
                labels: {
                    color: "#ffffff",
                    font: () => ({
                        size: window.innerWidth < 480 ? 11 : 14,
                        weight: "600"
                    })
                }
            }
        }
    };

    /* 📊 BAR OPTIONS */
    const barOptions = {
        responsive: true,
        maintainAspectRatio: false,

        /* ✅ STEP 5: Touch-friendly interaction */
        interaction: {
            mode: "nearest",
            intersect: true
        },

        animation: {
            duration: 1400,
            easing: "easeOutQuart"
        },
        plugins: {
            legend: {
                display: false
            }
        },
        scales: {
            x: {
                ticks: {
                    color: "#e9ecef",

                    /* ✅ STEP 4: Responsive font */
                    font: () => ({
                        size: window.innerWidth < 480 ? 11 : 13,
                        weight: "600"
                    })
                },
                grid: {
                    color: "rgba(255,255,255,0.05)"
                }
            },
            y: {
                beginAtZero: true,
                ticks: {
                    color: "#e9ecef",
                    stepSize: 1,

                    /* ✅ STEP 4: Responsive font */
                    font: () => ({
                        size: window.innerWidth < 480 ? 11 : 13,
                        weight: "500"
                    })
                },
                grid: {
                    color: "rgba(255,255,255,0.08)"
                }
            }
        }
    };

    /* ✅ INITIAL PIE CHART */
    let chart = new Chart(ctx, {
        type: "pie",
        data: chartData,
        options: pieOptions
    });

    /* 🔁 TOGGLE PIE ↔ BAR */
    document.getElementById("toggleChartBtn")?.addEventListener("click", () => {
        chart.destroy();
        chartType = chartType === "pie" ? "bar" : "pie";

        chart = new Chart(ctx, {
            type: chartType,
            data: chartData,
            options: chartType === "bar" ? barOptions : pieOptions
        });
    });
}
