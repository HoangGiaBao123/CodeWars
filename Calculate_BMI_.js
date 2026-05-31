function bmi(weight, height) {
  const bodyMassIndex = weight / Math.pow(height, 2);
  if(bodyMassIndex <= 18.5) {
    return "Underweight";
  } else if(bodyMassIndex <= 25) {
    return "Normal";
  } else if(bodyMassIndex <= 30) {
    return "Overweight";
  } return "Obese";
}
