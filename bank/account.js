var ox = ox || {};
ox.objectbasics = ox.objectbasics || {};
$(document).ready(function () {

    var peter = new ox.objectbasics.BankAccount("Peter", 100);
    console.log(peter.toString());
    peter.deposit(50);
    console.log(peter.toString());
});