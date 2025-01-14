$("#slider1, #slider2, #slider3, #slider4").owlCarousel({
  loop: true,
  margin: 20,
  responsiveClass: true,
  responsive: {
    0: {
      items: 1,
      nav: false,
      autoplay: true,
    },
    600: {
      items: 3,
      nav: true,
      autoplay: true,
    },
    1000: {
      items: 5,
      nav: true,
      loop: true,
      autoplay: true,
    },
  },
});

$(".plus-cart").click(function () {
  var id = $(this).attr("pid"); // Directly get attribute
  var eml = this.parentNode.children[2];
  if (id) {
    // Check if id is defined
    $.ajax({
      type: "GET",
      url: "/pluscart",
      data: { prod_id: id },
      success: function (data) {
        console.log(data);
        eml.innerText = data.quantity;
        document.getElementById("amount").innerText = data.amount;
        document.getElementById("total_amount").innerText = data.total_amount;
      },
    });
  } else {
    console.error("pid attribute is missing or undefined.");
  }
});

$(".minus-cart").click(function () {
  var id = $(this).attr("pid"); // Directly get attribute
  var eml = this.parentNode.children[2];
  if (id) {
    // Check if id is defined
    $.ajax({
      type: "GET",
      url: "/minuscart",
      data: { prod_id: id },
      success: function (data) {
        console.log(data);
        eml.innerText = data.quantity;
        document.getElementById("amount").innerText = data.amount;
        document.getElementById("total_amount").innerText = data.total_amount;
      },
    });
  } else {
    console.error("pid attribute is missing or undefined.");
  }
});

$(".remove-cart").click(function () {
  var id = $(this).attr("pid"); // Directly get attribute
  console.log(id);
  $.ajax({
    type: "GET",
    url: "/removecart",
    data: { prod_id: id },
    success: function (data) {
      console.log(data);
      document.getElementById("amount").innerText = data.amount
      document.getElementById("totalamount").innerText = data.totalamount
    },
  });
});
  
