const strs = ["flow", "flower","flight"]
 
const lcp = (strs) => {
	strs = strs.sort()
  const size = strs.length
  let start = 0, end = Math.min(strs[0].length, strs[size-1].length)
  
  while(start < end && strs[0][start] == strs[size-1][start]){
  	start += 1
  }
  return strs[0].substring(0, start)
}

let res = lcp(strs)
console.log(res)