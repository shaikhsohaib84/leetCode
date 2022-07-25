const arr = [1,2,3,4,5]

const setTimeOut = (arr) => {
    for(var i = 0; i < arr.length; i++) {
        function exe(i) {
            setTimeout(() => {
                console.log(arr[i])
            }, i*1000);
        }
        exe(i)
    }
}

setTimeOut(arr)