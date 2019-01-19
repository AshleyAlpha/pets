var ox = function (name) {
    this.name = name;

}

0x.prototype.fullName = function () {
    return this.name;
};
$(document).ready(function () {

    $("form#detail").submit(function (event) {
        event.preventDefault();
        var fullName = $("input#fullname").val();
        var Name = Name(fullName);

        var inputDeposit = parseInt($("input#initial-deposit").val());
        $("#user-info").show();
        $("form#detail").hide();
        $("#user-info h1").text(newName.fullName());
        $("#user-info h4").text(newAdress.inputDeposit);

        $("#deposit").click(function () {
            $("#bank-deposit").toggle();
            $("#withdraw").hide();
        });

        $("#withdraw").click(function () {
            $("#bank-withdraw").toggle();
            $("#deposit").hide();
        });

        $("#tdeposit").click(function () {
            var depositAmount = parseInt($("input#deposit-amount").val());
            var newBalance = inputDeposit + depositAmount;
            console.log(newBalance)

            $("#ac-balance").show();
            $("#bank-deposit").hide();
            $("#user-info").hide();
            $("#demo").text(newBalance)
        })
        $("#withdraw").click(function () {
            var withdrawAmount = parseInt($("input#withdraw-amount").val());
            var newBalance = inputDeposit - withdrawAmount;
            console.log(newBalance)

            $("#ac-balance").show();
            $("#demo").text(newBalance)
        })


    });


})