let buttons = document.getElementsByClassName('update_product_btn')
let detail = document.getElementsByClassName('detail')

// from: https://docs.djangoproject.com/en/4.1/howto/csrf/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

for(let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function() {
        let productid = this.dataset.product
        let action = this.dataset.action
        let user = this.dataset.user
        if(user == 'AnonymousUser') {
            window.location.href = "/admin/"
        } else {
            updateOrder(productid, action)
        }
    });
}

function updateOrder(productid, action) {
    let url = '/add_item/'
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body:JSON.stringify({"productid": productid, "action": action})
    })
    .then(res => res.json())
    .then(data => location.reload())
}

for(let i = 0; i < detail.length; i++) {
    detail[i].addEventListener("click", function() {
        let productid = this.dataset.product
        window.location.href = `/product/${productid}`
    });
}