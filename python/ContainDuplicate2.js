const duplicate = (array, num) => {
    let isTrue = false, obj = {}
    for (const[index, elem] of array.entries()){
      if(elem in obj && obj.elem - index <= num){
        isTrue = True
        return isTrue
      }
      obj[elem] = index
    }
    return isTrue
  }
  let array = [1,2,3,1], num = 3
  res = duplicate(array, num)
  console.log(res)