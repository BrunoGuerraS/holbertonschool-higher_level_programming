$(document).ready(function(){
    $("#add_item").on("click", function(){
        console.log("hey!!!!!!")
        $(".my_list").append("<li>Item</li>")
    })
})