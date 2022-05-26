$(document).ready(function(){
    $.ajax("https://swapi-api.hbtn.io/api/people/5/?format=json",
        {
            success: function(data){
                $("#character").append(data.name)
            }
        }
    )
})