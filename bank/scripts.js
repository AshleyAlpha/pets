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