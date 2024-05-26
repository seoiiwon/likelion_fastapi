document.getElementById("update").addEventListener("click", function () {
  let post_id = document.querySelector("script").getAttribute("data_post_id");
  window.location.href = `/api/post/update/${post_id}`;
});

document.getElementById("delete").addEventListener("click", function () {
  const post_id = document.querySelector("script").getAttribute("data_post_id");

  if (confirm("삭제하시겠습니까?")) {
    fetch(`/api/post/delete/${post_id}`, {
      method: "DELETE",
    }).then(() => {
      window.location.reload();
      window.location.href = "/api/post/list";
    });
  } else {
    return;
  }
});

document.getElementById("comment").addEventListener("click", function () {
  let post_id = document.querySelector("script").getAttribute("data_post_id");
  window.location.href = `/api/comment/list/${post_id}`;
});
