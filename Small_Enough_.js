function smallEnough(arr, limit){
  const array = arr.filter((n) => n <= limit);
  return JSON.stringify(array.sort()) == JSON.stringify(arr.sort())
}
