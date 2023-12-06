const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
var stripe = Stripe(context['STRIPE_PUBLIC_KEY']);
const checkoutButton = document.getElementById('checkout-button');

checkoutButton.addEventListener('click', function() {
    fetch(context['url'],{
        method: 'GET',
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            stripe.redirectToCheckout({
                sessionId: data.id
            })
                .then(function(result) {
                });
        });
});




