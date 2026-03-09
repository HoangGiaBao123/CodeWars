function tiyFizzBuzz(sentence) {
  let letters = sentence.split("");
  const vowels = ['a','u','i','e','o','A','U','I','E','O'];
  for(let i = 0; i < letters.length; i++) {
    if(letters[i] != " " && letters[i].toLowerCase() !== letters[i].toUpperCase()){
      if(letters[i] === letters[i].toLowerCase() && vowels.includes(letters[i])) {
        letters[i] = "Yard";
      }
      else if(letters[i] === letters[i].toUpperCase() && vowels.includes(letters[i])) {
        letters[i] = "Iron Yard";
      }
      else if(letters[i] === letters[i].toUpperCase() && vowels.includes(letters[i]) === false) {
        letters[i] = "Iron";
      }
    }
    else {
      
    }
  }
  return letters.join('')
