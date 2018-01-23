// Wrapper for Filesaver.js
function export_json() {
  var data = JSON.stringify(document.getElementById("export_output_textarea").value);
  var blob = new Blob([data], {type: "application/octet-stream"});
  var username = document.getElementById("username_text").value;
  var reponame = document.getElementById("reponame_text").value;
  var cogname = document.getElementById("cogname_text").value;
  var filename = username + "-" + reponame + "-" + cogname + "-info.json";
  saveAs(blob, filename);
}

function copy_json() {
  var data = document.getElementById("export_output_textarea").value;
  alert(data)
}
