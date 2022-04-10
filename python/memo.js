const memo = () => {
    let cache = {}
    return (...args) => {
        let cacheKey = args.toString()
        if(cacheKey in cache){
            console.log('from cache')
            return cache[cacheKey]
        } else{
            let res = args.reduce((acc, curr) => { 
                return acc+curr
                }, 0)
            console.log('NOT from cache')
            cache[cacheKey] = res
            return cache[cacheKey]
        }
    }
}

let m = memo()
console.log(m(1, 2))
console.log(m(1, 2))