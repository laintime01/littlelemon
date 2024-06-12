document.addEventListener('DOMContentLoaded', () => {
    const dateInput = document.querySelector('input[name="reservation_date"]');
    const timeSelect = document.querySelector('select[name="reservation_time"]');
    
    dateInput.addEventListener('change', () => {
        fetch(`/restaurant/bookings_json/?date=${dateInput.value}`)
            .then(response => response.json())
            .then(data => {
                const reservedTimes = data.map(booking => booking.reservation_time);
                Array.from(timeSelect.options).forEach(option => {
                    if (reservedTimes.includes(option.value)) {
                        option.disabled = true;
                        option.textContent = `${option.textContent} (Unavailable)`;
                    } else {
                        option.disabled = false;
                        option.textContent = option.value; // Reset option text
                    }
                });
            });
    });
});
