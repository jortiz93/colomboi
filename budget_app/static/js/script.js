window.onload = function () {
    // Get data from inline script variables
    const labels = JSON.parse(document.getElementById('chart-labels').textContent);
    const data = JSON.parse(document.getElementById('chart-data').textContent);

    // Create the chart
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'pie', // Change to 'line', 'pie', etc. as needed
        data: {
            labels: labels,
            datasets: [{
                label: 'My Dataset',
                data: data,
                backgroundColor: [
                    'rgba(0, 153, 0, 1)', //Green 
                    'rgba(0, 76, 153, 1)',
                    'rgba(153, 0, 153, 1)',
                    'rgba(153, 0, 0, 1)',
                    'rgba(76, 0, 153, 1)'
                ],
                borderColor: [
                    'rgba(0, 0, 0, 1)', //Green 
                    'rgba(0, 0, 0, 1)', //Green 
                    'rgba(0, 0, 0, 1)', //Green 
                    'rgba(0, 0, 0, 1)', //Green 
                    'rgba(0, 0, 0, 1)', //Green 
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
};
