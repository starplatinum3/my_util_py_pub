/**
 * @param {number} n
 * @return {string[]}
 */
 var generateParenthesis = function(n) {

    // let res=[]
    let res=new Set()
    dfs(0,"",n,res)
    // console.log("res");
    // console.log(res);
   
    // return res
    return  [...res]
};

function dfs(num,str,endNum,lst){
    if(num===endNum){
        // lst.push(str)
        lst.add(str)
        return
    }
    let nextNum=num+1
    dfs(nextNum,"()"+str,endNum,lst)
    dfs(nextNum,"("+str+")",endNum,lst)
    dfs(nextNum,str+"()",endNum,lst)

}

 let resLst= generateParenthesis(3)
 console.log("resLst"); 
 console.log(resLst);