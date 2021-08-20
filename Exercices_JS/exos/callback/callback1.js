function loadScript(src, callback) {
  // creates a <script> tag and append it to the page
  // this causes the script with given src to start loading and run when complete
  let script = document.createElement('script');
  script.src = src;
  script.onload = () => callback(null, script);
  script.onerror = () => callback(new Error(`script load error for ${src}`));

  document.head.append(script);
}

loadScript('script.js', function(err, res) {
  if (err) {
    alert('Error: ' + err);
  } else {
    alert('Result: ' + res);
  }
});
