$(document).ready(function () {
    $('#search-btn').on(types: 'click', selector: function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax( url: {
            url: '/products?search_filter=' + searchText,
                type: 'GET',
                success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class=product-container>
                                <a href="/products/${d.id}">
                                    <img class="product-mainImage" src="${d.mainImage}"/>
                                    <h4 class="product-name">${d.name}</h4>
                                    <p class="product-price">${d.price} kr.</p>
                                </a>
                            </div>`
                });
                $('.homePage').html(newHtml.join(''));
                $('#search-box').val(value: '');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
});