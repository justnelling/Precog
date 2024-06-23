document.addEventListener("DOMContentLoaded", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const url = tabs[0].url;
    chrome.runtime.sendMessage(
      { action: "fetchURLKeywords", url: url },
      (response) => {
        if (response && response.success) {
          console.log("RAG process activated");
        } else {
          console.error("Failed to activate RAG process");
        }
      }
    );
  });

  // Fetch and display any existing insights when the popup loads
  chrome.storage.local.get("insights", (data) => {
    if (data.insights) {
      document.getElementById("insights").value = JSON.stringify(
        data.insights,
        null,
        2
      );
    }
  });

  // Listen for messages from the background script
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "updateInsights" && request.insights) {
      document.getElementById("insights").value = JSON.stringify(
        request.insights,
        null,
        2
      );
    }
  });
});
