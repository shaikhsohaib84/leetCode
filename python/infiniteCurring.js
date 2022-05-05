const add = (val) => {
  return (b) => {
    if (b) return add(val + b);
    return val;
  };
};

const t = add(1)(2)(3)();
console.log(t);

