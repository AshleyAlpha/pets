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




                        0x.prototype.fullName = function () {
                            returnthis.balance += amount;
                        };

                        ox.objectbasics.BankAccount.prototype.withdraw = function (amount) {
                            this.balance -= amount;
                        };


                        ox.objectbasics.BankAccount.prototype.toString = function () {
                            return "Name: " + this.name + "Balance: rwf" + this.balance
                        };