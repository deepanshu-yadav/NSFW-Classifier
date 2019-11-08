

var API_ENDPOINT = "https://7ul4fiq2v1.execute-api.us-east-2.amazonaws.com/final_stage"
 
document.getElementById('inp').onchange = function(e) {
    var img = new Image();
    img.onload = draw;
    img.onerror = failed;
    img.src = URL.createObjectURL(this.files[0]);
    console.log(img.src);
  };
  function draw() {
    var canvas = document.getElementById('canvas');
    canvas.width = this.width;
    canvas.height = this.height;
    var ctx = canvas.getContext('2d');
    ctx.drawImage(this, 0,0);
    console.log("painted");
  }
  function failed() {
    alert("The provided file couldn't be loaded as an Image media");
};
 
document.getElementById("genre").onclick = function(){
    var canvas = document.getElementById("canvas")
    var image = canvas.toDataURL()
	  var inputData = {"data": image};
    console.log(inputData);
    $.ajax({
      url: API_ENDPOINT,
      type: 'POST',
      crossDomain: true,
      data: JSON.stringify(inputData),
      dataType: 'json',
      contentType: "application/json",
      success: function (response) {
	 console.log(response);
        document.getElementById("genreReturned").textContent = response;
      },
  });
}
