let nums = [-1,0,1,2,-1,-4]

nums.sort(sequence)
console.log(nums);

// https://www.cnblogs.com/fanda/p/4767984.html
// js sort 问题
function sequence(a,b){
    if (a>b) {
        return 1;
    }else if(a<b){
        return -1
    }else{
        return 0;
    }
}