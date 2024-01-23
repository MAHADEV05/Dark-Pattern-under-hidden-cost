// content.js

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'detectHiddenCosts') {
      // Get the text content of the webpage
      const pageText = document.body.innerText;
  
      // Send the text content to the machine learning backend for prediction
      fetch('http://localhost:5000/api/detect-hidden-costs', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: pageText }),
      })
      .then(response => response.json())
      .then(result => {
        if (result.hidden_costs_detected) {
          // Highlight the entire webpage if hidden costs are detected
          document.body.style.backgroundColor = 'yellow';
          document.body.style.color = 'red';
        } else {
          // Continue with your web scraping and text highlighting logic
          const hiddenCostKeywords = ['tax', 'extra charges', 'fees', 'shipping'];
  
          hiddenCostKeywords.forEach(keyword => {
            // Find elements containing the keyword in their text content on the entire webpage
            $(`:contains('${keyword}')`).each(function() {
              const originalText = $(this).text();
              const highlightedText = originalText.replace(new RegExp(`(${keyword})`, 'gi'), '<span style="background-color: yellow; color: red;">$1</span>');
              $(this).html(highlightedText);
            });
          });
        }
      })
      .catch(error => console.error('Error:', error));
    }
  });
  