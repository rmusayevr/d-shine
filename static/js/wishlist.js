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


function getWishlist() {
    const wishlists = document.querySelectorAll('.wishlist');
    wishlists.forEach((element) => {
        element.addEventListener('click', () => {
            return fetch(`${location.origin}/api/wishlist/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': element.dataset.id,
                })
            })
                .then((response) => response.json()).then((data) => {
                    if (data.success) {
                        alert('Added to wishlist');
                        fetch(`${location.origin}/api/wishlist/`).then(response => response.json()).then(data => {
                            document.getElementById('total-wishlist').innerHTML = `
                                <i class="fas fa-heart"></i> ${data.products.length}
                            `
                        })
                    }
                })
        })
    })
}

getWishlist()


function getRemoveWishlist() {
    const removeWishlists = document.querySelectorAll('.remove-wishlist');
    removeWishlists.forEach((element) => {
        element.addEventListener('click', async () => {
            return await fetch(`${location.origin}/api/wishlist/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': element.dataset.id,
                })
            })
                .then((response) => response.json()).then((data) => {
                    if (data.success) {
                        fetch(`${location.origin}/api/wishlist/`).then(response => response.json()).then(data => {
                            document.getElementById('wishlist-products').innerHTML = ''
                            data['products'].forEach((element) => {
                                document.getElementById('wishlist-products').innerHTML += `
                                <tr class="alert" role="alert">
                                    <td class="productImage" style="vertical-align: middle;"><img src="${element.image[0].image}" alt="${element.name}"></td>
                                    <td class="productName" style="vertical-align: middle;">
                                        <div class="row descList m0">
                                            <dl class="dl-horizontal">
                                                <dt>product name :</dt>
                                                <dd>${element.name}</dd>
                                                <dt>product code :</dt>
                                                <dd>${element.code}</dd>
                                                <dt>category :</dt>
                                                <dd>${element.category.name}</dd>
                                                <dt>manufacturer :</dt>
                                                <dd>${element.manufacturer.name}</dd>
                                            </dl>
                                        </div>
                                    </td>
                                    ${element.in_sale ?
                                        '<td class="price" style="vertical-align: middle;"><del>$' + element.price + '</del>$' + element.final_price + '</td>'
                                        : '<td class="price" style="vertical-align: middle;">$' + element.price + '</td>'}
                                    <td style="vertical-align: middle;"><button class="remove-wishlist" data-id="${element.id}" style="background-color: #fd405e; border: none; color: white; padding: 12px; border-radius: 5px;"><i class="far fa-trash-alt"></i></button></td>
                                    <td style="vertical-align: middle;"><button class="add-basket" data-id="${element.id}" style="background-color: #fd405e; border: none; color: white; padding: 12px 10px; border-radius: 5px;"><i class="fas fa-shopping-basket"></i></button></td>
                                </tr>
                            `
                            })
                            document.getElementById('total-wishlist').innerHTML = `
                                <i class="fas fa-heart"></i> ${data.products.length}
                            `
                            getRemoveWishlist()
                        })
                    }
                })
        })
    })
}

getRemoveWishlist()


function addBasket() {
    const addBaskets = document.querySelectorAll('.add-basket');
    addBaskets.forEach((element) => {
        element.addEventListener('click', () => {
            return fetch(`${location.origin}/api/basket/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': element.dataset.id,
                    'quantity': 1
                })
            })
                .then((response) => response.json()).then((data) => {
                    if (data.success) {
                        alert('Added to basket')
                        fetch(`${location.origin}/api/basket/`).then(response => response.json()).then(data => {
                            document.getElementById('total-basket').innerHTML = `
                            <i class="fas fa-gem"></i> ${data.products.length}
                        `
                        })
                    }
                })
        })
    })
}

addBasket()

if (document.getElementById('clear-wishlist')) {
    document.getElementById('clear-wishlist').addEventListener('click', async () => {
        return await fetch(`${location.origin}/api/wishlist/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
        })
            .then((response) => response.json()).then((data) => {
                if (data.success) {
                    fetch(`${location.origin}/api/wishlist/`).then(response => response.json()).then(data => {
                        document.getElementById('wishlist-products').innerHTML = ''
                        document.getElementById('total-wishlist').innerHTML = `
                        <i class="fas fa-gem"></i> ${data.products.length}
                        `
                    })
                    alert(data.message)
                }
            })
    })
}
