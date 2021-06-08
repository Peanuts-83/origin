var a = [[1, 2, 1, 24], [8, 11, 9, 4]];
for (let x in a){
  console.log(`row ${x}`);
  for (let y in a[x]){
    console.log(' ' + a[x][y]);
  }
}