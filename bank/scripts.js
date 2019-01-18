// business logic
function Contact(full, city, phone, email, id) {
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
            "You are now done registering. Thank you for using our E-banking system."
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
        $("ul#contacts").append(
            "<li><span class='contact'>" + newContact.fullName() + "</span></li>"
        );
        $(".contact")
            .last()
            .click(function () {
                $("#show-contact").show();
                $("#show-contact h2").text(newContact.fullName);
                $("#show-contact h2")
                    .first()
                    .click(function () {
                        $("h3").toggle();
                        // $(this).remove();
                    });
                $(".full-name").text(newContact.fullName);
                $(".city-name").text(newContact.cityName);
                $(".phone").text(newContact.phonenumber);
                $(".email").text(newContact.userEmail);
                $(".id").text(newContact.userId);
            });
        $("input#new-full-name").val("");
        $("input#new-city-name").val("");
        $("input#new-phone-number").val("");
        $("input#new-e-mail").val("");
        $("input#new-id").val("");

        event.preventDefault();
    });
});
user;

var config = {
    apiKey: "AIzaSyDn2228rz-kwPJJt7wfFVi8FMJdWPg6-iQ",
    authDomain: "group-work-9f3e5.firebaseapp.com",
    databaseURL: "https://group-work-9f3e5.firebaseio.com",
    projectId: "group-work-9f3e5",
    storageBucket: "",
    messagingSenderId: "316520824490"
};
firebase.initializeApp(config);
var db = firebase.database();
try {
    firebase
        .database()
        .ref()
        .child("User")
        .push(newContact).key;
} catch (err) {
    console.log(err);
}
var query = firebase
    .database()
    .ref("User")
    .limitToFirst(20);
query
    .once("value")
    .then(function (snapshot) {
        snapshot.forEach(renderSingleSnapshot);
    })
    .then(function () {
        $(document)
            .find("ul#contacts")
            .html(markup);
    });