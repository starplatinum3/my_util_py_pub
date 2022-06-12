//*[@id="Popover18-content"]/div/div/div[2]/a[1]/div/div[1]/span

// document.getel 

// js XPathEvaluator

// js XPath 获取元素

// https://blog.csdn.net/weixin_44745147/article/details/107764290
//封装xpath
function getElementByXpath(xpath) {
    let evalVal = document.evaluate(xpath, document)
    // evalVal 
    console.log("evalVal");
    console.log(evalVal);
    // var element = document.evaluate(xpath,document).iterateNext();
    var element = evalVal.iterateNext();
    // console.log();
    return element;
}

// #Popover18-content > div > div > div.Messages-list > a:nth-child(1) > div > div.Messages-userName > span
// let name=document.querySelector("#Popover18-content > div > div > div.Messages-list > a:nth-child(1) > div > div.Messages-userName > span")
// let name= getElementByXpath(`*[@id="Popover18-content"]/div/div/div[2]/a[1]/div/div[1]/span`)
// console.log("name");
// console.log(name);

// let Messages_list=document.getElementsByClassName("Messages-list")

// for(let msg of Messages_list){
//     console.log(msg);
// }

let Messages_followItems = document.getElementsByClassName("Messages-item Messages-followItem")

let msgs = []
for (let msg of Messages_followItems) {
    let img = msg.getElementsByClassName("Avatar Avatar--medium UserLink-avatar")[0]
    // console.log(msg);
    // console.log(img);
    // UserLink
    // let UserLink= msg.getElementsByClassName("UserLink")[0]
    let UserLink = msg.getElementsByClassName("UserLink")[1]
    console.log(UserLink);
    let Messages_itemContent = msg.getElementsByClassName("Messages-itemContent")[0]
    let textContentMessages_itemContent = Messages_itemContent.textContent
    let textContentUserLink = UserLink.textContent
    let imgSrc = img.src
    let UserLink_avatar = imgSrc
    //   console.log(imgSrc);
    msgs.push({
        textContentMessages_itemContent,
        textContentUserLink,
        UserLink_avatar
    })
}

console.log(msgs);

// let Messages_followItems=document.getElementsByClassName("Avatar Avatar--medium UserLink-avatar")


// Messages-item Messages-followItem