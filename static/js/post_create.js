let postForm = document.getElementById("postForm");

postForm.addEventListener("submit", (event) => {
  event.preventDefault();

  if (confirm("ㄹㅇ 저장?")) {
    let subject = document.getElementById("subject").value;
    let content = document.getElementById("content").value;

    fetch("/api/post/create", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ subject: subject, content: content }),
    }).then(() => {
      window.location.href = "/api/post/list";
    });
  } else {
    return;
  }
});


