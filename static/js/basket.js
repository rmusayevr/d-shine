if (document.querySelector('#basket')) {
    const product = document.querySelector('#basket');
    function getBasket() {
        product.addEventListener('click', async () => {
            return fetch(`${location.origin}/api/basket/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': product.dataset.id,
                    'quantity': 1,
                })
            })
                .then((response) => response.json()).then((data) => {
                    if (data.success) {
                        alert('Added to basket');
                        fetch(`${location.origin}/api/basket/`).then(response => response.json()).then(data => {
                            document.getElementById('total-basket').innerHTML = ''
                            document.getElementById('total-basket').innerHTML += `
                                <i class="fas fa-gem"></i> ${data.products.length}
                            `
                            getRemoveBasketItem()
                        })
                    }
                })
        })
    }

    getBasket()
}


function getRemoveBasketItem() {
    const removeBasketItems = document.querySelectorAll('.remove-basket');
    removeBasketItems.forEach((element) => {
        element.addEventListener('click', () => {
            return fetch(`${location.origin}/api/basket/`, {
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
                        fetch(`${location.origin}/api/basket/`).then(response => response.json()).then(data => {
                            document.getElementById('basket-products').innerHTML = ''
                            document.getElementById('total-price').innerHTML = ''
                            data['products'].forEach((element) => {
                                document.getElementById('basket-products').innerHTML += `
                                    <tr class="alert" role="alert">
                                        <td class="productImage" style="vertical-align: middle;"><img src="${element.product.image[0].image}" alt="${element.product.name}"></td>
                                        <td class="productName" style="vertical-align: middle;">
                                            <div class="row descList m0">
                                                <dl class="dl-horizontal">
                                                    <dt>product name :</dt>
                                                    <dd>${element.product.name}</dd>
                                                    <dt>product code :</dt>
                                                    <dd>${element.product.code}</dd>
                                                    <dt>category :</dt>
                                                    <dd>${element.product.category.name}</dd>
                                                    <dt>manufacturer :</dt>
                                                    <dd>${element.product.manufacturer.name}</dd>
                                                </dl>
                                            </div>
                                        </td>
                                        ${element.product.in_sale ?
                                        '<td class="price" style="vertical-align: middle;"><del>$' + element.product['price'] + '</del>$' + element.product['final_price'] + '</td>'
                                        : '<td class="price" style="vertical-align: middle;">$' + element.product['price'] + '</td>'}
                                        <td style="vertical-align: middle;">
                                            <div class="input-group spinner" style="height: max-content;">
                                                <input type="text" class="form-control" value="${element.quantity}">
                                                <div class="input-group-btn-vertical">
                                                    <button class="btn btn-default"><i class="fas fa-angle-up"></i></button>
                                                    <button class="btn btn-default"><i class="fas fa-angle-down"></i></button>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="price" style="vertical-align: middle;">$${element.subtotal.toFixed(2)}</td>
                                        <td style="vertical-align: middle;"><button class="remove-basket" data-id="${element.product.id}" style="background-color: #fd405e; border: none; color: white; padding: 12px 10px; border-radius: 5px;"><i class="far fa-trash-alt"></i></button></td>
                                    </tr>
                                `
                            })
                            document.getElementById('total-price').innerHTML += `
                                ${data.total === 0 ? '$0' : '$' + data.total.toFixed(2)}
                            `
                            document.getElementById('total-basket').innerHTML = `
                                <i class="fas fa-gem"></i> ${data.products.length}
                            `
                            getRemoveBasketItem()
                        })
                    }
                })
        })
    })
}


getRemoveBasketItem()


if (document.getElementById('clear-basket')) {
    document.getElementById('clear-basket').addEventListener('click', async () => {
        return await fetch(`${location.origin}/api/basket/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
        })
            .then((response) => response.json()).then((data) => {
                if (data.success) {
                    fetch(`${location.origin}/api/basket/`).then(response => response.json()).then(data => {
                        document.getElementById('basket-products').innerHTML = ''
                        document.getElementById('total-price').innerHTML = '$0'
                        document.getElementById('total-basket').innerHTML = `
                            <i class="fas fa-gem"></i> ${data.products.length}
                        `
                    })
                    alert(data.message)
                }
            })
    })
}
