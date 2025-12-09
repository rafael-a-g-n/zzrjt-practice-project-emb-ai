// Sentiment Analysis Application - Modern JavaScript

function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const responseDiv = document.getElementById("system_response");
    const loadingDiv = document.getElementById("loading");
    const submitButton = document.getElementById("submitButton");

    // Clear previous results
    responseDiv.innerHTML = "";
    responseDiv.className = "";

    // Show loading state
    loadingDiv.classList.add("active");
    submitButton.disabled = true;

    // Create XMLHttpRequest
    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState === 4) {
            // Hide loading state
            loadingDiv.classList.remove("active");
            submitButton.disabled = false;

            if (this.status === 200) {
                // Success - valid sentiment analysis
                const responseText = xhttp.responseText;
                responseDiv.innerHTML = responseText;
                
                // Detect sentiment type and apply appropriate class
                // Check for lowercase sentiment labels (after SENT_ prefix is removed)
                if (responseText.toLowerCase().includes('positive')) {
                    responseDiv.classList.add("sentiment-positive");
                } else if (responseText.toLowerCase().includes('negative')) {
                    responseDiv.classList.add("sentiment-negative");
                } else if (responseText.toLowerCase().includes('neutral')) {
                    responseDiv.classList.add("sentiment-neutral");
                } else {
                    responseDiv.classList.add("success");
                }
            } else if (this.status === 400 || this.status === 500) {
                // Error - invalid or blank input
                responseDiv.innerHTML = xhttp.responseText;
                responseDiv.classList.add("error");
            } else {
                // Unexpected error
                responseDiv.innerHTML = "An unexpected error occurred. Please try again.";
                responseDiv.classList.add("error");
            }
        }
    };

    xhttp.onerror = function() {
        // Network error
        loadingDiv.classList.remove("active");
        submitButton.disabled = false;
        responseDiv.innerHTML = "Network error. Please check your connection.";
        responseDiv.classList.add("error");
    };

    // Send request
    xhttp.open("GET", "sentimentAnalyzer?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}

// Allow Enter key to submit (Shift+Enter for new line)
document.addEventListener("DOMContentLoaded", function() {
    const textarea = document.getElementById("textToAnalyze");
    if (textarea) {
        textarea.addEventListener("keydown", function(event) {
            if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault();
                RunSentimentAnalysis();
            }
        });
    }
});

