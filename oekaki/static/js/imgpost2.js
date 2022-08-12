let btn = document.getElementById("submit");
btn.addEventListener("click", function(){
    let canvas = document.getElementById("draw-area");

    const data = canvas.toDataURL("image/png");
    //console.log(data);

    $.ajax({
        url: `${window.location.origin}/imgpost`,
        type: "POST",
        data: {"postimg": data},
        dataType: "json",
        success: function(data){
            console.log("成功");
        }
    })
});
