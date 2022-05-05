const arr = [[1, 2], [3], [4, 5, [6]], [7, 8]];

let result = [];
const flattend = (arr) => {
  arr.forEach((element, index) => {
    if (Array.isArray(element)) {
      flattend(element);
    } else {
      result.push(element);
    }
  });
};
flattend(arr);