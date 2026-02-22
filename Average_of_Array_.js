function avg(a) {
  let arr_sum = 0;
  
  for (let i = 0; i < a.length; i ++){
    arr_sum += a[i];
  }
  
  let avg_num = arr_sum / a.length
  return avg_num;
}

const averageNum = avg([2, 4, 6, 8])
console.log(averageNum)
