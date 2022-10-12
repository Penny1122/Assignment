//要求三：JavaScript 取得網路上的資料並顯示在網頁畫面中
//document.createElement("標籤") //建立<標籤>
//setAttribute('src', img_list[1])   // 設定<img src='img_list[1]' />，取得第一張圖片的網址
//document.getElementsByClassName("x")[i].appendChild(標籤)   // 將<img/>附加到<div class='x'>之中
//document.createTextNode(clist[i].stitle)   // 建立text node，文字為clist中的stitle
fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
.then(function(response){
    return response.json();
})
.then(function(data) {
    let clist = data.result.results
    //console.log(clist);
    for (let i=0; i<2; i++){
        //img 標籤
        let img_Link = clist[i].file.replaceAll("https", " https").split(" ");
        //console.log(img_Link);
        let img_Tag = document.createElement("img"); //建立<img/>
        img_Tag.setAttribute("src", img_Link[1]); //將scr="img_Link[1]" 放入img_Tag中
        document.querySelectorAll(".catframe")[i].appendChild(img_Tag); //將img_Tag 放入 <div class="catframe"> </div>中(html中已有<div class="catframe"> </div>)
        //div 標籤
        let promotion_Tag = document.createElement("div"); //建立<div> </div>
        promotion_Tag.setAttribute("class", "promotion"); //<div class="promotion"> </div>
        let promotion_Text = document.createTextNode(clist[i].stitle); //取得clist[i].stile的文字
        //console.log(promotion_Text);
        promotion_Tag.appendChild(promotion_Text); //將promotion_Text放入promotion_Tag <div>標籤內 => <div class="promotion">clist[i].stile</div>
        document.querySelectorAll(".catframe")[i].appendChild(promotion_Tag); //將promotion_Tag 放入 <div class="catframe"> </div>中(html中已有<div class="catframe"> </div>)
    }
    for (let j=2; j<10; j++){
        //img 標籤
        let img_Link = clist[j].file.replaceAll("https", " https").split(" ");
        //console.log(img_Link);
        let img_Tag = document.createElement("img"); 
        img_Tag.setAttribute("src", img_Link[1]); 
        document.querySelectorAll(".titleframe")[j-2].appendChild(img_Tag); 
        //div 標籤
        let promotion_Tag = document.createElement("div"); 
        promotion_Tag.setAttribute("class", "title-text"); 
        let promotion_Text = document.createTextNode(clist[j].stitle); 
        //console.log(promotion_Text);
        promotion_Tag.appendChild(promotion_Text); 
        document.querySelectorAll(".titleframe")[j-2].appendChild(promotion_Tag); 
    }
})
