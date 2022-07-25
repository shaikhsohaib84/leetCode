const arr = [3, 4, 1, 5, 7, 6]
let obj = {}
const target = 7

let lst = arr.filter((ins, idx) => {
    let temp = target - ins;

    if (obj[temp]) {
        console.log([arr[obj[temp] - 1], ins])
    } else {
        obj[ins] = idx + 1
    }
})