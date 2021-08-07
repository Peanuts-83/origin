function checkCashRegister(price, cash, cid) {
  let change = {
      status: 'OPEN',
      change: [],
    },
    cashInDraw = Object.fromEntries(cid);

  const money = {
    'ONE HUNDRED': 100,
    TWENTY: 20,
    TEN: 10,
    FIVE: 5,
    ONE: 1,
    QUARTER: 0.25,
    DIME: 0.1,
    NICKEL: 0.05,
    PENNY: 0.01,
  };

  for (let key of Object.keys(money)) {
    let diff = cash - price,
      coinVal = money[key],
      numCoinNeeded = Math.floor(diff / coinVal),
      numCoinInCid = cashInDraw[key] / coinVal,
      inCid =
        numCoinNeeded < numCoinInCid ? numCoinNeeded * coinVal : cashInDraw[key],
      cashInDrawSum = Object.values(cashInDraw)
        .reduce((acc, x) => acc + x)
        .toFixed(2);

    if (diff >= coinVal) {
      console.log(
        'diff: ' +
          diff +
          ', coinVal:' +
          coinVal +
          ' numCoinNeeded: ' +
          numCoinNeeded +
          ' numCoinInCid: ' +
          numCoinInCid +
          ' cashInDrawSum: ' +
          cashInDrawSum
      );
      console.log(' cid: ' + cid);

      change.change.push([key, inCid]);
      diff = (diff - inCid).toFixed(2);
      
      console.log('taken from cid: ' + inCid + ' new diff: ' + diff)

      // final check
      if (coinVal == 0.01 && diff > 0) {
        change.status = 'INSUFFICIENT_FUNDS';
        change.change = [];
        return change;
      } else if (
        coinVal == 0.01 &&
        diff == 0
      ) {
        change.status = 'CLOSED';
        return change;
      } else if (coinVal == 0.01 || diff == 0) {
        return change;
      }
    }
  }
}
/*
checkCashRegister(19.5, 20, [
  ['PENNY', 1.01],
  ['NICKEL', 2.05],
  ['DIME', 3.1],
  ['QUARTER', 4.25],
  ['ONE', 90],
  ['FIVE', 55],
  ['TEN', 20],
  ['TWENTY', 60],
  ['ONE HUNDRED', 100],
]);

checkCashRegister(3.26, 100, [
  ['PENNY', 1.01],
  ['NICKEL', 2.05],
  ['DIME', 3.1],
  ['QUARTER', 4.25],
  ['ONE', 90],
  ['FIVE', 55],
  ['TEN', 20],
  ['TWENTY', 60],
  ['ONE HUNDRED', 100],
]);

checkCashRegister(19.5, 20, [
  ['PENNY', 0.01],
  ['NICKEL', 0],
  ['DIME', 0],
  ['QUARTER', 0],
  ['ONE', 0],
  ['FIVE', 0],
  ['TEN', 0],
  ['TWENTY', 0],
  ['ONE HUNDRED', 0],
]);
*/
checkCashRegister(19.5, 20, [
  ['PENNY', 0.5],
  ['NICKEL', 0],
  ['DIME', 0],
  ['QUARTER', 0],
  ['ONE', 0],
  ['FIVE', 0],
  ['TEN', 0],
  ['TWENTY', 0],
  ['ONE HUNDRED', 0],
]);
