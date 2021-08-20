////////////////////////////////////////////////////////////////////////
// CALLBACK / function getting other function to be called / args >> error, result

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

  ////////////////////////////////////////////////////////////////////////
  // PROMISE / asynchronous request pending till resolve/reject / .then/catch/finally to manage response
  // args >> resolve, reject

  let promise = new Promise(function (resolve, reject) {
    // after 1 second signal that the job is finished with an error
    setTimeout(() => reject(new Error('Whoops!')), 3000);
  })
    .finally(console.log('Loading done, data ready to process.'))
    .then((result) => console.log(result))
    .catch((error) => console.log(error))
    .finally(console.log('Processing done.'));
  
    //////////////////////////////////////////////////////////////////////
    // ASYNC/AWAIT / Async to function returns promise / Await only with Async

    async function wait() {
        //await new Promise((resolve, reject) => setTimeout(reject(new Error('failed!')), 1000));
        let a = '10'
        let b = await new Promise((resolve, reject) => setTimeout(resolve, 1000));
        return a;
      }
      function f() {
        wait().then((response) => console.log(response)).catch(err => console.log(err));
      }
      
      f();

