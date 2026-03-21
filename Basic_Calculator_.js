function calculate(a, operator, b) {
  let expression = String(a) + " " + operator + " " + String(b);
  const operators = ['+', '-', '*', '/'];

  if((!operators.includes(operator)) || (operator === "/" && b === 0)) {
    return null;
  }
  else {
    return eval(expression);
  }
}
