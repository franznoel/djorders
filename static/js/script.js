var setProduct = function(productId,productName,productImage,productPrice) {
  document.getElementById('productId').value = productId;
  $('#pic-image').attr('src',productImage);
  $('#pic-name').html(productName);
  $('#pic-price').html('$'+productPrice);
}

var togglePayment = function() {
  $('#payment-information').toggle(400);
}

var getCookie = function(c_name) {
  var c_value = document.cookie;
  var c_start = c_value.indexOf(" " + c_name + "=");
  if (c_start == -1) {
    c_start = c_value.indexOf(c_name + "=");
  }
  if (c_start == -1) {
    c_value = null;
  } else {
    c_start = c_value.indexOf("=", c_start) + 1;
    var c_end = c_value.indexOf(";", c_start);
    if (c_end == -1) {
      c_end = c_value.length;
    }
    c_value = unescape(c_value.substring(c_start,c_end));
  }
  return c_value;
}

var setDate = function() {
  document.getElementById('today').valueAsDate = new Date();
}
