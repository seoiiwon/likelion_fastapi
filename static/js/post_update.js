postForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  let subject = document.getElementById("subject").value;
  let content = document.getElementById("content").value;
  let post_id = document.querySelector("script").getAttribute("data_post_id");

  if (confirm("저장하시겠습니까?")) {
    try {
      let response = await fetch(`/api/post/update/${post_id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          post_id: post_id,
          subject: subject,
          content: content,
        }),
      });

      if (response.ok) {
        window.location.href = "/api/post/list";
      } else {
        let errorMessage = await response.text();
        throw new Error(errorMessage);
      }
    } catch (error) {
      console.error("요청 실패:", error);
      alert("요청을 처리하는 중 오류가 발생했습니다.");
    }
  }
});



