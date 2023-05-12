/*
Show a modal asking for an email address to see the content, unless the user has already:
- entered an email address (1-year cookie)
- clicked "I'll enter my email later" (12-hour cookie)
- came from a mailing list link, with query param ?code=nBFw6 (1-day cookie)
*/
document.addEventListener("DOMContentLoaded", function () {
  const EMAIL_ADDRESS_COOKIE = "emailAddress";
  const LATER_INTENT_COOKIE = "laterIntent";
  const MAILING_LIST_COOKIE = "mailingList";

  function showModal() {
    document.getElementById("emailModal").style.display = "block";

    // Clicking the "I'll enter my email later" link sets a 12-hour cookie until the modal shows again.
    document.getElementById("emailModalCloseLink").addEventListener("click", function () {
      document.getElementById("emailModal").style.display = "none";

      var numTimes = parseInt(Cookies.get(LATER_INTENT_COOKIE) || 0, 10);
      if (numTimes > 1) {
        Cookies.set(LATER_INTENT_COOKIE, numTimes + 1, { expires: 365 });
      } else {
        var inTwelveHours = new Date(new Date().getTime() + 12 * 60 * 60 * 1000);
        Cookies.set(LATER_INTENT_COOKIE, numTimes + 1, { expires: inTwelveHours });
      }
    });

    // Submitting the form sets a 1-year cookie with the email address, and then submits the form to FormSpark.
    document.getElementById("emailForm").addEventListener("submit", function (event) {
      event.preventDefault();
      document.getElementById("emailModal").style.display = "none";

      var email = document.getElementById("emailInput").value;
      Cookies.set(EMAIL_ADDRESS_COOKIE, email, { expires: 365 });

      // var turnstileResponseElement = document.getElementsByName('cf-turnstile-resonse')[0];
      // var turnstileResponse = (turnstileResponseElement !== undefined) ? turnstileResponseElement.value : null;

      fetch("https://submit-form.com/ozySmLmG", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
        },
        body: JSON.stringify({
          "email": email,
          // "cf-turnstile-response": turnstileResponse,
        }),
      }).then(function (response) {
        // console.log(response);
      }).catch(function (error) {
        console.error(error);
      });

      // Send Google Analytics GA4 event for email address submission in the Spring 2023 LLM Bootcamp modal.
      if (typeof gtag !== "undefined") {
        gtag('event', 'email_address_submission', {
          'event_category': 'engagement',
          'event_label': 'Spring 2023 LLM Bootcamp',
        });
      }
    });
  }

  let url = new URL(window.location.href);

  // Check query params for ?code=nBFw6, which is the code for the mailing list, and if present:
  // - set a 1-day cookie
  // - remove the param from the URL
  let params = new URLSearchParams(url.search);
  let code = params.get('code');
  if (code === "nBFw6") {
    Cookies.set(MAILING_LIST_COOKIE, "true", { expires: 1 });
    params.delete('code');
    url.search = params.toString();
    history.replaceState(null, null, url.toString());
  }

  if (
    url.pathname.startsWith("/llm-bootcamp/spring-2023") &&
    !(Cookies.get(EMAIL_ADDRESS_COOKIE) || Cookies.get(LATER_INTENT_COOKIE) || Cookies.get(MAILING_LIST_COOKIE))
  ) {
      showModal();
    }
  }
);