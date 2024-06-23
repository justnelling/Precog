//? All variables and functions need to be defined within 1 function rn, because of how chrome extensions serialize the function calls. Just be mindful of this until we have time to research more into chrome extensions.

chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: URLKeywords,
  });
});

function URLKeywords() {
  const url = window.location.href;

  // submit url to backend
  async function submitURL(url) {
    const response = await fetch(
      `http://127.0.0.1:8000/submit-url?url=${encodeURIComponent(url)}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    if (!response.ok) {
      throw new Error("Failed to submit URL");
    }
    return url;
  }

  // fetch keywords from backend
  async function fetchKeywords(url) {
    const response = await fetch(
      `http://127.0.0.1:8000/keywords?url=${encodeURIComponent(url)}`
    );

    if (response.status === 404) {
      return null;
    }
    if (!response.ok) {
      throw new Error("Failed to fetch keywords");
    }

    const data = await response.json();
    return data;
  }

  // Poll for keywords with exponential backoff
  //! This is important to await response from server async functions to generate keywords from LLM
  async function pollForKeywords(url, maxAttempts = 10) {
    let attempts = 0;
    const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

    while (attempts < maxAttempts) {
      attempts++;
      const keywords = await fetchKeywords(url);
      if (keywords) {
        return keywords;
      }
      await delay(2 ** attempts * 1000); // Exponential backoff
    }
    throw new Error("Max attempts reached. Keywords not found.");
  }

  // async anon function
  (async () => {
    try {
      await submitURL(url);
      const keywords = await pollForKeywords(url);
      console.log("Keywords received: ", keywords);
    } catch (error) {
      console.error("Error: ", error);
    }
  })();
}
