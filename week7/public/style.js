document.querySelector("#name").addEventListener("click", function () {
  let username = document.querySelector("#input-name").value;
  let url = "http://127.0.0.1:3000/api/member?username=" + username;

  fetch(url)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      let result = document.querySelector("#searchName");
      //result.innerHTML = "";

      let clist = data.data;
      let name = clist.name;
      let username = clist.username;

      result.innerHTML = name + " (" + username + ")";
    })
    .catch(function (error) {
      result.innerHTML = "查無此人！！";
    });
});

document.querySelector("#changeName").addEventListener("click", function () {
  let newName = document.querySelector("#input-changeName").value;
  console.log(newName);
  let url = "http://127.0.0.1:3000/api/member";
  fetch(url, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name: newName }), //發送JSON格式資料給後端
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
      let result = document.querySelector("#newName");
      if (data["ok"]) {
        result.innerHTML = "更新成功";
      }
    });
});
