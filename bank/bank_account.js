ox.objectbasics.BankAccount = function (name, balance) {
    this.name = name;
    this.balance = balance;
}

ox.objectbasics.BankAccount.prototype.deposit = function (amount) {
    this.balance += amount;
};

ox.objectbasics.BankAccount.prototype.withdraw = function (amount) {
    this.balance -= amount;
};


ox.objectbasics.BankAccount.prototype.toString = function () {
    return "Name: " + this.name + "Balance:" + this.balance
};