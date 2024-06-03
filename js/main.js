if (navigator.geolocation) {
if (window.location.pathname === "/foremployee" && latuser.innerHTML === "" && lonuser.innerHTML === "" && myuserid.innerHTML !== "") {
  navigator.geolocation.getCurrentPosition(function(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
	  $.ajax({
		  url:"/location",
		  data:{lat:latitude,lon:longitude},
		  type:'post',
		  success:function(data){
			  var x=data.location;
			  myaddress.innerHTML="";
			  for (var y=0;y<x.length;y++){
			  myaddress.innerHTML+="<form class=\"message\">j'ai déjà visité<span class=\"someaddress\">"+x[y].name+"</span><input value=\"&#9733;\" name=\"etoile1\" class=\"btn btn-link\" type=\"submit\" /><input value=\"&#9733;\" name=\"etoile2\" class=\"btn btn-link\" type=\"submit\" /><input value=\"&#9733;\" name=\"etoile3\" class=\"btn btn-link\" type=\"submit\" /><input value=\"&#9733;\" name=\"etoile4\" class=\"btn btn-link\" type=\"submit\" /><input value=\"&#9733;\" name=\"etoile5\" class=\"btn btn-link\" type=\"submit\" /></form>";
			  }
			  $(".message").submit(function(){
				  return false;
			  });
			  $(".message input[type='submit']").click(function(){
				  var note = ($(this)[0].name.replace("etoile",""));
				  var address = ($($(this)[0].parentElement).children(".someaddress").html());
				  $(".manote").html(note);
				  $(".monadresse").html(address);
				  overlay.style.display="block";
				  return false;
			  });
		  }
	  });
	  $("#envoyernote").click(function(){
		  $.ajax({url:"/sauvernote",
			  type:"post",
			  data:{note:$(".manote").html(),address:$(".monadresse").html(),user_id:myuserid.innerHTML},
			  success:function(){
				  alert("vous avez envoyé la note");
			  }});
		  return false;
	  });

  });
} else if(document.getElementById("member_lat")) {
  navigator.geolocation.getCurrentPosition(function(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
var map = L.map('map').setView([latitude, longitude], 13);
member_lat.value=latitude;
member_lon.value=longitude;
overlay.style.display='block';
L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
setTimeout(function () {
    map.invalidateSize();
}, 0);
	  map.on('mouseup', function(e) {
    const latitude = e.latlng.lat;
    const longitude = e.latlng.lng;
member_lat.value=latitude;
member_lon.value=longitude;
var popup = L.popup()
    .setLatLng([parseFloat(latitude), parseFloat(longitude)])
    .setContent("cette personne est ici")
    .openOn(map);
	  });


  });
} else if(document.getElementById("createjobform")) {
  navigator.geolocation.getCurrentPosition(function(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
var map = L.map('map').setView([latitude, longitude], 13);
myjob_lat.value=latitude;
myjob_lon.value=longitude;
overlay.style.display='block';
L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
setTimeout(function () {
    map.invalidateSize();
}, 0);
	  map.on('mouseup', function(e) {
    const latitude = e.latlng.lat;
    const longitude = e.latlng.lng;
myjob_lat.value=latitude;
myjob_lon.value=longitude;
var popup = L.popup()
    .setLatLng([parseFloat(latitude), parseFloat(longitude)])
    .setContent("votre ami(e) travaille ici")
    .openOn(map);
	  });


  });

} else if(document.getElementById("createphotoform")) {
  navigator.geolocation.getCurrentPosition(function(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
var map = L.map('map').setView([latitude, longitude], 13);
photo_lat.value=latitude;
photo_lon.value=longitude;
overlay.style.display='block';
L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
setTimeout(function () {
    map.invalidateSize();
}, 0);
	  map.on('mouseup', function(e) {
    const latitude = e.latlng.lat;
    const longitude = e.latlng.lng;
photo_lat.value=latitude;
photo_lon.value=longitude;
var popup = L.popup()
    .setLatLng([parseFloat(latitude), parseFloat(longitude)])
    .setContent("cette photo a été  prise ici")
    .openOn(map);
	  });


  });
}
} else {
  console.log("Geolocation is not supported by this browser.");
}
if (document.getElementById("btnlocation")){
btnlocation.onclick=function(){
var fd=new FormData();
fd.set("latitude",btnlocation.dataset.latitude);
fd.set("longitude",btnlocation.dataset.longitude);
fd.set("userid",btnlocation.dataset.userid);
  $.ajax({
    // Your server script to process the upload
    url: "/updatelocation",
    type: "post",

    // Form data
    data: fd,

    // Tell jQuery not to process data or worry about content-type
    // You *must* include these options!
    cache: false,
    contentType: false,
    processData: false,

    // Custom XMLHttpRequest
    success: function (data) {
	    console.log("HEY")
	    console.log(JSON.stringify(data))
	    console.log(JSON.stringify(data.redirect))
	    if (data.redirect){
	    window.location=data.redirect;
	    }else{
	    window.location="/";
	    }
},
    xhr: function () {
      var myXhr = $.ajaxSettings.xhr();
      if (myXhr.upload) {
        // For handling the progress of the upload
        myXhr.upload.addEventListener('progress', function (e) {
          if (e.lengthComputable) {
            $('progress').attr({
              value: e.loaded,
              max: e.total,
            });
          }
        }, false);
      }
      return myXhr;
    }
  });
	return false;
}

}
$(document).ready(function () {
$("#translatebtn").click(function(){

	var url="/translate";
	console.log(url,sometext1.value);
	$.ajax({url:url,
		type:"post",
		data:{somecontent: sometext1.value},
		success:function(data){
			var pic=data.content;
	$("#sometext2").val(pic);
		}});
	return false;
});
$("#pays_telephone, [name=sex]").change(function(){

	var url="/chercherimage/"+$("[name=sex]:checked").val()+"/"+$("#pays_telephone").val();
	console.log(url);
	$.ajax({url:url,
		success:function(data){
			var pic=data.images;
	$(someurl).html("<p>"+data.q+"</p>");
			for (var i=0;i<pic.length;i++){
	$(someurl).append(`
	<div class="champ">
	<input id="image${i+1}" ${i == 0 ? "checked" : ""} value="${pic[i].src}" name="someurl" type="radio"/>
	<label for="image${i+1}"><img src="${pic[i].src}" width=200 height=200 />image ${i+1}</label>
	</div>
		`
	);
			}
		}});
})
      $('.someselect').selectize({
          sortField: 'text'
      });
  });

