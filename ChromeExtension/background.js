//? All variables and functions need to be defined within 1 function rn, because of how chrome extensions serialize the function calls. Just be mindful of this until we have time to research more into chrome extensions.

chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: sendURLToBackend,
  });
});

function sendURLToBackend() {
  const url = window.location.href;

  fetch("http://127.0.0.1:8000/submit-url", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url: url }),
  })
    .then((response) => response.json())
    .then((data) => console.log("Success: ", data))
    .catch((error) => {
      console.error("Error: ", error);
    });
}
