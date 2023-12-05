var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function showInfoPopup(message) {
    $(document).ready(function() {
        $('#myModal').modal('show'); // Открываем модальное окно при загрузке страницы
        document.getElementById('text-modal').innerText = message
        setTimeout(function() {
            $('#myModal').modal('hide'); // Закрываем модальное окно через 10 секунд
        }, 2000);
    });
}


document.querySelectorAll('#order-button').forEach(
    item => item.addEventListener('click', function() {
        var value = item.value;
        const cookies = document.cookie;
        fetch('../AddItem/' + value,{
            method: 'GET',
            headers: {
                'X-CSRFToken': csrftoken,
                'Cookie': cookies,
            }
        })
            .then(function(response) {
                return response.json();
            })
            .then(function(data) {
                showInfoPopup(data.otvet);
            })
            .catch(error => {
                console.error('Ошибка запроса:', error);
            });
    })
);


document.querySelectorAll('#order-delete').forEach(
    item => item.addEventListener('click', function() {
        var value = item.value;
        const cookies = document.cookie;
        fetch('../DelItem/' + value,{
            method: 'GET',
            headers: {
                'X-CSRFToken': csrftoken,
                'Cookie': cookies,
            }
        })
            .then(function(response) {
                return response.json();
            })
            .then(function(data) {
                showInfoPopup(data.otvet);
                location.reload();
            })
            .catch(error => {
                console.error('Ошибка запроса:', error);
            });
    })
);

