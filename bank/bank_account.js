var ox = function (name) {
    this.name = name;

}

0x.prototype.fullName = function () {
    return this.name;
};
$(document).ready(function () {

            $("form#contact").submit(function (event) {
                        event.preventDefault();
                        var firstName = $("input#firstname").val();
                        var lastName = $("input#lastname").val();
                        var newName = new Name(firstName, lastName);

                        var inputEmail = $("input#e-mail").val();
                        var inputNumber = $("input#p-number").val();
                        var inputDeposit = parseInt($("input#initial-deposit").val());
                        var newAdress = new Adresses(inputEmail, inputNumber, inputDeposit);






                        0x.prototype.fullName = function () {
                            returnthis.balance += amount;
                        };

                        ox.objectbasics.BankAccount.prototype.withdraw = function (amount) {
                            this.balance -= amount;
                        };


                        ox.objectbasics.BankAccount.prototype.toString = function () {
                            return "Name: " + this.name + "Balance: rwf" + this.balance
                        };