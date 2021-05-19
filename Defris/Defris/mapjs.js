document.getElementById("africa").style = "fill:#ffff66";
document.getElementById("australia").style = "fill:#ffff66";
document.getElementById("north_america").style = "fill:#0000cc";
document.getElementById("south_america").style = "fill:#66ccff";
document.getElementById("europe").style = "fill:#00ff99";
document.getElementById("asia").style = "fill:#ff0000";

//document.getElementById("africaN").style = "fill:#cc9900";
//document.getElementsByClassName("africaS").style = "fill:#ffff00";
//document.getElementById("africaV").style = "fill:#ffff99";
//document.getElementById("africaE").style = "fill:#ffff99";


//document.getElementById("path2415").style = "fill:#ff9955";
//var fs = require('fs');
//fs.readFile('demofile1.html', function(err, data) {
    //res.writeHead(200, {'Content-Type': 'text/html'});
    //res.write(data);
    //return res.end();
  //});

/*
$(document).ready(function() {
    $.ajax({
        url: "test.csv",
        dataType: "text",
        success: function(data) {processData(data);}
     });
    
     function processData(allText) {
         alert("1");
     }
    });
    */
         /*
        alert(allText);
        var allTextLines = allText.split(/\r\n|\n/);
        var headers = allTextLines[0].split(',');
        var lines = [];
    
        for (var i=1; i<allTextLines.length; i++) {
            var data = allTextLines[i].split(',');
            if (data.length == headers.length) {
    
                var tarr = [];
                for (var j=0; j<headers.length; j++) {
                    tarr.push(headers[j]+":"+data[j]);
                }
                lines.push(tarr);
            }
        }
        
       // alert(lines);
    }
});*/
/*
readTextFile("1980-2030_region_predictions.csv");

function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, true);
    alert("0");
    alert(rawFile.responseText);
    rawFile.onreadystatechange = function ()
    {
        alert("1");
        if(rawFile.readyState === 4)
        {
            alert("2");
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                alert(allText);
            }
        }
    }
    //rawFile.send(null);
}
*/


var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
  //alert(txtFile);
}


function changeColorOfId(id)
{
    document.getElementById(id).style = "fill:#ff9955";
}