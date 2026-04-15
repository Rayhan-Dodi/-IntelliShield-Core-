// Purpose: Gets the current tab URL and full page HTML, then sends to your local server

$(document).ready(function() {

    // Show current URL immediately when popup opens
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        let tab = tabs[0];
        if (tab) {
            $("#p1").text("The URL being tested is - " + tab.url);
        }
    });

    // Main button click handler
    $("button").click(function() {
        transfer();
    });
});

function transfer() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        let tab = tabs[0];
        if (!tab) {
            $("#div1").text("Error: Cannot access current tab.");
            return;
        }

        let tablink = tab.url;
        $("#p1").text("The URL being tested is - " + tablink);

        // Get the full HTML of the current webpage (via content script)
        chrome.tabs.sendMessage(tab.id, {action: "getPageHTML"}, function(response) {
            if (!response || !response.html) {
                $("#div1").text("Error: Could not read page content.");
                return;
            }

            let markup = "url=" + encodeURIComponent(tablink) + 
                        "&html=" + encodeURIComponent(response.html);

            // Send data to your local server
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "http://localhost/IntelliShield-Core/clientServer.php", true);
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        $("#div1").html(xhr.responseText);
                    } else {
                        $("#div1").html("Error connecting to server: " + xhr.status);
                    }
                }
            };

            xhr.send(markup);
        });
    });
}