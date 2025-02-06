document.getElementById("words-btn").addEventListener("click", function () {
  alert("Navigate to the Words Learning Section");
});

document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("alphabet-btn")
    .addEventListener("click", function () {
      fetch("/learn-alphabets", {
        method: "POST",
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === "success") {
            // Handle success (e.g., show a message or update the page)
            alert(data.message);
          } else {
            // Handle error
            alert("An error occurred: " + data.message);
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("An error occurred.");
        });
    });
});
