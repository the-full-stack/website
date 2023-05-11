document.addEventListener("DOMContentLoaded", function () {
  function showModal() {
    document.getElementById("emailModal").style.display = "block";

    document.getElementById("emailModalCloseLink").addEventListener("click", function () {
      var inTwelveHours = new Date(new Date().getTime() + 12 * 60 * 60 * 1000);
      Cookies.set("email", "later", { expires: inTwelveHours });
      document.getElementById("emailModal").style.display = "none";
    });

    document.getElementById("emailForm").addEventListener("submit", function (event) {
      event.preventDefault();

      var email = document.getElementById("emailInput").value;
      Cookies.set("email", email, { expires: 365 });

      document.getElementById("emailModal").style.display = "none";

      fetch("https://submit-form.com/ozySmLmG", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
        },
        body: JSON.stringify({
          "email": email,
          "g-recaptcha-response": captchaResponse,
        }),
      }).then(function (response) {
        // console.log(response);
      }).catch(function (error) {
        console.error(error);
      });
    });
  }

  var urlPath = window.location.pathname;
  if (
    urlPath.startsWith("/llm-bootcamp/spring-2023") &&
    !Cookies.get("email")
  ) {
    showModal();
  }
});
