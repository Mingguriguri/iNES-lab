function calculateDeg(){
  const sun = document.getElementById('my-sun');
  const sun_style = window.getComputedStyle(sun, null);
  const tr = sun_style.getPropertyValue("-webkit-transform") ||
           sun_style.getPropertyValue("-moz-transform") ||
           sun_style.getPropertyValue("-ms-transform") ||
           sun_style.getPropertyValue("-o-transform") ||
           sun_style.getPropertyValue("transform") ||
           "Either no transform set, or browser doesn't do getComputedStyle";
  var values = tr.split('(')[1].split(')')[0].split(',');
  var a = values[0];
  var b = values[1];
  var c = values[2];
  var d = values[3];
  var scale = Math.sqrt(a*a + b*b);
  var sin = b/scale;
  var angle = Math.round(Math.atan2(b, a) * (180/Math.PI));
  const path = document.getElementById('my-path');
  const bg = document.getElementById('my-bg');
  if (Math.abs(angle) >= 90) {
    path.style.backgroundColor = "black";
    bg.style.backgroundColor = "black";
    path.style.transition = "background-color 5s ease";
    bg.style.transition = "background-color 5s ease";
  } else {
    path.style.backgroundColor = "white";
    bg.style.backgroundColor = "white";
    path.style.transition = "background-color 5s ease";
    bg.style.transition = "background-color 5s ease";
  }
}

function get_cloud_left(){
  const cloud = document.getElementById("my-cloud2");
  const rect = cloud.getBoundingClientRect();
  console.log(rect['x'])
  if(rect['x'] > 800){
    cloud.style.animationPlayState = "paused;";
    cloud.style.transform = "translate(-500px, 0);";
    cloud.style.animation = "float1 25s linear;";
  }
}

setInterval(calculateDeg, 1000);
setInterval(get_cloud_left, 1000);
