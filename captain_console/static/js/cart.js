(function () {
    var products = document.getElementsByName('prod-price');
    var total = 0;
    for (i = 0; i < products.length; i++) {
        var temp = products[i].innerText.replace("$ ", "")
        total += parseFloat(temp);
    }
    var newstring = document.getElementById('total')
    newstring.innerText += total;
})();