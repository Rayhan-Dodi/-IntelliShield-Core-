<?php
// Purpose: Mediator between popup.js and Python backend (features_extraction.py)

header("Access-Control-Allow-Origin: *");
header("Content-Type: text/plain");

// Get data from popup.js
$url  = isset($_POST['url'])  ? trim($_POST['url'])  : '';
$html = isset($_POST['html']) ? $_POST['html'] : '';

// Basic validation
if (empty($url)) {
    echo "Error: No URL received.";
    exit;
}

// Save the received HTML to a file for Python to analyze (if needed)
file_put_contents('markup.txt', $html);

// Prepare command to run Python script
// IMPORTANT: Change this path to your actual Python 3 path
$python_path = "/usr/bin/python3";           // Linux / macOS (common)
$script_path = "features_extraction.py";     // Your Python file

// For Windows, use something like:
// $python_path = "C:\\Python39\\python.exe";

$command = escapeshellcmd($python_path . " " . $script_path . " " . escapeshellarg($url));

// Execute Python script and get result
$decision = exec($command . " 2>&1", $output, $return_var);

// Debug output (uncomment when testing)
// echo "Debug: Command = $command\n";
// echo "Debug: Return code = $return_var\n";
// echo "Debug: Raw output = " . implode("\n", $output) . "\n";

if ($return_var !== 0) {
    echo "Error executing Python script. Please check server logs.";
} else {
    echo $decision ?: "Analysis completed. No output from Python.";
}
?>