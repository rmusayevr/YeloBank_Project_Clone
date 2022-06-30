const rangeInputs = document.querySelectorAll('input[type="range"]')

function handleInputChange(e) {
  let target = e.target
  const min = target.min
  const max = target.max
  const val = target.value
  target.style.backgroundSize = (val - min) * 100 / (max - min) + '% 100%'
  }
rangeInputs.forEach(input => {
  input.addEventListener('input', handleInputChange)
})


function change_montly_pay() {
  var interest = 0.0108333333
  var x = parseFloat(Math.pow(1 + interest, parseFloat($('#period').val())));
  var monthly = (parseFloat($('#amount').val())*x*interest)/(x-1);
  $('#monthly_pay').text(parseFloat(monthly).toFixed(2))
  $('#monthly_pay').val(parseFloat(monthly).toFixed(2))
}

change_montly_pay()

function check_salary_for_period() {
  let salaryRange = $("#salary").val()
  let monthly_pay = $('#monthly_pay').val()
  if (parseFloat(monthly_pay) > parseFloat(salaryRange)){
    backgroundSizeOfPeriodRange = '100% 100%';
    $("#period_range").val(48); 
    $('#period_range').css("background-size", backgroundSizeOfPeriodRange);
    change_montly_pay()
  }
  else {
    change_montly_pay()
    const minPeriod = $('#period')[0].min;
    const maxPeriod = $('#period')[0].max;
    const valPeriod = $('#period').val();
    backgroundSizeOfPeriodRange = (valPeriod - minPeriod) * 100 / (maxPeriod - minPeriod) + '% 100%';
    $('#period_range').css("background-size", backgroundSizeOfPeriodRange);
      
  }
}
function check_salary_for_amount() {
  periodRangeValue = $("#period_range").val(); 
  if (periodRangeValue == 48) {
    let salaryRange = $("#salary").val()
    let monthly_pay = $('#monthly_pay').val()
    if (parseFloat(monthly_pay) > parseFloat(salaryRange)){
      const minAmount = $('#amount')[0].min;
      const maxAmount = $('#amount')[0].max;
      const valAmount = $('#amount').val() ;
      const newValAmount = $('#amount').val(valAmount-3000)
      backgroundSizeOfAmountRange = (newValAmount - minAmount) * 100 / (maxAmount - minAmount) + '% 100%';
      $('#amount_range').css("background-size", backgroundSizeOfAmountRange);
      change_montly_pay()
    }
  }
}

$("#salary_range, #amount_range, #period_range").on("input change", function() {
  let salaryRange = $("#salary_range").val()
  $("#salary").val(salaryRange)
  let amounRange = $("#amount_range").val()
  $("#amount").val(amounRange)
  let periodRange = $("#period_range").val()
  $("#period").val(periodRange)
  check_salary_for_period()
  check_salary_for_amount()
})


$('#salary, #period, #amount').on("input change", function() {
      let salary = $('#salary').val()
      if (salary < 350) $("#salary").val(350);
      if (salary > 14950) $("#salary").val(14950);
      $("#salary_range").val(salary);
      const minSalary = $('#salary')[0].min;
      const maxSalary = $('#salary')[0].max;
      const valSalary = $('#salary').val();
      backgroundSizeOfSalaryRange = (valSalary - minSalary) * 100 / (maxSalary - minSalary) + '% 100%';
      $('#salary_range').css("background-size", backgroundSizeOfSalaryRange);
      let amount = $("#amount").val();
      if (amount < 300) $("#amount").val(300);
      if (amount > 30000) $("#amount").val(30000);
      $("#amount_range").val(amount);
      const minAmount = $('#amount')[0].min;
      const maxAmount = $('#amount')[0].max;
      const valAmount = $('#amount').val();
      backgroundSizeOfAmountRange = (valAmount - minAmount) * 100 / (maxAmount - minAmount) + '% 100%';
      $('#amount_range').css("background-size", backgroundSizeOfAmountRange);
      let period = $("#period").val()
      if (period < 6) $("#period").val(6);
      if (period > 48) $("#period").val(48);
      $("#period_range").val(period);
      const minPeriod = $('#period')[0].min;
      const maxPeriod = $('#period')[0].max;
      const valPeriod = $('#period').val();
      backgroundSizeOfPeriodRange = (valPeriod - minPeriod) * 100 / (maxPeriod - minPeriod) + '% 100%';
      $('#period_range').css("background-size", backgroundSizeOfPeriodRange);
      check_salary_for_period()
      check_salary_for_amount()
    })

let dollarValue = document.getElementById("dollar_price").innerHTML
let euroValue = document.getElementById("euro_price").innerHTML
let aznValueForUSD = document.getElementById("azn_price_for_usd").innerHTML
let aznValueForEUR = document.getElementById("azn_price_for_eur").innerHTML


$('#selling').on("input change", function() { 
  if ($("#buying_select").val() == "USD") {
    $('#buying').text(parseFloat($("#selling").val()/parseFloat(dollarValue).toFixed(4)).toFixed(2))
  } else if ($("#buying_select").val() == "EUR") {
    $('#buying').text(parseFloat($("#selling").val()/parseFloat(euroValue).toFixed(4)).toFixed(2))
  } 
  $("#buying_select").change(function () {
    if ($("#buying_select").val() == "USD") {
      $('#buying').text(parseFloat($("#selling").val()/parseFloat(dollarValue).toFixed(4)).toFixed(2))
    } else if ($("#buying_select").val() == "EUR") {
      $('#buying').text(parseFloat($("#selling").val()/parseFloat(euroValue).toFixed(4)).toFixed(2))
    } 
  })
});


$(document).ready(function () {
  $("#selling_select").change(function () {
      var val = $(this).val();
      if (val == "AZN") {
          $("#buying_select").html("<option value='USD'>USD</option><option value='EUR'>EUR</option>");
          if ($("#buying_select").val() == "USD") {
            $('#buying').text(parseFloat($("#selling").val()/parseFloat(dollarValue).toFixed(4)).toFixed(2))
          } else if ($("#buying_select").val() == "EUR") {
            $('#buying').text(parseFloat($("#selling").val()/parseFloat(euroValue).toFixed(4)).toFixed(2))
          } 
          $("#buying_select").change(function () {
            if ($("#buying_select").val() == "USD") {
              $('#buying').text(parseFloat($("#selling").val()/parseFloat(dollarValue).toFixed(4)).toFixed(2))
            } else if ($("#buying_select").val() == "EUR") {
              $('#buying').text(parseFloat($("#selling").val()/parseFloat(euroValue).toFixed(4)).toFixed(2))
            } 
          })
      } else if (val == "USD") {
          $("#buying_select").html("<option value='AZN'>AZN</option>");
          $('#buying').text(parseFloat($("#selling").val()*parseFloat(aznValueForUSD).toFixed(4)).toFixed(2))
      } else if (val == "EUR") {
          $("#buying_select").html("<option value='AZN'>AZN</option>");
          $('#buying').text(parseFloat($("#selling").val()*parseFloat(aznValueForEUR).toFixed(4)).toFixed(2))
      }
  });
});
