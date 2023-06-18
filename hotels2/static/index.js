function fillAndShowTheForm(hotel, checkin, checkout, booking_id, customer_id){
    const form = document.querySelector('.rebooking');

    form.innerHTML = '';

    const newFormHTML = `
      <h2 class="change-title">Change parameters:</h2>
      <div class="change-params">
        <h2>${hotel}</h2>
        <h3>Current check in: ${checkin}</h3>
        <h3>Current check out: ${checkout}</h3>
      </div>
      <div class="form-group">
        <label for="new_checkin">New check in date:</label>
        <input type="date" id="new_checkin" name="new_checkin" required>
      </div>
      <div class="form-group">
        <label for="new_checkout">New check out date:</label>
        <input type="date" id="new_checkout" name="new_checkout" required>
      </div>
      <div class="form-group">
        <input type="hidden" id="booking_id" name="booking_id" value=${booking_id}>
        <input type="hidden" id="customer_id" name="customer_id" value=${customer_id}>
      </div>
      <div class="form-group">
        <button class="reserve-btn approve-change">Approve change</button>
      </div>      
    `;

    form.insertAdjacentHTML('beforeend', newFormHTML);
}


function removeBooking(booking_id) {
    fetch('/remove-booking', {
        method: 'POST',
        body: JSON.stringify({booking_id: booking_id})
    }).then((_res) => {
        window.location.href = '/bookings'
    });
}