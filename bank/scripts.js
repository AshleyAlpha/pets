// business logic
function details(full, city, phone, email, id) {
    this.fullName = full;
    this.cityName = city;
    this.userEmail = email;
    this.phonenumber = phone;
    this.userId = id;
}
Contact.prototype.fullName = function () {
    return this.fullName;
};

// user interface logic
$(document).ready(function () {
            $("#hidden1").hide();
            $("#hidden2").hide();
            $("form#new-contact").submit(function (event) {
                        alert(
                            "You are now done registering. Thank  you for banking with our E-banking system."
                        );
                        var inputtedFirstName = $("input#new-full-name").val();
                        var inputtedLastName = $("input#new-city-name").val();
                        var inputtedPhone = $("input#new-phone-number").val();
                        var inputtedEmail = $("input#new-e-mail").val();
                        var inputtedId = $("input#new-id").val();
                        var newContact = new Contact(
                            inputtedFullName,
                            inputtedCityName,
                            inputtedPhone,
                            inputtedEmail,
                            inputtedId
                        );