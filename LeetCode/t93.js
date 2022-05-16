/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function (s) {
    let p1 = 1
    let p2 = 2
    let p3 = 3
    let p4 = 4
    let pLst = [1, 2, 3, 4]
    let res=[]
    while(true){
        let res=check(s,pLst)
        if(res!==undefined){
            res.push(res)
        }
    }

};

function makeIp(s, p1, p2,
    p3,
    p4) {
    let res = ""
    for (let i = 0; i < s.length; i++) {


    }
}

function makeIp(s, pLst) {
    let res = ""
    for (let i = 0; i < s.length; i++) {
        res += s[i]
        if (pLst.includes(i)) {
            res += "."
        }

    }
    return res
}

function check(s,pLst) {
     let ip =makeIp(s,pLst)
     let sps= ip.split(".")
     for(let ii of sps){
         let numIpToken=parseInt(ii)
         let ok=numIpToken>=0&&numIpToken<=255

         
         if(!ok){
             return undefined
         }
     }
     return ip

    // for (let i = 0; i < s.length; i++) {

    // }
}