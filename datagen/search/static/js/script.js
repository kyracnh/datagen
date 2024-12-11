// static/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    // Market Size Chart (Bar Chart)
    const ctx1 = document.getElementById('marketSizeChart').getContext('2d');
    const marketSizeChart = new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: ['TAM', 'SAM', 'SOM'], // Example categories for Market Size
            datasets: [{
                label: 'Market Size (in Billion USD)',
                data: [150, 120, 80], // Example data points
                backgroundColor: ['rgba(75, 192, 192, 0.2)', 'rgba(153, 102, 255, 0.2)', 'rgba(255, 159, 64, 0.2)'],
                borderColor: ['rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)'],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Market Trends Chart (Line Chart)
    const ctx2 = document.getElementById('marketTrendsChart').getContext('2d');
    const marketTrendsChart = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: ['2020', '2021', '2022', '2023'], // Example years
            datasets: [{
                label: 'Market Trends Growth',
                data: [5, 10, 15, 25], // Example trend data
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 2
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Customer Segmentation Chart (Pie Chart)
    const ctx3 = document.getElementById('customerSegmentationChart').getContext('2d');
    const customerSegmentationChart = new Chart(ctx3, {
        type: 'pie',
        data: {
            labels: ['Young Adults', 'Middle Aged', 'Seniors'], // Example categories
            datasets: [{
                label: 'Customer Segmentation',
                data: [30, 40, 30], // Example segmentation data
                backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(255, 159, 64, 0.2)'],
                borderColor: ['rgba(255, 99, 132, 1)', 'rgba(75, 192, 192, 1)', 'rgba(255, 159, 64, 1)'],
                borderWidth: 1
            }]
        }
    });

    // Customer Needs and Pain Points Chart (Radar Chart)
    const ctx4 = document.getElementById('customerNeedsChart').getContext('2d');
    const customerNeedsChart = new Chart(ctx4, {
        type: 'radar',
        data: {
            labels: ['Price Sensitivity', 'Quality', 'Customer Support', 'Brand Reputation'], // Example needs
            datasets: [{
                label: 'Customer Needs and Pain Points',
                data: [70, 60, 90, 85], // Example data points
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 2
            }]
        }
    });

    // Market Growth Rate Chart (Bar Chart)
    const ctx5 = document.getElementById('marketGrowthRateChart').getContext('2d');
    const marketGrowthRateChart = new Chart(ctx5, {
        type: 'bar',
        data: {
            labels: ['2020', '2021', '2022', '2023'], // Example years
            datasets: [{
                label: 'Market Growth Rate (%)',
                data: [5, 10, 15, 20], // Example growth rate data
                backgroundColor: 'rgba(255, 159, 64, 0.2)',
                borderColor: 'rgba(255, 159, 64, 1)',
                borderWidth: 1
            }]
        }
    });

});
