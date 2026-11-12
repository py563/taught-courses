(function () {
  var form = document.getElementById("teaching-contact-form");
  if (!form) return;

  var workerUrl = form.getAttribute("data-worker-url");
  var source = form.getAttribute("data-source") || window.location.hostname || "";
  var statusEl = document.getElementById("teaching-contact-status");
  var submitBtn = document.getElementById("teaching-contact-submit");
  if (!workerUrl || !submitBtn) return;

  var defaultLabel = submitBtn.textContent;

  function setStatus(message, type) {
    if (!statusEl) return;
    statusEl.hidden = !message;
    statusEl.textContent = message || "";
    statusEl.classList.remove("is-error", "is-success", "is-pending");
    if (type) statusEl.classList.add(type);
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    setStatus("Sending your message…", "is-pending");
    submitBtn.disabled = true;
    submitBtn.textContent = "Sending…";

    var formData = new FormData(form);
    var payload = {
      name: formData.get("name"),
      phoneNumber: formData.get("phoneNumber"),
      email: formData.get("email"),
      message: formData.get("message"),
      source: source,
    };

    fetch(workerUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    })
      .then(function (response) {
        if (!response.ok) {
          return response.text().then(function (text) {
            throw new Error(text || "Request failed");
          });
        }
        return response.json().catch(function () {
          return {};
        });
      })
      .then(function () {
        form.reset();
        setStatus("Thanks — your message was sent. I’ll get back to you soon.", "is-success");
      })
      .catch(function () {
        setStatus(
          "Something went wrong. Please try again or email work@prajwalyashasvi.in directly.",
          "is-error"
        );
      })
      .finally(function () {
        submitBtn.disabled = false;
        submitBtn.textContent = defaultLabel;
      });
  });
})();
