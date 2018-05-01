// function loopForm(form)
// {
//   if (document.getElementById('checkbox').checked == false) 
//   {
//       //alert('Select at least one member');
//       document.getElementById('checkalert').innerHTML="Select at least one member";
//       return false;
//   }
// }

function validate(){
	var user = document.loginform.username.value;
	var pass = document.loginform.password.value;
	if(user == ""){
		document.getElementById('useralert').innerHTML="Please enter the username";
		document.getElementById('form_css1').style.borderColor = "red";
		return false;
	}
	else if(pass == ""){
		document.getElementById('passalert').innerHTML="Please enter the password";
		document.getElementById('form_css2').style.borderColor = "red";
		return false;
	}

}

setTimeout(function() {
 $('.alert').fadeOut();
}, 3000 );

$("document").ready(function(){

    $("#usr_trans_li").click(function(){
        $('#content').load('/trans_view #trans_tbl', function() {
            });
    });

    $("#usr_dash_li").click(function(){
        $('#content').load('/dashboard #msg', function() {
            });
    });
});



//Attemp to do the calculation using javascript but decided to use python instead. And use javascript for making ajax and jquery calls
var year;
var month;
var rate;
var amount;
var montyly_payment;

$("document").ready(function() {
	$("#submit").click(function() {

		year = document.getElementById("year").value;
  		month = document.getElementById("month").value;
  		rate = document.getElementById("rate").value;
  		amount = document.getElementById("amount").value;
  		term_raw = year * 12;
  		term = term_raw + month;
  		rate = rate/1200;
		mPmt = calculatePayment();
		  
		var a = 5;
		var b = 6;
		var c = a + b;
		console.log(c);
  		document.getElementById("pmt").value = "$" + mPmt.toFixed(2);
  		document.getElementById("output").innerHTML = c;
	});
});


function calculatePayment()
{
	var payment = amount*(apr * Math.pow((1 + rate), term))/(Math.pow((1 + rate), term) - 1);
	
	return payment;
}


  
// These are the javascript code functioning in the app.
// Get the data from user details form and send it to backend using ajax 
// $("document").ready(function(){
// 	$( "#user_submit" ).click(function(event) {
// 		event.preventDefault();
// 		var form = $('#user_form').validate().form();

// 		if (form == true){
// 			$.ajax({
// 				type: 'POST',
// 				url:'/mortgage/user/',
// 				data: {
// 					name:$('#name').val(),
// 					email:$('#email').val(),
// 					mortgage_name:$('#mortgage_config_name').val(),
// 					csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
// 				},
// 				success: function(){
	
// 				}
				
// 			});

// 			$( "#user_form" ).toggle( "slow", function() {
// 				$('#content').load('/mortgage/loan #loan_form', function() {
// 				});
// 			});
	
// 			$("#user_toggle").click(function(){
// 				$( "#user_form" ).toggle( "slow", function() {
// 					});
// 			});

// 		} else {


// 		}
		

		
// 	});
// });
jQuery.browser = {};
(function () {
    jQuery.browser.msie = false;
    jQuery.browser.version = 0;
    if (navigator.userAgent.match(/MSIE ([0-9]+)\./)) {
        jQuery.browser.msie = true;
        jQuery.browser.version = RegExp.$1;
    }
})();


$("document").ready(function() {
	  
	$("#user_form").validate({
	  rules: {
			name: "required",
			email: {
				required: true,
				email: true
			},
			mortgage_config_name: "required",
		},
		messages: {
			name: "Please enter your first name",
			email: "Please enter a valid email address",
			mortgage_config_name: "Please enter a name for this mortgage",
		},

		submitHandler: function(form) {
			$.ajax({
				type: 'POST',
				url:'/mortgage/user/',
				data: {
					name:$('#name').val(),
					email:$('#email').val(),
					mortgage_name:$('#mortgage_config_name').val(),
					csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
				},
				success: function(){
	
				}
				
			});

			$( "#user_form" ).toggle( "slow", function() {
				$('#content').load('/mortgage/loan #loan_form', function() {
				});
			});
	
			$("#user_toggle").click(function(){
				$( "#user_form" ).toggle( "slow", function() {
					});
			});
		}
	});
	
	jQuery.validator.addMethod("lettersonly", function(value, element) {
	  return this.optional(element) || /^[a-z]+$/i.test(value);
	}, "Letters only please"); 

});

function validateForm() {
	var amount = document.forms["loan_form"]["loan_amount"].value;
	var year = document.forms["loan_form"]["year"].value;
	var month = document.forms["loan_form"]["month"].value;
	var rate = document.forms["loan_form"]["rate"].value;
	var extra_monthly = document.forms["loan_form"]["add_per_month"].value;
	var extra_yearly = document.forms["loan_form"]["add_per_year"].value;

    if (amount == "") {
        alert("Loan amount must be filled out");
        return false;
	} else if (amount !=="" && !$.isNumeric(amount)){
		alert("Please enter only numbers for Loan amount")
		return false;
	} else if(year == '' || year > 30){
		alert("Please choose year between range of 1 to 30");
        return false;
	} else if(year !=="" && !$.isNumeric(year)){
		alert("Please choose year between range of 1 to 30");
        return false;
	}else if (rate == ''){
		alert("Rate must be filled out");
		return false;
	} else if(rate !=="" && !$.isNumeric(rate)){
		alert("Please enter only numbers for rate amount. Example: 5, 4.5, etc.");
        return false;
	} else if(extra_monthly =="" || extra_yearly ==""){
		alert("Please enter amount for extra payment");
		return false;
	} else if(extra_monthly > 0 && extra_yearly > 0){
		alert("Please enter amount for either monthly or annual extra payment");
        return false;
	} 
}

// $("document").ready(function(){
// 	$( "#loan_submit" ).click(function(event) {
// 		event.preventDefault();
// 		$.ajax({
// 			type: 'POST',
// 			url:'/mortgage/loan/',
// 			data: {
// 				name:$('#loan_amount').val(),
// 				email:$('#year').val(),
// 				mortgage_name:$('#month').val(),
// 				mortgage_name:$('#rate').val(),
// 				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
// 			},
// 			success: function(){

// 			}
			
// 		});

// 		$( "#loan_form" ).toggle( "slow", function() {
// 			$('#content').load('/mortgage/show_data.html #show_data_form', function() {
// 			});
// 		});
// 	});

// 	$("#loan_toggle").click(function(){
//         $( "#loan_form" ).toggle( "slow", function() {
//             });
//     });

// });



$("document").ready(function() {
	$("#ammortization_table_btn").click(function(){
		$( "#ammortization_table" ).toggle( "slow", function() {
			});
	});
});


$("document").ready(function() {
	$(extra_options_form).hide();
	$("#extra_options").click(function(){
		$( "#extra_options_form" ).toggle( "slow", function() {
			
		});
	});
});



