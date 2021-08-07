function checkCashRegister(price, cash, cid) {
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
  
    let change = {
        status: 'OPEN',
        change: [],
      },
      cashInDraw = Object.fromEntries(cid),
      diff = cash - price;
  
    for (let key of Object.keys(money)) {
      let coinVal = money[key],
        cashInDrawSum = Object.values(cashInDraw)
          .reduce((acc, x) => acc + x)
          .toFixed(2),
        numCoinNeeded = Math.floor(diff / coinVal),
        numCoinInCid = cashInDraw[key] / coinVal,
        inCid =
          numCoinNeeded < numCoinInCid
            ? numCoinNeeded * coinVal
            : cashInDraw[key];
  
      if (diff >= coinVal) {
        console.log(
          key +
            ': diff: ' +
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
  
        change.change.push([key, inCid]);
        diff = (diff - inCid).toFixed(2);
        cashInDraw[key] -= inCid;
  
        console.log('taken from cid: ' + inCid + ' new diff: ' + diff);
        cashInDrawSum = Object.values(cashInDraw)
          .reduce((acc, x) => acc + x)
          .toFixed(2);
        console.log(cashInDrawSum);
  
        // final check
        if (coinVal == 0.01 && diff > 0) {
          change.status = 'INSUFFICIENT_FUNDS';
          change.change = [];
          return change;
        } else if (key == 'PENNY' && diff == 0 && cashInDrawSum == 0) {
          change.status = 'CLOSED';
          change.change = cid;
          return change;
        } else if (key == 'PENNY' || diff == 0) {
          return change;
        }
      }
    }
  }s