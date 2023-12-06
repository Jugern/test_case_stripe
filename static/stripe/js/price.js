function sendRequestWithCookies() {
  const cookies = document.cookie;

  const requestOptions = {
    method: 'GET',
    headers: {
      'Cookie': cookies
    }
  };

  // Отправляем запрос
  fetch('../api/v1/price/', requestOptions)
    .then(response => response.json())
    .then(data => {
      document.getElementById('header_price').innerHTML = '$' + data['price'];
    })
    .catch(error => {
      console.error('Ошибка запроса:', error);
    });
}

sendRequestWithCookies()
setInterval(sendRequestWithCookies, 2000);