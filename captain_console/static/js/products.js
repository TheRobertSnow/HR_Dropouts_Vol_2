$(document).ready(function () {
    $('#search-btn').on("click", function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        var add_options = $('#add_opt').val();
        var add_cat = $('#add_cat').val();
        var add_type = $('#add_type').val();
        $.ajax( {
            url: '/?search_filter=' + searchText,
            type: 'GET',
            headers: {
                'addFilter': add_options,
                'addType': add_type,
                'addCategory': add_cat,
            },
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class=product-container>
                                <a href="/products/${d.id}">
                                    <div class="product-mainImage">
                                        <img src="${d.mainImageLink}" alt="">
                                    </div>
                                    <h4 class="product-name">${d.name}</h4>
                                    <p class="product-price">$ ${d.price.toFixed(2)}</p>
                                </a>
                            </div>`
                });
                $('.homePage').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    });
});