
var xmlhttp = new XMLHttpRequest();
var token = localStorage.getItem("auth_token") ;
var url = "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token="+token;

xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        console.log(myArr);
        myFunction(myArr);
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send();

function myFunction(arr) {
    document.getElementById("user_name").innerHTML = 'email:'+arr.email;
}