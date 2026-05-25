function highAndLow(numbers){
  const nums = numbers.split(" ").map(Number)
  let maximum = nums[0]
  let minimum = nums[0]
  for(let num of nums) {
    if(num > maximum) {
      maximum = num
    }
  }
  for(let num of nums) {
    if(num < minimum) {
      minimum = num
    }
  }
  return `${maximum} ${minimum}`
