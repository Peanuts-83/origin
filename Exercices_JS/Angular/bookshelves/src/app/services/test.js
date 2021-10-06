function delay(msec) {
    return new Promise((resolve, reject) => {
      resolve(setTimeout(msec))
    })
  }


  delay(5000)
    .then(() => {
    console.log('5 sec have passed.')
  })